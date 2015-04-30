
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, \
        Boolean, Numeric, Enum, SmallInteger, \
        UniqueConstraint, CheckConstraint
from sqlalchemy import inspect
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql import func

from datetime import datetime
from decimal import Decimal
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

Base = declarative_base()

################################################################################
# General
################################################################################


class PLMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class User(Base, PLMixin):
    """User"""
    name = Column(String(255), unique=True, nullable=False)
    gender = Column(Enum('male', 'female'), nullable=False, default='male')

    def prs(self, exercise, date):
        """Get PRs for the given date"""
        session = inspect(self).session
        prs = [10, 8, 5, 3, 2, 1]
        for pr in prs:
            set_ = session.query(Set).join(Workout).join(User).\
                    filter(User.id==self.id).\
                    filter(Set.reps>=pr).\
                    filter(Workout.date<=date).\
                    filter(Set.exercise_id==exercise.id).\
                    order_by(Set.weight.desc(), Set.reps.desc()).first()
            if set_:
                print '%dRM - %.1fx%d - E1RM: %.1f' % (pr, set_.weight, set_.reps, set_.beachle())

    def graph_pl(self, data_type, date_begin, date_end=None):
        """Graph the power lifts"""
        session = inspect(self).session
        for exercise_name in ['Squat', 'Bench Press', 'Deadlift']:
            exercise = session.query(Exercise).filter(Exercise.name==exercise_name).one()
            self.graph(data_type, exercise, date_begin, date_end)
        plt.legend()
        plt.show()

    def graph(self, data_type, exercise, date_begin, date_end=None):
        """Graph user data"""
        if date_end is None:
            date_end = datetime.now()
        session = inspect(self).session
        dates = session.query(Workout.date).join(Set).\
                filter(Set.exercise==exercise).\
                filter(Workout.date>date_begin, Workout.date<date_end).\
                order_by(Workout.date.asc()).distinct().all()
        data_values = {
                'tonnage': func.sum(Set.weight * Set.reps),
                'intensity': func.max(Set.weight),
                }
        data = [session.query(data_values[data_type]).
                filter(Set.exercise==exercise).
                join(Workout).filter(Workout.date==d[0]).
                filter(Set.reps>0).one()
                for d in dates]
        plt.plot(dates, data, '-o', label=exercise.name)
        plt.title(data_type.capitalize())

    def get_weight(self, date, unit='lbs'):
        """Get user's weight on a given date in the given units"""
        session = inspect(self).session
        weight = session.query(Weight).filter(Weight.user==self).\
                                       filter(Weight.date<=date).\
                                       first()
        return weight.convert(unit)


class Exercise(Base, PLMixin):
    name = Column(String(255), unique=True, nullable=False)
    type = Column(Enum('squat', 'press', 'hinge', 'pull', 'other'),
        nullable=False, default='other')

    def __repr__(self):
        return 'Exercise: %s' % self.name

    def __unicode__(self):
        return self.name


''
################################################################################
# Weight Tracking
################################################################################


class Weight(Base, PLMixin):
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    weight = Column(Numeric(5, 2), nullable=False)
    weight_unit = Column(Enum('lbs', 'kgs'), nullable=False, default='lbs')

    __mapper_args__ = {'order_by': 'weight."date" DESC'}

    def __unicode__(self):
        return '%s: %s%s on %s' % (self.user, self.weight, self.weight_unit, self.date)

    def convert(self, unit='lbs'):
        """Convert units"""
        if unit == self.weight_unit:
            return self.weight
        if unit == 'lbs':
            return self.weight * Decimal('2.2046')
        if unit == 'kgs':
            return self.weight * Decimal('0.4536')
        raise ValueError

''
################################################################################
# Workout Tracking
################################################################################


class Set(Base, PLMixin):
    order = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=False)
    exercise = relationship('Exercise')
    weight = Column(Numeric(6, 2), nullable=False)
    weight_unit = Column(Enum('lbs', 'kgs'), nullable=False, default='lbs')
    reps = Column(Integer, nullable=False)
    workout_id = Column(Integer, ForeignKey('workout.id'), nullable=False)
    type = Column(Enum('warmup', 'work', 'accessory'),
        nullable=False, default='work')
    rpe = Column(Numeric(3, 1), CheckConstraint('rpe<=10 AND rpe>=0'), nullable=True)

    __mapper_args__ = {'order_by': order}
    __table_args__ = (UniqueConstraint('order', 'workout_id'),)

    def __repr__(self):
        return 'Set: %s' % unicode(self)

    def __unicode__(self):
        return '%s: %sx%s' % (self.exercise, self.weight, self.reps)

    def beachle(self):
        """Beachle one rep max formula"""
        if self.reps == 1:
            return self.weight
        return float(self.weight) * (1 + self.reps / 30.0)

    def brzycki(self):
        """Brzycki one rep max formula"""
        return float(self.weight) * (36.0 / (37 - self.reps))

    def inol(self, max):
        """Calculate INOL based on a given max for this exercise"""
        return (self.reps / (100 * (1 - float(self.weight)/float(max))))

    def tonnage(self):
        """Tonnage for the set"""
        return self.weight * self.reps


