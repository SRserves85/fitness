"""Inserts into tables

Should only be the runner for upserting and inserting other python scripts
"""
from science.loaders.table_loaders.base import BaseLoader


class perform_work(BaseLoader):
    def __init__(self):
        pass

if __name__ == '__main__':
    loading = perform_work()

    loading._pull_data()
    loading._load_athletes()
    loading._load_workouts()
    loading._load_workout_joules()
