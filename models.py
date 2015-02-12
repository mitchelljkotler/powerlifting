
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, \
        Boolean, Numeric, Enum, UniqueConstraint, CheckConstraint
from sqlalchemy import inspect
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, declared_attr
Base = declarative_base()

class PLMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class Exercise(Base, PLMixin):
    name = Column(String(255), unique=True, nullable=False)
    # make this an enum
    type = Column(Enum('squat', 'press', 'hinge', 'pull', 'other'),
        nullable=False, default='other')

    def __repr__(self):
        return 'Exercise: %s' % self.name

    def __unicode__(self):
        return self.name


class Set(Base, PLMixin):
    order = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=False)
    exercise = relationship('Exercise')
    weight = Column(Numeric(6, 2), nullable=False)
    reps = Column(Integer, nullable=False)
    workout_id = Column(Integer, ForeignKey('workout.id'), nullable=False)
    # type - warm up, workset, accessory
    # RPE

    __mapper_args__ = {'order_by': order}
    __table_args__ = (UniqueConstraint('order', 'workout_id'),)

    def __repr__(self):
        return 'Set: %s' % unicode(self)

    def __unicode__(self):
        return '%s: %sx%s' % (self.exercise, self.weight, self.reps)

    def beachle(self):
        """Beachle one rep max formula"""
        return self.weight * (1 + self.reps / 30.0)

    def brzycki(self):
        """Brzycki one rep max formula"""
        return self.weight * (36.0 / (37 - self.reps))

    def inol(self, max):
        """Calculate INOL based on a given max for this exercise"""
        return (self.reps / (100 * (1 - self.weight/float(max))))

    def tonnage(self):
        """Tonnage for the set"""
        return self.weight * self.reps


class Workout(Base, PLMixin):
    name = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    sets = relationship('Set', backref='workout', cascade='all, delete-orphan')

    def __repr__(self):
        return 'Workout: %s' % unicode(self)

    def __unicode__(self):
        set_string = '\n'.join(str(s) for s in self.sets)
        return '%s on %s\n%s' % (self.name, self.date, set_string)


class Attempt(Base, PLMixin):
    order = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=False)
    exercise = relationship('Exercise')
    weight = Column(Numeric(6, 2), nullable=False)
    meet_id = Column(Integer, ForeignKey('meet.id'), nullable=False)
    make = Column(Boolean, nullable=False)

    __mapper_args__ = {'order_by': (exercise, order)}

    def __repr__(self):
        return 'Attempt: %s' % str(self)

    def __unicode__(self):
        return '%s: %s' % (self.exercise, self.weight)


class Meet(Base, PLMixin):
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    attempts = relationship('Attempt', backref='meet')

    def __repr__(self):
        return 'Meet: %s' % str(self)

    def __unicode__(self):
        return '%s on %s' % (self.name, self.date)

    def wilks(self, weight):
        """Calculate wilks score"""
        mcoeffs = (-216.0475144, 16.2606339, -0.002388645,
                   -0.00113732, 7.01863E-06, -1.291E-08)
        fcoeffs = (594.31747775582, -27.23842536447, 0.82112226871,
                   -0.00930733913, 0.00004731582, -0.00000009054)

        weight_kg = weight * 0.453592
        session = inspect(self).session

        best_attempt = lambda lift:\
                session.Query(Attempt).join(Exercise)\
                .filter(Exercise.name==lift)\
                .filter(Attempt.make==True)\
                .order_by(Attempt.weight.desc())\
                .first().weight
        total = sum(best_attempt(lift) for lift in
                    ['Squat', 'Bench Press', 'Deadlift'])

        return ((total * 500) /
                sum(mcoeffs[i] * weight_kg ** i for i in xrange(6)))
