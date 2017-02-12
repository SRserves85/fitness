"""movement converters to Joules of energy

Needs athlete information to calculate anything

For most movements, Basic Formaula will be:
work (joules) = mass * gravity * height * number_reps
"""

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
    bar_lift = lb_to_kg(dead_lift_weight) * 9.80665 * dis * number
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
    """Takes weight, upper_leg_length number and returns joules.

    movement length: upper_leg_length
    mass = 0.66 of body mass

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number


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


def wall_ball_calc(weight, upper_leg_length, shoulder_height, wall_ball_weight, number):
    """Takes weight, upper_leg_length, well_ball_weight, number and returns joules

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) shoulder_height
        d(int) wall_ball_weight
        d(int) number

    returns:
        d(float) joules
    """
    squat = lb_to_kg(weight + wall_ball_weight) * 0.88 * 9.80665 * in_to_meter(upper_leg_length) * number
    wall_ball = lb_to_kg(wall_ball_weight) * 9.80665 * in_to_meter(120 - shoulder_height) * number
    return squat + wall_ball


def kettle_bell_calc(kettle_bell_weight, arm_length, number):
    """Takes kettle_bell_weight, arm_length, number and returns joules.

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(kettle_bell_weight) * 9.80665 * in_to_meter(arm_length * 2) * number


def russian_kettle_bell_calc(kettle_bell_weight, arm_length, number):
    """Takes kettle_bell_weight, arm_length, number and returns joules.

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(kettle_bell_weight) * 9.80665 * in_to_meter(arm_length) * number


def thruster_calc(weight, upper_leg_length, shoulder_height, arm_length, thruster_weight, number):
    """Takes kettle_bell_weight, armlength, number and returns joules.

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    air_squat = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    weight_squat = lb_to_kg(thruster_weight) * 9.80665 * in_to_meter(upper_leg_length) * number
    press = lb_to_kg(thruster_weight) * 9.80665 * in_to_meter(arm_length) * number
    return air_squat + weight_squat + press


def row_distance_calc(row_500_time_sec, distance):
    """ takes weight, row_time, distance returns joules

    Assumes you are rowing at 80% your 500 meter pace.
    Couldn't think of a better way to do this to take into account better rowers.

    see below for concept 2 calculation:
    http://www.concept2.com/indoor-rowers/training/calculators/calorie-calculator

    aargs:
        d(int) row_500_time_sec
        d(int) distance

    returns:
        d(float) joules
    """
    adjusted_500_time = row_500_time_sec * 1.2
    pace = adjusted_500_time / 500
    time = distance / pace
    wattage = (2.8 / pace)  # Joules/second
    return wattage * time  # joules


def row_calories_calc(row_calories):
    """takes row_calories returns joules

    Need conversion to actual work done, not metabolic calorie as reported by
    concept2

    aargs:
        d(int): row_calories

    returns:
        d(float): joules
    """
    return row_calories * 2092


def back_squat_calc(weight, upper_leg_length, back_squat_weight, number):
    """Takes weight, upper_leg_length, back_squat_weight, number and return joules

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) back_squat_weight
        d(int) number

    returns:
        d(float) joules
    """
    body = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    weight = lb_to_kg(back_squat_weight) * 9.80665 * in_to_meter(upper_leg_length) * number
    return body + weight


def muscle_up_calc(weight, arm_length, number):
    """Takes weight, armlength, number and returns joules.

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(arm_length * 2) * number


def push_press_calc(weight, push_press_weight, arm_length, upper_leg_length, number):
    """Takes push_press_weight, arm_length, number and returns joules.

    assumes a 0.5 upper_leg_length dip for drive

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    dip_length = upper_leg_length / 2

    dip_drive = lb_to_kg(push_press_weight) * 9.80665 * in_to_meter(dip_length) * number
    dip_drive_weight = lb_to_kg(weight) * 9.80665 * in_to_meter(dip_length) * number
    press_weight = lb_to_kg(push_press_weight) * 9.80665 * in_to_meter(arm_length) * number
    return dip_drive + dip_drive_weight + press_weight


def overhead_squat_calc(weight, upper_leg_length, overhead_squat_weight, number):
    """Takes weight, upper_leg_length, back_squat_weight, number and return joules

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) back_squat_weight
        d(int) number

    returns:
        d(float) joules
    """
    body = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    weight = lb_to_kg(overhead_squat_weight) * 9.80665 * in_to_meter(upper_leg_length) * number
    return body + weight


def back_extension_calc(weight, shoulder_height, leg_length, number):
    """Takes weight, shoulder_height, leg_length and returns joules

    assumes body weight is 0.75 of total weight
    assumes height of lift is torso length

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) leg_length
        d(int) number

    returns:
        d(float) joules
    """
    ext_weight = lb_to_kg(weight * 0.75)
    length = shoulder_height - leg_length
    return lb_to_kg(ext_weight) * 9.80665 * in_to_meter(length) * number


