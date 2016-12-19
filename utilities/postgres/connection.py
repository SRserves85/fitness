"""Useful place to put all of my connections for postgres
"""
import psycopg2
from sqlalchemy import create_engine

from env import LOCAL_PG_CRIDENTIALS

con = psycopg2.connect(user=LOCAL_PG_CRIDENTIALS['username'],
                       dbname=LOCAL_PG_CRIDENTIALS['db_name'])

engine = create_engine(
    'postgresql://{}@localhost/{}'.format(LOCAL_PG_CRIDENTIALS['username'],
                                          LOCAL_PG_CRIDENTIALS['db_name']))
