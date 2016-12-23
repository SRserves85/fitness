"""Inserts into tables

Should only be the runner for upserting and inserting other python scripts
"""

from science.loaders.table_loaders.athlete_loader import _load_athletes
from science.loaders.table_loaders.workout_loader import _load_workouts

if __name__ == '__main__':
    _load_athletes()
    _load_workouts()