def GHD_sit_up_calc(weight, shoulder_height, leg_length, number):
    """Takes weight, shoulder_height, leg_length and returns joules

    assumes body weight is 0.75 of total weight
    assumes height of lift is torso length
    uses a 1.5 multiplyer for output joules to correct for extra motion

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) leg_length
        d(int) number

    returns:
        d(float) joules
    """
    ext_weight = lb_to_kg(weight * 0.75)
    length = shoulder_height - leg_length
    return lb_to_kg(ext_weight) * 9.80665 * in_to_meter(length) * number * 1.5


def press_calc(press_weight, arm_length, number):
    """Takes press_weight, arm_length, number and returns joules.

    aargs:
        d(float) press_weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(press_weight) * 9.80665 * in_to_meter(arm_length) * number


def sit_up_calc(weight, shoulder_height, leg_length, number):
    """Takes weight, shoulder_height, leg_length and returns joules

    assumes body weight is 0.75 of total weight
    assumes height of lift is torso length

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) leg_length
        d(int) number

    returns:
        d(float) joules
    """
    ext_weight = lb_to_kg(weight * 0.75)
    length = shoulder_height - leg_length
    return lb_to_kg(ext_weight) * 9.80665 * in_to_meter(length) * number


def front_squat_calc(weight, upper_leg_length, front_squat_weight, number):
    """Takes weight, upper_leg_length, back_squat_weight, number and return joules

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) back_squat_weight
        d(int) number

    returns:
        d(float) joules
    """
    body = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    weight = lb_to_kg(front_squat_weight) * 9.80665 * in_to_meter(upper_leg_length) * number
    return body + weight


def rope_climb_calc(weight, number):
    """Takes weight, number and returns joules.

    hardcoded for 12 foot rope

    aargs:
        d(float) weight
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(144) * number


def ring_dip_calc(weight, arm_length, number):
    """Takes weight, arm_length, number and returns joules.

    aargs:
        d(float) weight
        d(int) arm_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 9.80665 * in_to_meter(arm_length) * number


def walking_lunge_calc(weight, upper_leg_length, number):
    """Takes weight, upper_leg_length, number and returns joules.

    calculated similar to squats

    multiplied by 2: 1 rep = 2 lunges

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(weight) * 0.75 * 9.80665 * in_to_meter(upper_leg_length) * number * 2


def knees_to_elbows_calc(weight, shoulder_height, leg_length, number):
    """Takes weight, shoulder_height, leg_length, number and returns joules

    same calculation as sit_ups (no real good way to do this)

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) leg_length
        d(int) number

    returns:
        d(float) joules
    """
    ext_weight = lb_to_kg(weight * 0.75)
    length = shoulder_height - leg_length
    return lb_to_kg(ext_weight) * 9.80665 * in_to_meter(length) * number


def bench_press_calc(bench_press_weight, arm_length, number):
    """Takes bench_press_weight, arm_length, number and returns joules.

    For Pushups, 60% of body mass is used ()

    aargs:
        d(float) bench_press_weight
        d(int) arm_length
        d(int) number

    returns:
        d(float) joules
    """
    return lb_to_kg(bench_press_weight) * 9.80665 * in_to_meter(arm_length) * number


