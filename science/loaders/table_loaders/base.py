"""loading script as object
"""

from science.loaders.table_loaders.athlete_loader import _load_athletes
from science.loaders.table_loaders.workout_loader import _load_workouts
from science.loaders.table_loaders.workout_joules_loader import _load_workout_joules

from utilities.google.sheets import _pull_google_workout_data


class BaseLoader(object):
    def __init__(self):
        pass

    def _pull_data(self):
        _pull_google_workout_data()

    def _load_athletes(self):
        _load_athletes()

    def _load_workouts(self):
        _load_workouts()

    def _load_workout_joules(self):
        _load_workout_joules()
