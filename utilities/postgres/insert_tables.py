"""creates tables for athletes
"""
from sqlalchemy import create_engine

from env import LOCAL_PG_CRIDENTIALS
from utilities.postgres import Base
from utilities.postgres.models.athletes import Athlete
from utilities.postgres.models.workout import Workout
from utilities.postgres.models.workout_joules import Workout_Joules


def insert_tables():

    # Set and connect the engine
    user = LOCAL_PG_CRIDENTIALS['username']
    dbname = LOCAL_PG_CRIDENTIALS['db_name']
    engine = create_engine('postgresql://{}@localhost/{}'.format(user, dbname))

    # place the tables in postgres
    Base.metadata.create_all(engine)
if __name__ == "__main__":
    insert_tables()
