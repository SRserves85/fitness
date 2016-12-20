"""Workouts Model for Postgresql

Should include relevent workout data
"""

from sqlalchemy import Column, String, DateTime, Integer, Float
from utilities.postgres import Base


class Workout(Base):

    __tablename__ = 'workouts'

    __table_args__ = {'extend_existing': True}

    name = Column(String(), nullable=False, primary_key=True)
    workout_type = Column(String(), nullable=False, primary_key=True)
    date = Column(DateTime(), nullable=False, primary_key=True)
    workout_length_seconds = Column(Integer(), nullable=False, primary_key=True)
    created_at = Column(DateTime())
    wattage = Column(Float())
    pull_up = Column(Integer())
    push_up = Column(Integer())
    burpie = Column(Integer())
    double_under = Column(Integer())
    run_dist_meters = Column(Integer())
    deadlift = Column(Integer())
    deadlift_weight = Column(Integer())
    box_jump = Column(Integer())
    air_squat = Column(Integer())
    handstand_push_up = Column(Integer())
    wall_ball = Column(Integer())
    well_ball_weight = Column(Integer())
    kettle_bell_swing = Column(Integer())
    kettle_bell_swing_weight = Column(Integer())
    russian_kettle_bell_swing = Column(Integer())
    russian_kettle_bell_swing_weight = Column(Integer())
    thruster = Column(Integer())
    thruster_weight = Column(Integer())
    row_dist_meters = Column(Integer())
    row_calories = Column(Integer())
    back_squat = Column(Integer())
    back_squat_weight = Column(Integer())
    muscle_up = Column(Integer())
    push_press = Column(Integer())
    push_press_weight = Column(Integer())
    overhead_squat = Column(Integer())
    overhead_squat_weight = Column(Integer())
    back_extension = Column(Integer())
    GHD_sit_up = Column(Integer())
    press = Column(Integer())
    press_weight = Column(Integer())
    abmat_sit_up = Column(Integer())
    front_squat = Column(Integer())
    front_squat_weight = Column(Integer())
    rope_climb = Column(Integer())
    ring_dip = Column(Integer())
    walking_lunge = Column(Integer())
    knees_to_elbows = Column(Integer())
    bench_press = Column(Integer())
    bench_press_weight = Column(Integer())
    push_jerk = Column(Integer())
    push_jerk_weight = Column(Integer())
    clean = Column(Integer())
    clean_weight = Column(Integer())
    power_clean = Column(Integer())
    power_clean_weight = Column(Integer())
    jerk = Column(Integer())
    jerk_weight = Column(Integer())
    sumo_dead_lift = Column(Integer())
    sumo_dead_lift_weight = Column(Integer())
    cycling_avg_watts = Column(Integer())
