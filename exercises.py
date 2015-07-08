from models import Exercise
# XXX better meta data?
# ROM modifer?
#  way to specify attributes other than weight, ie distance, time, etc
# pause identifier?
# chains/bands

exercises = [
    # the powerlifts
    Exercise(
        name='Squat',
        type='squat',
        description='Low bar powerlifting style back squat'),
    Exercise(
        name='Bench Press',
        type='press',
        plane='horizontal',
        description='Powerlifting competition style paused bench press'),
    Exercise(
        name='Deadlift',
        type='hinge',
        description='Powerlifting competition style deadlift'),

    # the olympic lifts (including the old c&p)
    Exercise(name='Clean & Press', type='hinge', dynamic=True),
    Exercise(name='Snatch', type='hinge', dynamic=True),
    Exercise(name='Clean & Jerk', type='hinge', dynamic=True),

    # squats
    Exercise(
        name='High Bar Squat',
        type='squat',
        description='High bar olympic style back squat'),
    Exercise(name='Front Squat', type='squat'),
    Exercise(name='Overhead Squat', type='squat'),
    Exercise(name='Split Squat', type='squat', laterality='unilateral'),
    Exercise(name='Lunge', type='squat', laterality='unilateral'),
    Exercise(
        name='Bulgarian Split Squat',
        type='squat',
        laterality='unilateral'),
    Exercise(name='Pin Squat', type='squat'),
    Exercise(name='Paused Squat', type='squat'),
    Exercise(name='Box Squat', type='squat'),
    Exercise(name='Zercher Squat', type='squat'),
    Exercise(name='Goblet Squat', type='squat', equipment='dumbbell'),
    Exercise(name='Barbell Hack Squat', type='squat'),
    Exercise(name='Machine Hack Squat', type='squat', equipment='machine'),

    # presses
    Exercise(name='Overhead Press', type='press', plane='vertical'),
    Exercise(name='Push Press', type='press', plane='vertical', dynamic=True),
    Exercise(name='Behind the Neck Press', type='press', plane='vertical'),
    Exercise(
        name='Sntach Grip Behind the Neck Press',
        type='press',
        plane='vertical',
        description='The Klokov press'),
    Exercise(
        name='Behind the Neck Push Press',
        type='press',
        dynamic=True,
        plane='vertical'),
    Exercise(
        name='Dumbbell Overhead Press',
        type='press',
        equipment='dumbbell',
        plane='vertical'),
    Exercise(
        name='Behind the Neck Jerk',
        type='press',
        dynamic=True,
        plane='vertical'),
    Exercise(name='Jerk', type='press', dynamic=True, plane='vertical'),
    Exercise(name='Power Jerk', type='press', dynamic=True, plane='vertical'),

    Exercise(name='Slingshot Bench Press', type='press', plane='horizontal'),
    Exercise(name='Close Grip Bench Press', type='press', plane='horizontal'),
    Exercise(name='Incline Bench Press', type='press', plane='horizontal'),
    Exercise(
        name='Dumbbell Bench Press',
        type='press',
        equipment='dumbbell',
        plane='horizontal'),
    Exercise(
        name='Dumbbell Incline Bench Press',
        type='press',
        equipment='dumbbell',
        plane='horizontal'),
    Exercise(name='Floor Press', type='press', plane='horizontal'),
    Exercise(name='JM Press', type='press', plane='horizontal'),
    Exercise(name='Board Press', type='press', plane='horizontal'),
    Exercise(name='2 Board Press', type='press', plane='horizontal'),
    Exercise(name='3 Board Press', type='press', plane='horizontal'),
    Exercise(name='4 Board Press', type='press', plane='horizontal'),
    Exercise(name='Pin Press', type='press', plane='horizontal'),
    Exercise(
        name='Paused Bench Press',
        type='press',
        plane='horizontal',
        description='A bench press with a pause longer than competition style'),
    Exercise(name='Touch and Go Bench Press', type='press', plane='horizontal'),
    Exercise(name='Decline Bench Press', type='press', plane='horizontal'),

    Exercise(name='Dip', type='press', equipment='bodyweight'),
    Exercise(name='Ring Dip', type='press', equipment='bodyweight'),
    Exercise(name='Push Up', type='press', plane='horizontal'),

    # hinges ie deadlift variations
    Exercise(name='Sumo Deadlift', type='hinge'),
    Exercise(name='Romanian Deadlift', type='hinge'),
    Exercise(name='Straight Leg Deadlift', type='hinge'),
    Exercise(name='Good Morning', type='hinge'),
    Exercise(name='Power Clean', type='hinge', dynamic=True),
    Exercise(name='Power Snatch', type='hinge', dynamic=True),
    Exercise(name='Hang Clean', type='hinge', dynamic=True),
    Exercise(name='Hang Snatch', type='hinge', dynamic=True),
    Exercise(name='Hang Power Clean', type='hinge', dynamic=True),
    Exercise(name='Hang Power Snatch', type='hinge', dynamic=True),
    Exercise(name='Muscle Snatch', type='hinge', dynamic=True),
    Exercise(name='Clean', type='hinge', dynamic=True),
    Exercise(name='High Pull', type='hinge', dynamic=True),
    Exercise(name='Rack Pull', type='hinge'),
    Exercise(name='Block Pull', type='hinge'),
    Exercise(name='Deficit Deadlift', type='hinge'),
    Exercise(name='Snatch Grip Deadlift', type='hinge'),
    Exercise(name='Halting Deadlift', type='hinge'),
    Exercise(name='Paused Deadlift', type='hinge'),
    Exercise(name='Trap Bar Deadlift', type='hinge', equipment='trap bar'),

    # pulls (upper back work)
    Exercise(name='Pendlay Row', type='pull', plane='horizontal'),
    Exercise(
        name='Dumbbell Row',
        type='pull',
        equipment='dumbbell',
        plane='horizontal'),
    Exercise(
        name='Chest Supported Row',
        type='pull',
        equipment='machine',
        plane='horizontal'),
    Exercise(name='T Bar Row', type='pull', plane='horizontal'),
    Exercise(
        name='Cable Row',
        type='pull',
        equipment='cable',
        plane='horizontal'),
    Exercise(name='Upright Row', type='pull'),

    Exercise(
        name='Chin Up',
        type='pull',
        equipment='bodyweight',
        plane='vertical'),
    Exercise(
        name='Pull Up',
        type='pull',
        equipment='bodyweight',
        plane='vertical'),
    Exercise(
        name='Lat Pulldown',
        type='pull',
        equipment='cable',
        plane='vertical'),

    # isolation exercises
    # biceps
    Exercise(name='Curl', type='other'),
    Exercise(name='Dumbbell Curl', type='other', equipment='dumbbell'),
    Exercise(name='Hammer Curl', type='other', equipment='dumbbell'),
    Exercise(name='Preacher Curl', type='other', equipment='ez bar'),
    # triceps
    Exercise(
        name='Lying Triceps Extension',
        type='other',
        equipment='ez bar',
        description='Rippetoe style, EZ bar to behind the head'),
    Exercise(name='Triceps Extension', type='other'),
    Exercise(name='Triceps Pushdown', type='other', equipment='cable'),
    Exercise(name='French Press', type='other'),
    Exercise(name='Triceps Kickback', type='other', equipment='dumbbell'),
    # delts
    Exercise(name='Lateral Raise', type='other', equipment='dumbbell'),
    Exercise(name='Front Raise', type='other'),
    Exercise(name='Rear Delt Fly', type='other', equipment='dumbbell'),
    Exercise(name='Face Pull', type='other', equipment='cable'),
    # pecs
    Exercise(name='Dumbbell Fly', type='other', equipment='dumbbell'),
    Exercise(name='Cable Fly', type='other', equipment='cable'),
    # traps
    Exercise(name='Shrug', type='other'),
    Exercise(name='Power Shrug', type='other'),
    # quads
    Exercise(name='Leg Extension', type='other', equipment='machine'),
    Exercise(name='Leg Press', type='other', equipment='machine'), # is this a squat?
    # hams
    Exercise(name='Leg Curl', type='other', equipment='machine'),
    Exercise(name='Glute Ham Raise', type='other', equipment='bodyweight'),
    # calves
    Exercise(name='Calf Raise', type='other'),
    Exercise(name='Seated Calf Raise', type='other', equipment='machine'),
    # glutes
    Exercise(name='Glute Bridge', type='other'),
    Exercise(name='Hip Thrust', type='other'),
    # erectors
    Exercise(name='Back Extension', type='other', equipment='bodyweight'),
    # abs
    Exercise(name='Sit Up', type='other', equipment='bodyweight'),
    Exercise(name='Ab Wheel', type='other'),
    Exercise(name='Side Bend', type='other'),
    Exercise(name='Plank', type='other', equipment='bodyweight'),
]
