"""Inserts into tables

Should only be the runner for upserting and inserting other python scripts
"""



 # Set and connect the engine
    user = LOCAL_PG_CRIDENTIALS['username']
    dbname = LOCAL_PG_CRIDENTIALS['db_name']
    engine = create_engine('postgresql://{}@localhost/{}'.format(user, dbname))
