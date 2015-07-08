
import os
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from exercises import exercises
from muscles import muscles
from exercise_muscles import exercise_muscles
from models import Base, Exercise, Set, Workout, User, Weight
from controllers.tsr_import import Import
from controllers.py import convert_meet

db_file = 'pl.db'

engine = create_engine('sqlite:///%s' % db_file)
Session = sessionmaker(bind=engine)
session = Session()

if not os.path.exists(db_file):
    Base.metadata.create_all(engine)

    user = User(name='mitch')
    session.add(user)
    session.add_all(muscles)
    session.add_all(exercises)
    exercise_muscles(session)
    session.commit()
else:
    user = session.query(User).filter(User.name=='mitch').scalar()

squat = session.query(Exercise).filter_by(name='Squat').one()
bench = session.query(Exercise).filter_by(name='Bench Press').one()
dead  = session.query(Exercise).filter_by(name='Deadlift').one()

if __name__ == '__main__':
    importer = Import(session, user)
    importer.parse_all('./tsr/data/')

    # meets and weights
    meet_dates_weights = [
            (date(2013, 10, 12,), 194),
            (date(2014,  3, 29,), 194),
            (date(2014, 10, 11,), 194),
            (date(2015,  4, 26,), 195),
            ]
    for date_, weight in meet_dates_weights:
        convert_meet(session, date_)
        session.add(Weight(user=user, date=date_, weight=weight))
    session.commit()
