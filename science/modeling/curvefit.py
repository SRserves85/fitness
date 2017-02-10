import numpy as np
from scipy.optimize import curve_fit


def fit_athlte_results(workout_time, wattage):
    """Takes workout results and returns coefficients for a log curve

    aargs:
        d(numpy.array): workout times (seconds)
        d(numpy.array): workout wattage (joules)

    returns:
        d(list): coefficients of fitted workout curve
    """

    def function(x, a, b, c):
        """Should return a standard log decline plot
        """
        return a + b * (np.log(np.abs(c) * x))
    xdata = workout_time
    ydata = wattage
    popt, pcov = curve_fit(function, xdata, ydata)
    return popt


# for importing
def function(x, a, b, c):
    """Should return a standard log decline plot
    """
    return a + b * (np.log(np.abs(c) * x))
