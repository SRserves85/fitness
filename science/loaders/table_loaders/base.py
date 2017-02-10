"""loading script as object
"""

from science.loaders.table_loaders.athlete_loader import load_athletes
from science.loaders.table_loaders.workout_loader import load_workouts
from science.loaders.table_loaders.workout_joules_loader import load_workout_joules

from utilities.google.sheets import pull_google_workout_data


class BaseLoader(object):
    """ Base class to load data. After testing future classes, put working
        methods here
    """
    def __init__(self):
        pass

    def pull_data(self):
        pull_google_workout_data()

    def load_athletes(self):
        load_athletes()

    def load_workouts(self):
        load_workouts()

    def load_workout_joules(self):
        load_workout_joules()
