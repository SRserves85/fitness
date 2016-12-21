"""Contains everything to import workout files
"""
import pandas as pd
import numpy as np
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from science.loaders.helpers.workout_cal_converters.movement_conversion_model import (pull_up_calc,
                                                                                      push_up_calc,
                                                                                      burpie_calc,
                                                                                      double_under_calc,
                                                                                      run_dist_meters_calc,
                                                                                      dead_lift_calc,
                                                                                      box_jump_calc,
                                                                                      air_squat_calc,
                                                                                      handstand_push_up_calc,
                                                                                      wall_ball_calc,
                                                                                      kettle_bell_calc,
                                                                                      russian_kettle_bell_calc,
                                                                                      thruster_calc,
                                                                                      row_distance_calc,
                                                                                      row_calories_calc,
                                                                                      back_squat_calc,
                                                                                      muscle_up_calc,
                                                                                      push_press_calc,
                                                                                      overhead_squat_calc,
                                                                                      back_extension_calc,
                                                                                      GHD_sit_up_calc,
                                                                                      press_calc,
                                                                                      sit_up_calc,
                                                                                      front_squat_calc,
                                                                                      rope_climb_calc,
                                                                                      ring_dip_calc,
                                                                                      walking_lunge_calc,
                                                                                      knees_to_elbows_calc,
                                                                                      bench_press_calc,
                                                                                      push_jerk_calc,
                                                                                      clean_calc,
                                                                                      power_clean_calc,
                                                                                      jerk_calc,
                                                                                      sumo_dead_lift_calc,
                                                                                      cycling_avg_watts_calc)
from utilities.postgres.models.workout import Workout
from utilities.postgres.connection import engine, db_query


