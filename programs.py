
from models import Program, ProgramWorkout, ProgramSet, Exercise
from decimal import Decimal

def texas(session):

    squat = session.query(Exercise).filter_by(name='Squat').one()
    bench = session.query(Exercise).filter_by(name='Bench Press').one()
    dead  = session.query(Exercise).filter_by(name='Deadlift').one()

    ohp = session.query(Exercise).filter_by(name='Overhead Press').one()
    rdl = session.query(Exercise).filter_by(name='Romanian Deadlift').one()
    chinup = session.query(Exercise).filter_by(name='Chin Up').one()

    tm = Program(name='Texas Method')
    session.add(tm)

    vd = ProgramWorkout(name='Volume Day', program=tm)
    ld = ProgramWorkout(name='Light Day', program=tm)
    id = ProgramWorkout(name='Intensity Day', program=tm)
    session.add_all([vd, ld, id])

    ### vd

    for i in xrange(5):
        session.add(ProgramSet(
                order=i,
                exercise=squat,
                reps=5,
                workout=vd,
                weight_percent=Decimal('76.5')
                ))

    for i in xrange(5):
        session.add(ProgramSet(
                order=5+i,
                exercise=bench,
                reps=5,
                workout=vd,
                weight_percent=Decimal('76.5')
                ))

    for i in xrange(3):
        session.add(ProgramSet(
                order=10+i,
                exercise=rdl,
                reps=5,
                workout=vd,
                weight_percent=Decimal('76.5')
                ))
    ### ld

    for i in xrange(2):
        session.add(ProgramSet(
                order=i,
                exercise=squat,
                reps=5,
                workout=ld,
                weight_percent=Decimal('61.2')
                ))

    for i in xrange(3):
        session.add(ProgramSet(
                order=2+i,
                exercise=ohp,
                reps=5,
                workout=ld,
                weight_percent=Decimal('72.7')
                ))

    for i in xrange(3):
        session.add(ProgramSet(
                order=5+i,
                exercise=chinup,
                reps=5,
                workout=ld,
                weight_percent=Decimal('76.5')
                ))
    ### id

    for i in xrange(3):
        session.add(ProgramSet(
                order=i,
                exercise=squat,
                reps=2,
                workout=id,
                weight_percent=Decimal(85 + 5 * i)
                ))

    for i in xrange(3):
        session.add(ProgramSet(
                order=3+i,
                exercise=bench,
                reps=3,
                workout=id,
                weight_percent=Decimal(80 + 5 * i)
                ))

    for i in xrange(2):
        session.add(ProgramSet(
                order=6+i,
                exercise=dead,
                reps=3,
                workout=id,
                weight_percent=Decimal(90 - 10 * i)
                ))

    return tm
