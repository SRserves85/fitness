"""Inserts into tables

Should only be the runner for upserting and inserting other python scripts
"""

from science.loaders.athlete_loader import _load_athletes

if __name__ == '__main__':
    _load_athletes()
