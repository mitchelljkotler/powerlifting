from sqlalchemy import func

from cmd import Cmd
from datetime import datetime, timedelta
from shlex import shlex

from models import Exercise, Set, Workout

class CLI(Cmd):
    """Input from the command line"""

    prompt = '> '

    def __init__(self, session):
        Cmd.__init__(self)
        self.session = session
        self.current_workout = None
        self.current_exercise = None
        self.current_order = None

    def do_EOF(self, line):
        """End on EOF"""
        return True

    def _parse_args(self, line, num):
        """Parse command args"""
        lex = shlex(line, posix=True)
        lex.whitespace_split = True
        args = []
        for _ in xrange(num):
            args.append(lex.get_token())
        return args

    def _parse_date(self, date):
        for sep in ['/', '-', '.']:
            if sep in date:
                date = map(int, date.split('/'))
                if len(date) == 2:
                    month, day = date
                    year = datetime.now().year
                else:
                    month, day, year = date
                date = datetime(year, month, day)
                return date
        raise ValueError

    def do_workout(self, line):
        """workout [name] [date]"""
        name, date = self._parse_args(line, 2)
        if not name:
            name = 'Workout'
        if not date:
            date = datetime.now()
        else:
            try:
                date = self._parse_date(date)
            except ValueError:
                print 'Bad date format: mm/dd[/yyyy]'
                return
        self.current_workout = Workout(name=name, date=date)
        self.current_order = 0
        self.session.add(self.current_workout)
        self.session.commit()

    def do_show_workout(self, line):
        """Print the current workout"""
        print str(self.current_workout)

    def do_all_workouts(self, line):
        """Show all workouts"""
        dates = self._parse_args(line, 2)
        dates = [self._parse_date(date) for date in dates if date]
        if len(dates) == 2:
            workouts = self.session.query(Workout)\
                                   .filter(Workout.date > dates[0])\
                                   .filter(Workout.date < dates[1])\
                                   .all()
        elif len(dates) == 1:
            workouts = self.session.query(Workout)\
                                   .filter(Workout.date > dates[0])\
                                   .filter(Workout.date < (dates[0] + timedelta(1)))\
                                   .all()
        else:
            workouts = self.session.query(Workout).all()
        for workout in workouts:
            print '%s: %s - %s' % (workout.id, workout.date, workout.name)

    def do_choose_workout(self, line):
        """Choose a workout"""
        self.current_workout = self.session.query(Workout)\
                                           .filter(Workout.id == line)\
                                           .scalar()
        self.current_order = len(self.current_workout.sets)

    def do_delete_workout(self, line):
        """Delete a workout"""
        workout = self._parse_args(line, 1)[0]
        if workout:
            workout = self.session.query(Workout)\
                                  .filter(Workout.id == workout)\
                                  .scalar()
        else:
            workout = self.current_workout
        confirm = raw_input('Delete workout:\n%s\n[yn]? ' % workout)
        if confirm == 'y':
            self.session.delete(workout)
            self.session.commit()
            print 'Deleted'

    def do_exercise(self, line):
        """Add an exercise"""
        name = line
        self.current_exercise = self.session.query(Exercise)\
                .filter(func.lower(Exercise.name) == func.lower(name)).\
                first()
        print self.current_exercise

    def complete_exercise(self, text, line, begidx, endidx):
        mline = line.split(None, 1)[1]
        offs = len(mline) - len(text)
        return [e.name[offs:] for e in
                self.session.query(Exercise)
                .filter(Exercise.name.ilike('%s%%' % mline))
                .all()]

    def do_search_exercise(self, line):
        """search exercise"""
        exercises = self.session.query(Exercise)\
                                .filter(Exercise.name.ilike('%%%s%%' % line))\
                                .all()
        for exercise in exercises:
            print exercise

    def do_set(self, line):
        """Add a set"""
        weight, reps, sets = self._parse_args(line, 3)
        if not sets:
            sets = 1
        for _ in xrange(int(sets)):
            set_ = Set(
                    order=self.current_order,
                    exercise=self.current_exercise,
                    weight=weight,
                    reps=reps,
                    workout=self.current_workout,
               )
            self.session.add(set_)
            self.current_order += 1
        self.session.commit()

    def do_delete_set(self, line):
        """Delete a set"""
        set_num = self._parse_args(line, 1)
        set_ = self.session.query(Set)\
                    .join(Workout)\
                    .filter(Workout.id == self.current_workout.id)\
                    .filter(Set.order == set_num)\
                    .scalar()
        self.session.delete(set_)
        self.session.commit()
