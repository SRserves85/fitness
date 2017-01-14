import numpy as np
from scipy.optimize import curve_fit


def fit_athlte_results(workout_time, joules_expended):
    """Takes workout results and returns coefficients for a log curve

    aargs:
        d(numpy array): workout times (seconds)
        d(numpy_array): joules expended (joules)

    returns:
        d(list): coefficients of fitted workout curve
    """
