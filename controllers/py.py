
from datetime import timedelta
from models import Workout, Meet, Attempt

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
