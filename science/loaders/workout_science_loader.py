"""Pulls workouts for each athlete and models them
"""

import pandas as pd
import numpy as np
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from science.modeling.curvefit import fit_athlte_results
from science.modeling.curvefit import function

from utilities.postgres.connection import engine, db_query


def model_workouts():
    """Function to model workouts already in postgres.
    """

    print "Modeling Athlete workouts..."

    # Pull all workout data for every athlete
    workouts = db_query.query("SELECT * FROM workouts")

    # create a unique athlete list
    stats = {}
    grouped = workouts[workouts.workout_type == 'metcon'].groupby('name')
    for name, group in grouped:
        workout_times = group.workout_length_seconds.values
        workout_work = group.joules.values

        # Calculate Workout Wattage
        workout_watts = workout_work / workout_times

        # fit curve from model to get coefficients
        curve_coeffs = fit_athlte_results(workout_times, workout_watts)
        stats[name] = {}
        stats[name]['a'] = curve_coeffs[0]
        stats[name]['b'] = curve_coeffs[1]
        stats[name]['c'] = curve_coeffs[2]
    modeled = pd.DataFrame(stats).transpose()



if __name__ == '__main__':
    model_workouts()