class Workout(Base, PLMixin):
    name = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    sets = relationship('Set', backref='workout', cascade='all, delete-orphan')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='workouts')

    __mapper_args__ = {'order_by': 'workout."date" ASC'}

    def __repr__(self):
        return 'Workout: %s' % unicode(self)

    def __unicode__(self):
        return '%s on %s' % (self.name, self.date)

''
################################################################################
# Meet Tracking
################################################################################


class Attempt(Base, PLMixin):
    order = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=False)
    exercise = relationship('Exercise')
    weight = Column(Numeric(6, 2), nullable=False)
    weight_unit = Column(Enum('lbs', 'kgs'), nullable=False, default='lbs')
    meet_id = Column(Integer, ForeignKey('meet.id'), nullable=False)
    make = Column(Boolean, nullable=False)

    __mapper_args__ = {'order_by': 'attempt."exercise_id" ASC, attempt."order" ASC'}

    def __repr__(self):
        return 'Attempt: %s' % unicode(self)

    def __unicode__(self):
        return '%s: %s - %s' % (self.exercise, self.weight, 'Make' if self.make else 'Miss')

    def convert(self, unit='lbs'):
        """Convert units"""
        if unit == self.weight_unit:
            return self.weight
        if unit == 'lbs':
            return self.weight * Decimal('2.2046')
        if unit == 'kgs':
            return self.weight * Decimal('0.4536')
        raise ValueError


class Meet(Base, PLMixin):
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    attempts = relationship('Attempt', backref='meet')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='meets')

    def __repr__(self):
        return 'Meet: %s' % unicode(self)

    def __unicode__(self):
        return '%s on %s' % (self.name, self.date)

    def total(self):
        """Total"""
        session = inspect(self).session

        best_attempt = lambda lift:\
                session.query(Attempt).join(Exercise).join(Meet)\
                .filter(Attempt.meet==self)\
                .filter(Exercise.name==lift)\
                .filter(Attempt.make==True)\
                .order_by(Attempt.weight.desc())\
                .first().convert('kgs')
        return float(sum(best_attempt(lift) for lift in
                    ['Squat', 'Bench Press', 'Deadlift']))

    def wilks(self):
        """Calculate wilks score"""
        mcoeffs = (-216.0475144, 16.2606339, -0.002388645,
                   -0.00113732, 7.01863E-06, -1.291E-08)
        fcoeffs = (594.31747775582, -27.23842536447, 0.82112226871,
                   -0.00930733913, 0.00004731582, -0.00000009054)
        coeffs = mcoeffs if self.user.gender == 'male' else fcoeffs

        weight = float(self.user.get_weight(self.date, unit='kgs'))
        return ((self.total() * 500) /
                sum(coeffs[i] * weight ** i for i in xrange(6)))

    def prs(self):
        """PRs prior to this meet"""
        session = inspect(self).session
        for exercise_name in ['Squat', 'Bench Press', 'Deadlift']:
            print exercise_name
            exercise = session.query(Exercise).filter_by(name=exercise_name).one()
            self.user.prs(exercise, self.date)
            print

''
################################################################################
# Program
################################################################################

class ProgramWeight(Base, PLMixin):
    """How to set the weight for a set"""

    type = Column(Enum('add', 'percantage'), nullable=False)

    # add
    amount = Column(Integer, nullable=True)
    which = Column(Enum('any', 'workout'), nullable=False, default='workout')
    often = Column(Integer, nullable=True)

    # percantage
    percantage = Column(Integer, nullable=True)

class ProgramSet(Base, PLMixin):
    """A set in a program"""

    order = Column(Integer, nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercise.id'), nullable=False)
    exercise = relationship('Exercise')
    reps = Column(Integer, nullable=False)
    amrap = Column(Boolean, nullable=False)
    workout_id = Column(Integer, ForeignKey('programworkout.id'), nullable=False)
    type = Column(Enum('warmup', 'work', 'accessory'),
        nullable=False, default='work')

    weight_id = Column(Integer, ForeignKey('programweight.id'), nullable=False)
    weight = relationship('ProgramWeight')

    __mapper_args__ = {'order_by': order}
    __table_args__ = (UniqueConstraint('order', 'workout_id'),)

    def __repr__(self):
        return 'Set: %s' % unicode(self)

    def __unicode__(self):
        return '%s: %sx%s' % (self.exercise, self.weight, self.reps)


class ProgramWorkout(Base, PLMixin):
    """A program workout"""

    name = Column(String(255), nullable=False)
    program_id = Column(Integer, ForeignKey('program.id'), nullable=False)
    sets = relationship('ProgramSet', backref='workout')


class Program(Base, PLMixin):
    """A program"""

    name = Column(String(255), nullable=False)
    workouts = relationship('ProgramWorkout', backref='program')
    days = Column(SmallInteger, nullable=False)

    def get_days(self):
        """Convert days from a small int to list"""
        return [(self.days >> i) & 1 for i in xrange(7)]

    def set_days(self, days):
        self.days = sum((n << i) for i, n in enumerate(days))

    def __unicode__(self):
        return self.name