def _load_workouts():
    # read csv
    # TODO: google-doc implimentation
    print("importing data...")
    df = pd.read_csv('data/workouts.csv').fillna(0.0)


    print("loading {} athletes...".format(len(df.name.unique())))
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # find all current athletes in DB
    athletes = db_query.query("SELECT * FROM athletes")

    # check workouts aren't from foreign Athletes
    for item in df.name.unique().tolist():
        if item not in athletes.name.unique().tolist():
            raise ValueError("unknown athlete: {}".format(item))
            break

    athlete_list = df.name.unique().tolist()

    # iterate through athletes to load data for future calculation and table
    # insertion
    for athlete in athlete_list:
        stats = athletes[athletes['name'] == athlete]

        weight = stats['weight']
        height = stats['height']
        shoulder_height = stats['shoulder_height']
        arm_length = stats['arm_length']
        leg_length = stats['leg_length']
        upper_leg_length = stats['upper_leg_length']
        lower_leg_length = stats['lower_leg_length']
        back_squat = stats['back_squat']
        front_squat = stats['front_squat']
        overhead_squat = stats['overhead_squat']
        snatch = stats['snatch']
        clean = stats['clean']
        jerk = stats['jerk']
        bench = stats['bench']
        mile_run_seconds = stats['mile_run_seconds']
        row_500_time = stats['row_500_time']

        # iterate through workouts by athlete

        for row, index in df[df['name'] == athlete].iterrows():
            try:
                name = str(athlete)
                workout_type = str(index['workout_type'])
                date = index['date']
                workout_length_seconds = int(index['workout_length_seconds'])
                created_at = datetime.datetime.now()
                pull_up_number = int(index['pull_up'])
                push_up_number = int(index['push_up'])
                burpie_number = int(index['burpie'])
                double_under_number = int(index['double_under'])
                run_dist_meters = int(index['run_dist_meters'])
                deadlift_number = int(index['deadlift'])
                deadlift_weight = int(index['deadlift_weight'])
                box_jump_number = int(index['box_jump'])
                box_jump_height = int(index['box_jump_height'])
                air_squat_number = int(index['air_squat'])
                handstand_push_up_number = int(index['handstand_push_up'])
                wall_ball_number = int(index['wall_ball'])
                wall_ball_weight = int(index['wall_ball_weight'])
                kettle_bell_swing_number = int(index['kettle_bell_swing'])
                kettle_bell_swing_weight = int(index['kettle_bell_swing_weight'])
                russian_kettle_bell_swing_number = int(index['russian_kettle_bell_swing'])
                russian_kettle_bell_swing_weight = int(index['russian_kettle_bell_swing_weight'])
                thruster_number = int(index['thruster'])
                thruster_weight = int(index['thruster_weight'])
                row_dist_meters = int(index['row_dist_meters'])
                row_calories = int(index['row_calories'])
                back_squat_number = int(index['back_squat'])
                back_squat_weight = int(index['back_squat_weight'])
                muscle_up_number = int(index['muscle_up'])
                push_press_number = int(index['push_press'])
                push_press_weight = int(index['push_press_weight'])
                overhead_squat_number = int(index['overhead_squat'])
                overhead_squat_weight = int(index['overhead_squat_weight'])
                back_extension_number = int(index['back_extension'])
                GHD_sit_up_number = int(index['GHD_sit_up'])
                press_number = int(index['press'])
                press_weight = int(index['press_weight'])
                abmat_sit_up_number = int(index['abmat_sit_up'])
                front_squat_number = int(index['front_squat'])
                front_squat_weight = int(index['front_squat_weight'])
                rope_climb_number = int(index['rope_climb'])
                ring_dip_number = int(index['ring_dip'])
                walking_lunge_number = int(index['walking_lunge'])
                knees_to_elbows_number = int(index['knees_to_elbows'])
                bench_press_number = int(index['bench_press'])
                bench_press_weight = int(index['bench_press_weight'])
                push_jerk_number = int(index['push_jerk'])
                push_jerk_weight = int(index['push_jerk_weight'])
                clean_number = int(index['clean'])
                clean_weight = int(index['clean_weight'])
                power_clean_number = int(index['power_clean'])
                power_clean_weight = int(index['power_clean_weight'])
                jerk_number = int(index['jerk'])
                jerk_weight = int(index['jerk_weight'])
                sumo_dead_lift_number = int(index['sumo_dead_lift'])
                sumo_dead_lift_weight = int(index['sumo_dead_lift_weight'])
                cycling_avg_watts = int(index['cycling_avg_watts'])
            except ValueError:
                raise
            # Calculate Calories expended in the workout:
            calories = np.array([
                pull_up_calc(weight, arm_length, pull_up_number),
                push_up_calc(weight, arm_length, push_up_number),
                burpie_calc(weight, height, burpie_number),
                double_under_calc(weight, height, double_under_number),
                run_dist_meters_calc(weight, run_dist_meters),
                dead_lift_calc(weight, shoulder_height, height, arm_length, deadlift_weight, deadlift_number),
                box_jump_calc(weight, box_jump_height, box_jump_number),
                air_squat_calc(weight, upper_leg_length, air_squat_number),
                handstand_push_up_calc(weight, height, arm_length, shoulder_height, handstand_push_up_number),
                wall_ball_calc(weight, upper_leg_length, shoulder_height, wall_ball_weight, wall_ball_number),
                kettle_bell_calc(kettle_bell_swing_weight, arm_length, kettle_bell_swing_number),
                russian_kettle_bell_calc(russian_kettle_bell_swing_weight, arm_length, russian_kettle_bell_swing_number),
                thruster_calc(weight, upper_leg_length, shoulder_height, arm_length, thruster_weight, thruster_number),
                row_distance_calc(row_500_time, row_dist_meters),
                row_calories_calc(row_calories),
                back_squat_calc(weight, upper_leg_length, back_squat_weight, back_squat_number),
                muscle_up_calc(weight, arm_length, muscle_up_number),
                push_press_calc(weight, push_press_weight, arm_length, upper_leg_length, push_press_number),
                overhead_squat_calc(weight, upper_leg_length, overhead_squat_weight, overhead_squat_number),
                back_extension_calc(weight, shoulder_height, leg_length, back_extension_number),
                GHD_sit_up_calc(weight, shoulder_height, leg_length, GHD_sit_up_number),
                press_calc(press_weight, arm_length, press_number),
                sit_up_calc(weight, shoulder_height, leg_length, abmat_sit_up_number),
                front_squat_calc(weight, upper_leg_length, front_squat_weight, front_squat_number),
                rope_climb_calc(weight, rope_climb_number),
                ring_dip_calc(weight, arm_length, ring_dip_number),
                walking_lunge_calc(weight, upper_leg_length, walking_lunge_number),
                knees_to_elbows_calc(weight, shoulder_height, leg_length, knees_to_elbows_number),
                bench_press_calc(bench_press_weight, arm_length, bench_press_number),
                push_jerk_calc(weight, push_jerk_weight, arm_length, upper_leg_length, push_jerk_number),
                clean_calc(weight, shoulder_height, height, arm_length, clean_weight, upper_leg_length, clean_number),
                power_clean_calc(weight, shoulder_height, height, arm_length, power_clean_weight, upper_leg_length, power_clean_number),
                jerk_calc(weight, jerk_weight, arm_length, upper_leg_length, jerk_number),
                sumo_dead_lift_calc(weight, shoulder_height, height, arm_length, sumo_dead_lift_weight, sumo_dead_lift_number),
                cycling_avg_watts_calc(cycling_avg_watts)
            ])
            import pdb; pdb.set_trace()

if __name__ == '__main__':
    _load_workouts()
