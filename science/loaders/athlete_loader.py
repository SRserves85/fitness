"""Contains everything to import athlete files
"""
import pandas as pd
import datetime

from fish import ProgressFish
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from utilities.postgres.models.athletes import Athlete
from utilities.postgres.connection import engine

def _load_athletes():
    # read csv
    # TODO: set google-doc implimentation
    df = pd.read_csv('data/athlete.csv')

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # current implimentation means all information must be included
    for row, index in df.iterrows():
        try:
            insert = Athlete(
                    name=str(index['name']),
                    created_at=datetime.datetime.now(),
                    weight=float(index['weight']),
                    height=int(index['height']),
                    shoulder_height = int(index['shoulder_height']),
                    arm_length =int(index['arm_length']),
                    leg_length=int(index['leg_length']),
                    upper_leg_length=int(index['upper_leg_length']),
                    lower_leg_length=int(index['lower_leg_length']),
                    back_squat=int(index['back_squat']),
                    front_squat=int(index['front_squat']),
                    overhead_squat=int(index['overhead_squat']),
                    snatch=int(index['snatch']),
                    clean=int(index['clean']),
                    jerk=int(index['jerk']),
                    bench=int(index['bench']),
                    mile_run_seconds = int(index['mile_run_seconds']))
        except(ValueError, TypeError):
            raise("please fill out the form correctly!")
        try:
            session.add(insert)
            session.flush()
        except IntegrityError:
            session.rollback()
    session.commit()
