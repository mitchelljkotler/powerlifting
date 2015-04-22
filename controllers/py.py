
from sqlalchemy import func

from datetime import date, datetime, timedelta
from models import Exercise, Set, Workout, Meet, Attempt

class PyController(object):
    """Python functions to control"""

    def __init__(self, session, user):
        self.session = session
        self.user = user

    def add_workout(name='Workout', date=None):
        """Add a workout"""
        if not date:
            date = datetime.now()
        workout = Workout(name=name, date=date, user=self.user)
        self.session.add(workout)
        self.session.commit()
        return workout

    def get_workouts():
        """Get a list of workouts"""
        # date range
        workouts = self.session.query(Workout).all()
        for workout in workouts:
            print '{} - {} - {}'.format(workout.id, workout.date, workout.name)

    def get_workout(id):
        """Get a workout"""
        return self.session.query(Workout).filter_by(id=id).scalar()

    def get_exercise(name):
        """Get an exercise"""
        return self.session.query(Exercise).filter(func.lower(Exercise.name)==name.lower()).scalar()

    def add_set(workout, exercise, weight=0, reps=0, sets=1, rpe=None):
        """Add a set to a workout"""
        order = len(workout.sets)
        for _ in xrange(sets):
            set_ = Set(
                    order=order,
                    workout=workout,
                    exercise=exercise,
                    weight=weight,
                    reps=reps,
                    )
            self.session.add(set_)
            order += 1
        self.session.commit()

def add_meet(session, user):
    """add a meet"""
    name = raw_input('name:')
    date_ = raw_input('date:')
    date = date(*map(int, date_.split('-')))
    weight = raw_input('weight:')
    meet = Meet(name=name, date=date, user=user)
    session.add(meet)
    session.commit()
    for lift in  ['Squat', 'Bench Press', 'Deadlift']:
        print lift
        exercise = session.query(Exercise).find_by(name=lift)
        for attempt_num in xrange(1, 4):
            print 'attempt', attempt_num
            weight = raw_input('weight:')
            make = raw_input('make:')
            attempt = Attempt(order=attempt_number, exercise=exercise, weight=weight, meet=meet, make=bool(int(make)))
            session.add(attempt)
            session.commit()

def convert_meet(session, date):
    """convert a workout on a given date to a meet"""
    workout = session.query(Workout).filter(Workout.date>date, Workout.date<(date+timedelta(1))).one()
    meet = Meet(name=workout.name, date=date, user=workout.user)
    session.add(meet)
    session.commit()
    for exercise_name in ['Squat', 'Bench Press', 'Deadlift']:
        attempt_sets = [s for s in workout.sets if
                s.exercise.name == exercise_name][-3:]
        for i, attempt_set in enumerate(attempt_sets):
            attempt = Attempt(order=i, exercise=attempt_set.exercise,
                              weight=attempt_set.weight, meet=meet,
                              make=(attempt_set.reps==1))
            session.add(attempt)
            session.commit()
