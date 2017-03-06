"""Useful place to put all of my connections for postgres
"""
import psycopg2
from sqlalchemy import create_engine
from db import DB

from env import LOCAL_PG_CREDENTIALS

con = psycopg2.connect(user=LOCAL_PG_CREDENTIALS['username'],
                       dbname=LOCAL_PG_CREDENTIALS['db_name'])

engine = create_engine(
    'postgresql://{}@localhost/{}'.format(LOCAL_PG_CREDENTIALS['username'],
                                          LOCAL_PG_CREDENTIALS['db_name']))
db_query = DB(password=LOCAL_PG_CREDENTIALS['password'],
              hostname=LOCAL_PG_CREDENTIALS['hostname'],
              username=LOCAL_PG_CREDENTIALS['username'],
              dbtype=LOCAL_PG_CREDENTIALS['db_type'],
              dbname=LOCAL_PG_CREDENTIALS['db_name'],
              port=LOCAL_PG_CREDENTIALS['port'])
