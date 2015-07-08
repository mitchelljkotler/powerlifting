from models import Exercise, Muscle

def make(exercise, muscle_types):
    return [ExerciseMuscleAssociation(
            session.query(Exercise).filter(Exercise.name==exercise).one(),
            session.query(Muscle).filter(Muscle.name==muscle).one(),
            type_,
            ) for muscle, type_ in muscle_types]

def exercise_muscles(session):

    session.add_all(make('Squat', [
        ('Quadriceps', 'primary'),
        ('Gluteus Maximus', 'primary'),
        ('Hamstrings', 'secondary'),
        ('Erector Spinae', 'secondary'),
        ('Rectus Abdominis', 'secondary'),
        ('Obliques', 'secondary'),
        ]))

    session.add_all(make('Bench Press', [
        ('Pectoralis Major, Sternal', 'primary'),
        ('Pectoralis Major, Clavicular', 'primary'),
        ('Triceps Brachii', 'primary'),
        ('Anterior Deltoid', 'secondary'),
        ]))

    session.add_all(make('Deadlift', [
        ('Erector Spinae', 'primary'),
        ('Gluteus Maximus', 'primary'),
        ('Hamstrings', 'primary'),
        ('Quadriceps', 'secondary'),
        ('Latissimus Dorsi', 'secondary'),
        ('Trapezius', 'secondary'),
        ('Rhomboids', 'secondary'),
        ]))
