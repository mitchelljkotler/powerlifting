
import os
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from exercises import exercises
from models import Base, Exercise, Set, Workout, User
from controllers.tsr_import import Import

db_file = 'pl.db'

engine = create_engine('sqlite:///%s' % db_file)
Session = sessionmaker(bind=engine)
session = Session()

if not os.path.exists(db_file):
    Base.metadata.create_all(engine)

    user = User(name='mitch')
    session.add(user)
    session.add_all(exercises)
    session.commit()
else:
    user = session.query(User).filter(User.name=='mitch').scalar()

squat = session.query(Exercise).filter_by(name='Squat').one()
bench = session.query(Exercise).filter_by(name='Bench Press').one()
dead  = session.query(Exercise).filter_by(name='Deadlift').one()

if __name__ == '__main__':
    # XXX only import new data
    importer = Import(session, user)
    importer.parse_all('/home/mitch/scratch/tsr/data/')

    # meets and weights
    convert_meet(session, date(2013, 10, 12))
    convert_meet(session, date(2014,  3, 29))
    convert_meet(session, date(2014, 10, 11))
    session.add_all([
        Weight(user=mitch, date=date(2013, 10, 12), weight=194),
        Weight(user=mitch, date=date(2014,  3, 29), weight=194),
        Weight(user=mitch, date=date(2014, 10, 11), weight=194),
        ])
    session.commit()
