import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

from scipy.optimize import fmin_slsqp


def get_coeffs(X, y):
    """Calculates workout coefficients for each movement

    Aargs:
        d(numpy.array) X workout wattages
        d(numpy.array) y total workout expected wattage

    Returns:
        d(pandas.DataFrame) workout coefficients
    """

    lr = LinearRegression()
    lr.fit(X, y)
    return lr.coef_

def get_specific_coeffs(X, y):
