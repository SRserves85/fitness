"""Inserts into tables

Should only be the runner for upserting and inserting other python scripts
"""
from science.loaders.table_loaders.base import BaseLoader


class perform_work(BaseLoader):
    def __init__(self):
        pass

if __name__ == '__main__':
    LOADING = perform_work()

    LOADING.pull_data()
    LOADING.load_athletes()
    LOADING.load_workouts()
    LOADING.load_workout_joules()
