
from datetime import datetime
import os
import re

from models import Exercise, Set, Workout

class Import(object):

    p_first_line = re.compile(r'\*\*(?P<year>\d\d\d\d)-(?P<month>\d\d)-'
                              r'(?P<day>\d\d) (?P<hour>\d\d):(?P<min>\d\d)'
                              r'( - (?P<name>.*))?\*\*')
    p_exercise = re.compile(r'\*\*(?P<name>.*)\*\*')
    p_set = re.compile(r'\* (?P<weight>[0-9.]+) lbs x (?P<reps>\d+) reps')
    translate_exercise = {
            'Chin-Up': 'Chin Up',
            'Weighted Chin-Up': 'Chin Up',
            'Pull-Up': 'Pull Up',
            'Weighted Pull-Up': 'Pull Up',
            'Weighted Dip': 'Dip',
            'Bodyweight Dip': 'Dip',
            'Speed Squat': 'Squat',
            'Speed Bench Press': 'Bench Press',
            'Speed Deadlift': 'Deadlift',
            'Dumbbell Lateral Raise': 'Lateral Raise',
            'Lying Barbell Triceps Extension': 'Lying Triceps Extension',
            'Hyperextension': 'Back Extension',
            'Barbell Pin Press': 'Slingshot Bench Press',
            'Cable Crossover': 'Cable Fly',
            'Weighted Decline Sit Up': 'Sit Up',
            'Decline Sit-Up': 'Sit Up',
            'Block Pull (Below the Knee)': 'Block Pull',
            'Ring Dips': 'Ring Dip',
            'Kneeling Ab Roller': 'Ab Wheel',
            'Rope Triceps Extension': 'Triceps Pushdown',
            'Barbell Glute Bridge': 'Glute Bridge',
            'Chest-Supported Row': 'Chest Supported Row',
            'Clean and Press': 'Clean & Press',
            'Fly': 'Dumbbell Fly',
            'Paused Close Grip Bench Press': 'Close Grip Bench Press',
            }

    def __init__(self, session, user):
        self.session = session
        self.user = user

    def parse_file(self, file_name):
        """Read one file saved form TSR"""
        print 'Processing %s' % file_name

        with open(file_name) as file_:

            first = file_.readline()
            m_first = self.p_first_line.match(first)
            if not m_first:
                print 'Error: could not parse "%s" from %s' % (first, file_name)
                return
            date = datetime(
                    *[int(i) for i in m_first.group(
                        'year', 'month', 'day', 'hour', 'min')])
            name = m_first.group('name') or 'Default'
            workout = Workout(name=name, date=date, user=self.user)
            self.session.add(workout)
            self.session.commit()

            order = 0
            for line in file_:
                m_exercise = self.p_exercise.match(line)
                if m_exercise:
                    name = self.translate_exercise.get(m_exercise.group('name'),
                                                  m_exercise.group('name'))
                    exercise = self.session.query(Exercise).\
                            filter(Exercise.name==name).\
                            scalar()
                    if not exercise:
                        print 'Error: no exercise named %s' % name
                        self.session.rollback()
                        return
                m_set = self.p_set.match(line)
                if m_set:
                    set_ = Set(
                            order=order,
                            workout=workout,
                            exercise=exercise,
                            weight=m_set.group('weight'),
                            reps=m_set.group('reps'),
                            )
                    self.session.add(set_)
                    self.session.flush()
                    order += 1

        self.session.commit()

    def _get_last_workout_date(self):
        """get last workout date"""

        last = self.session.query(Workout).order_by(Workout.date.desc()).first()
        return last.date


    def parse_all(self, dir_path):
        """parse all files in a dir"""

        last_date = self._get_last_workout_date()
        last_date_str = last_date.strftime('%Y-%m-%d')
        files = [f for f in sorted(os.listdir(dir_path))
                if os.path.basename(f) > last_date_str]

        for file_ in files:
            self.parse_file(os.path.join(dir_path, file_))
