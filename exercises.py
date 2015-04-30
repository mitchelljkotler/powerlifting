from models import Exercise
# XXX add descriptions to exercises?  better meta data?

exercises = [
    # the powerlifts
    Exercise(name='Squat', type='squat'),
    Exercise(name='Bench Press', type='press'),
    Exercise(name='Deadlift', type='hinge'),

    # the olympic lifts (including the old c&p)
    Exercise(name='Snatch', type='hinge'),
    Exercise(name='Clean & Jerk', type='hinge'),
    Exercise(name='Clean & Press', type='hinge'),

    # squats
    Exercise(name='High Bar Squat', type='squat'),
    Exercise(name='Front Squat', type='squat'),
    Exercise(name='Overhead Squat', type='squat'),
    Exercise(name='Split Squat', type='squat'),
    Exercise(name='Lunge', type='squat'),
    Exercise(name='Bulgarian Split Squat', type='squat'),
    Exercise(name='Pin Squat', type='squat'),
    Exercise(name='Paused Squat', type='squat'),
    Exercise(name='Box Squat', type='squat'),
    Exercise(name='Goblet Squat', type='squat'),
    Exercise(name='Hack Squat', type='squat'),

    # presses
    Exercise(name='Overhead Press', type='press'),
    Exercise(name='Push Press', type='press'),
    Exercise(name='Behind the Neck Press', type='press'),
    Exercise(name='Behind the Neck Push Press', type='press'),
    Exercise(name='Behind the Neck Jerk', type='press'),
    Exercise(name='Jerk', type='press'),
    Exercise(name='Power Jerk', type='press'),
    Exercise(name='Slingshot Bench Press', type='press'),
    Exercise(name='Close Grip Bench Press', type='press'),
    Exercise(name='Incline Bench Press', type='press'),
    Exercise(name='Dumbbell Bench Press', type='press'),
    Exercise(name='Dumbbell Incline Bench Press', type='press'),
    Exercise(name='Floor Press', type='press'),
    Exercise(name='JM Press', type='press'),
    Exercise(name='Board Press', type='press'),
    Exercise(name='2 Board Press', type='press'),
    Exercise(name='3 Board Press', type='press'),
    Exercise(name='4 Board Press', type='press'),
    Exercise(name='Pin Press', type='press'),
    Exercise(name='Paused Bench Press', type='press'),
    Exercise(name='Touch and Go Bench Press', type='press'),
    Exercise(name='Decline Bench Press', type='press'),
    Exercise(name='Dip', type='press'),
    Exercise(name='Ring Dip', type='press'),
    Exercise(name='Push Up', type='press'),

    # hinges ie deadlift variations
    Exercise(name='Sumo Deadlift', type='hinge'),
    Exercise(name='Romanian Deadlift', type='hinge'),
    Exercise(name='Straight Leg Deadlift', type='hinge'),
    Exercise(name='Good Morning', type='hinge'),
    Exercise(name='Power Clean', type='hinge'),
    Exercise(name='Power Snatch', type='hinge'),
    Exercise(name='Hang Clean', type='hinge'),
    Exercise(name='Hang Snatch', type='hinge'),
    Exercise(name='Hang Power Clean', type='hinge'),
    Exercise(name='Hang Power Snatch', type='hinge'),
    Exercise(name='Muscle Snatch', type='hinge'),
    Exercise(name='Clean', type='hinge'),
    Exercise(name='High Pull', type='hinge'),
    Exercise(name='Rack Pull', type='hinge'),
    Exercise(name='Block Pull', type='hinge'),
    Exercise(name='Deficit Deadlift', type='hinge'),
    Exercise(name='Snatch Grip Deadlift', type='hinge'),
    Exercise(name='Halting Deadlift', type='hinge'),
    Exercise(name='Paused Deadlift', type='hinge'),
    Exercise(name='Trap Bar Deadlift', type='hinge'),

    # pulls (upper back work)
    Exercise(name='Pendlay Row', type='pull'),
    Exercise(name='Dumbbell Row', type='pull'),
    Exercise(name='Chin Up', type='pull'),
    Exercise(name='Pull Up', type='pull'),
    Exercise(name='Lat Pulldown', type='pull'),
    Exercise(name='Chest Supported Row', type='pull'),
    Exercise(name='T Bar Row', type='pull'),
    Exercise(name='Upright Row', type='pull'),
    Exercise(name='Cable Row', type='pull'),

    # isolation exercises
    # biceps
    Exercise(name='Curl', type='other'),
    Exercise(name='Dumbbell Curl', type='other'),
    Exercise(name='Hammer Curl', type='other'),
    Exercise(name='Preacher Curl', type='other'),
    # triceps
    Exercise(name='Lying Triceps Extension', type='other'),
    Exercise(name='Triceps Extension', type='other'),
    Exercise(name='Triceps Pushdown', type='other'),
    Exercise(name='French Press', type='other'),
    Exercise(name='Triceps Kickback', type='other'),
    # delts
    Exercise(name='Lateral Raise', type='other'),
    Exercise(name='Front Raise', type='other'),
    Exercise(name='Rear Delt Fly', type='other'),
    Exercise(name='Face Pull', type='other'),
    # pecs
    Exercise(name='Cable Fly', type='other'),
    Exercise(name='Dumbbell Fly', type='other'),
    # traps
    Exercise(name='Shrug', type='other'),
    Exercise(name='Power Shrug', type='other'),
    # quads
    Exercise(name='Leg Extension', type='other'),
    Exercise(name='Leg Press', type='other'), # is this a squat?
    # hams
    Exercise(name='Leg Curl', type='other'),
    Exercise(name='Glute Ham Raise', type='other'),
    # calves
    Exercise(name='Calf Raise', type='other'),
    Exercise(name='Seated Calf Raise', type='other'),
    # glutes
    Exercise(name='Glute Bridge', type='other'),
    Exercise(name='Hip Thrust', type='other'),
    # erectors
    Exercise(name='Back Extension', type='other'),
    # abs
    Exercise(name='Sit Up', type='other'),
    Exercise(name='Ab Wheel', type='other'),
    Exercise(name='Side Bend', type='other'),
    Exercise(name='Plank', type='other'),
]
