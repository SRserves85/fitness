"""movement converters to Joules of energy

Needs athlete information to calculate anything

For most movements, Basic Formaula will be:
work (joules) = mass * gravity * height * number_reps
"""
import numpy as np

from science.loaders.helpers.unit_conversion.converter import (lb_to_kg,
                                                               in_to_meter)


def pull_up_calc(weight, arm_length, number):
    """Takes weight, arm_length, number and returns joules.

    aargs:
        d(float) weight
        d(int) arm_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(arm_length) * number


def push_up_calc(weight, arm_length, number):
    """Takes weight, arm_length, number and returns joules.

    For Pushups, 60% of body mass is used ()

    aargs:
        d(float) weight
        d(int) arm_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 0.60 * 9.80665 * in_to_meter(arm_length) * number


def burpie_calc(weight, height, number):
    """Takes weight, arm_length, number and returns joules.

    For burpies, 66% of height is used for center of gravity of a typical
    standing person.

    aargs:
        d(float) weight
        d(int) height
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(height) * 0.66 * number


def double_under_calc(weight, height, number):
    """Takes weight, number and returns joules.

    Average jump height is assumed to be 7in in according to crossfit HQ

    Jump rope weight is assumed to be 0.5 lb

    aargs:
        d(float) weight
        d(int) number

    returns:
        d(float) joules
    """
    jumping = lb_to_kg(weight) * 9.80665 * in_to_meter(7) * number
    swinging = lb_to_kg(0.5) * 9.80665 * in_to_meter(height) * number * 2
    return jumping + swinging


def run_dist_meters_calc(weight, distance):
    """Takes weight, arm_length, number and returns joules.
    see:
    http://www.runnersworld.com/weight-loss/how-many-calories-are-you-really-burning

    According to The US Health And Safety Journal, Mean Calories is equal to:
    0.63 * weight per mile

    This will have a 1 as an efficiency factor

    aargs:
        d(float) weight
        d(int) distance

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 0.63 * 4184 * (distance / 1609.34)


def dead_lift_calc(weight, shoulder_height, height, arm_length, dead_lift_weight, number):
    """Takes weight, shoulder_height, arm_length, and number and returns joules

    For dead_lift, 0.225 meters is the starting location height of the bar
    ending location = shoulder_height - arm_length

    Body Center of mass is 0.66 for a standing person

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) height
        d(int) arm_length
        d(int) dead_lift_weight
        d(int) number

    returns:
        d(float) joules
    """

    dis = (in_to_meter(shoulder_height) - in_to_meter(arm_length)) - 0.225

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(dead_lift_weight) * 9.80665 * dis
    return body_lift + bar_lift


def box_jump_calc(weight, box_jump_height, number):
    """Takes weight, box_jump_height, number and returns joules.

    This will have a 1 as an efficiency factor

    aargs:
        d(float) weight
        d(int) box_jump_height
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(box_jump_height) * number


def air_squat_calc(weight, upper_leg_length, number):
    """Takes weight, upper_leg_lengthm number and returns joules.

    movement length: upper_let_length
    mass = 0.66 of body mass

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 0.66 * 9.80665 * in_to_meter(upper_leg_length) * number


def handstand_push_up_calc(weight, height, arm_length, shoulder_height, number):
    """Takes weight, height, arm_length, shoulder_height number and returns
    joules.

    aargs:
        d(float) weight
        d(int) height
        d(int) arm_length
        d(int) shoulder_height
        d(int) number

    returns:
        d(float) joules
    """
    length = in_to_meter(arm_length) - (in_to_meter(height) - in_to_meter(shoulder_height))
    return lb_to_kg(weight) * 9.80665 * length * number
