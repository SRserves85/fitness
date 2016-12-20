"""Converts different units
"""


def lb_to_kg(lb_number):
    """Takes lbs and returns value in kg 

    aargs:
        d(float) lb_number

    returns:
        d(float) kg_number
    """
    if isinstance(lb_number, float):
        return 0.453592 * lb_number
    else:
        print "Something is really really wrong!!!"
        raise(ValueError)


def in_to_meter(in_number):
    """Takes in and returns value in meters

    aargs:
        d(float) in_number

    returns:
        d(float) meters_number
    """
    if isinstance(in_number, float):
        return 0.0254 * in_number
    else:
        print "Something is really really wrong!!!"
        raise(ValueError)