def push_jerk_calc(weight, push_press_weight, arm_length, upper_leg_length, number):
    """weight, push_press_weight, arm_length, upper_leg_length, number and returns joules.

    assumes a 0.5 upper_leg_length dip for drive
    finishes lift as 1/4 squat calc

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    dip_length = upper_leg_length / 4

    dip_drive = lb_to_kg(push_press_weight) * 9.80665 * in_to_meter(dip_length) * number
    dip_drive_weight = lb_to_kg(weight) * 9.80665 * in_to_meter(dip_length) * number
    press_weight = lb_to_kg(push_press_weight) * 9.80665 * in_to_meter(arm_length) * number
    return dip_drive + dip_drive_weight + press_weight


def clean_calc(weight, shoulder_height, height, arm_length, clean_weight, upper_leg_length, number):
    """Takes weight, shoulder_height, height, arm_length, clean_weight, number and returns joules

    starts as dead_lift_calc
    adds front squat calcs to work performed

    For dead_lift, 0.225 meters is the starting location height of the bar
    ending location = shoulder_height - arm_length

    Body Center of mass is 0.66 for a standing person

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) height
        d(int) arm_length
        d(int) clean_weight
        d(int) number

    returns:
        d(float) joules
    """

    dis = (in_to_meter(shoulder_height) - in_to_meter(arm_length)) - 0.225

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(clean_weight) * 9.80665 * dis * number
    air_squat = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    weight_squat = lb_to_kg(clean_weight) * 9.80665 * in_to_meter(upper_leg_length) * number
    return body_lift + bar_lift + air_squat + weight_squat


def power_clean_calc(weight, shoulder_height, height, arm_length, power_clean_weight, upper_leg_length, number):
    """Takes weight, shoulder_height, height, arm_length, power_clean_weight, number and returns joules

    starts as dead_lift_calc
    adds front squat calcs to work performed

    For dead_lift, 0.225 meters is the starting location height of the bar
    ending location = shoulder_height - arm_length

    uses a 0.8 multiplied factor for the finish

    Body Center of mass is 0.66 for a standing person

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) height
        d(int) arm_length
        d(int) power_clean_weight
        d(int) number

    returns:
        d(float) joules
    """

    dis = (in_to_meter(shoulder_height) - in_to_meter(arm_length)) - 0.225

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(power_clean_weight) * 9.80665 * dis * number
    air_squat = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number * 0.8
    weight_squat = lb_to_kg(power_clean_weight) * 9.80665 * in_to_meter(upper_leg_length) * number * 0.8
    return body_lift + bar_lift + air_squat + weight_squat


def jerk_calc(weight, jerk_weight, arm_length, upper_leg_length, number):
    """Takes weight jerk_weight, arm_length, number and returns joules.

    assumes a 0.4 upper_leg_length dip for drive

    aargs:
        d(float) weight
        d(int) jerk_weight
        d(int) arm_length
        d(int) upper_leg_length
        d(int) number

    returns:
        d(float) joules
    """
    dip_length = upper_leg_length / 4

    dip_drive = lb_to_kg(jerk_weight) * 9.80665 * in_to_meter(dip_length) * number
    dip_drive_weight = lb_to_kg(weight) * 9.80665 * in_to_meter(dip_length) * number
    press_weight = lb_to_kg(jerk_weight) * 9.80665 * in_to_meter(arm_length) * number
    return dip_drive + dip_drive_weight + press_weight


def sumo_dead_lift_calc(weight, shoulder_height, height, arm_length, sumo_dead_lift_weight, number):
    """Takes weight, shoulder_height, arm_length, and number and returns joules

    For sumo_dead_lift, 0.225 meters is the starting location height of the bar
    ending location = shoulder_height - arm_length

    Body Center of mass is 0.66 for a standing person

    aargs:
        d(float) weight
        d(int) shoulder_height
        d(int) height
        d(int) arm_length
        d(int) sumo_dead_lift_weight
        d(int) number

    returns:
        d(float) joules
    """

    dis = (in_to_meter(shoulder_height) - in_to_meter(arm_length)) - 0.225

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(sumo_dead_lift_weight) * 9.80665 * dis * number
    return body_lift + bar_lift


def cycling_avg_watts_calc(cycling_avg_watts):
    """
    This is a special case just for cyclists.
    """
    return cycling_avg_watts


def snatch_calc(weight, upper_leg_length, height, arm_length, snatch_weight, number):
    """takes weight, upper_leg_length, height, arm_length, snatch_weight, number and returns joules.

    Assumes squat snatch is performed.
    Similar calculation to clean only more height

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) height
        d(int) arm_length
        d(int) snatch_weight
        d(int) number

    returns:
        d(float) joules
    """

    total_dis = in_to_meter(height) + in_to_meter(arm_length)
    catch_dis = total_dis - in_to_meter(upper_leg_length)

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(snatch_weight) * 9.80665 * catch_dis * number
    air_squat = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length) * number
    overhead_squat = lb_to_kg(snatch_weight) * 9.80665 * in_to_meter(upper_leg_length) * number

    return body_lift + bar_lift + air_squat + overhead_squat


def power_snatch_calc(weight, upper_leg_length, height, arm_length, snatch_weight, number):
    """takes weight, upper_leg_length, height, arm_length, snatch_weight, number and returns joules.

    Assumes squat snatch is performed.
    Similar calculation to snatch, but assumed half leg length for high catch

    aargs:
        d(float) weight
        d(int) upper_leg_length
        d(int) height
        d(int) arm_length
        d(int) snatch_weight
        d(int) number

    returns:
        d(float) joules
    """

    total_dis = in_to_meter(height) + in_to_meter(arm_length)
    catch_dis = total_dis - in_to_meter(upper_leg_length)

    body_lift = lb_to_kg(weight) * 9.80665 * (in_to_meter(height) - 0.225) * 0.66 * number
    bar_lift = lb_to_kg(snatch_weight) * 9.80665 * catch_dis * number
    air_squat = lb_to_kg(weight) * 0.85 * 9.80665 * in_to_meter(upper_leg_length / 2) * number
    overhead_squat = lb_to_kg(snatch_weight) * 9.80665 * in_to_meter(upper_leg_length / 2) * number

    return body_lift + bar_lift + air_squat + overhead_squat
