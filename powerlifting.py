
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Exercise, Set, Workout
from controllers import CLI

db_file = 'pl.db'

engine = create_engine('sqlite:///%s' % db_file)
Session = sessionmaker(bind=engine)
session = Session()

if not os.path.exists(db_file):
    Base.metadata.create_all(engine)

    session.add_all([
        Exercise(name='Squat', type='squat'),
        Exercise(name='Bench Press', type='press'),
        Exercise(name='Deadlift', type='hinge'),
        Exercise(name='Snatch', type='hinge'),
        Exercise(name='Clean & Jerk', type='hinge'),
        Exercise(name='Front Squat', type='squat'),
        Exercise(name='Overhead Squat', type='squat'),
        Exercise(name='Split Squat', type='squat'),
        Exercise(name='Lunge', type='squat'),
        Exercise(name='Bulgarian Split Squat', type='squat'),
        Exercise(name='Overhead Press', type='press'),
        Exercise(name='Push Press', type='press'),
        Exercise(name='Jerk', type='press'),
        Exercise(name='Slingshot Bench Press', type='press'),
        Exercise(name='Close Grip Bench Press', type='press'),
        Exercise(name='Incline Bench Press', type='press'),
        Exercise(name='Dumbbell Bench Press', type='press'),
        Exercise(name='Dumbbell Incline Bench Press', type='press'),
        Exercise(name='Floor Press', type='press'),
        Exercise(name='Dip', type='press'),
        Exercise(name='Romanian Deadlift', type='hinge'),
        Exercise(name='Good Morning', type='hinge'),
        Exercise(name='Power Clean', type='hinge'),
        Exercise(name='Power Snatch', type='hinge'),
        Exercise(name='Clean', type='hinge'),
        Exercise(name='Pendlay Row', type='pull'),
        Exercise(name='Dumbbell Row', type='pull'),
        Exercise(name='Chin Up', type='pull'),
        Exercise(name='Pull Up', type='pull'),
        Exercise(name='Curl', type='other'),
        Exercise(name='Lying Triceps Extension', type='other'),
        Exercise(name='Lateral Raise', type='other'),
        Exercise(name='Front Raise', type='other'),
        Exercise(name='Face Pull', type='other'),
        Exercise(name='Flye', type='other'),
        Exercise(name='Back Extension', type='other'),
        Exercise(name='Sit Up', type='other'),
        Exercise(name='Ab Wheel', type='other'),
    ])
    session.commit()

if __name__ == '__main__':
    CLI(session).cmdloop()
