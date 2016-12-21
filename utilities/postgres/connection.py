"""Useful place to put all of my connections for postgres
"""
import psycopg2
from sqlalchemy import create_engine
from db import DB

from env import LOCAL_PG_CRIDENTIALS

con = psycopg2.connect(user=LOCAL_PG_CRIDENTIALS['username'],
                       dbname=LOCAL_PG_CRIDENTIALS['db_name'])

engine = create_engine(
    'postgresql://{}@localhost/{}'.format(LOCAL_PG_CRIDENTIALS['username'],
                                          LOCAL_PG_CRIDENTIALS['db_name']))
db_query = DB(password=LOCAL_PG_CRIDENTIALS['password'],
              hostname=LOCAL_PG_CRIDENTIALS['hostname'],
              username=LOCAL_PG_CRIDENTIALS['username'],
              dbtype=LOCAL_PG_CRIDENTIALS['db_type'],
              dbname=LOCAL_PG_CRIDENTIALS['db_name'],
              port=LOCAL_PG_CRIDENTIALS['port'])
