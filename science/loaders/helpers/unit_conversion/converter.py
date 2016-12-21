"""Converts different units
"""


def lb_to_kg(lb_number):
    """Takes lbs and returns value in kg

    aargs:
        d(float) lb_number

    returns:
        d(float) kg_number
    """
    try:
        return 0.453592 * lb_number
    except (ValueError, TypeError):
        print "Something is really really wrong!!!"
        raise


def in_to_meter(in_number):
    """Takes in and returns value in meters

    aargs:
        d(float) in_number

    returns:
        d(float) meters_number
    """
    try:
        return 0.0254 * in_number
    except (ValueError, TypeError):
        print "Something is really really wrong!!!"
        raise(ValueError)
