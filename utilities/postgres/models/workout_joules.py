"""Workouts work Model for Postgresql

Should include relevent workout data
"""

from sqlalchemy import Column, String, DateTime, Integer, Float
from utilities.postgres import Base

class Workout_Joules(Base):

    __tablename__ = 'workout_joules'

    __table_args__ = {'extend_existing': True}

    name = Column(String(), nullable=False, primary_key=True)
    workout_type = Column(String(), nullable=False, primary_key=True)
    date = Column(DateTime(), nullable=False, primary_key=True)
    workout_length_seconds = Column(Integer(), nullable=False, primary_key=True)
    created_at = Column(DateTime(), nullable=False, primary_key=True)
    joules_total = Column(Float(), nullable=False)
    pull_up_joules = Column(Integer())
    push_up_joules = Column(Integer())
    burpie_joules = Column(Integer())
    double_under_joules = Column(Integer())
    run_dist_meters_joules = Column(Integer())
    deadlift_joules = Column(Integer())
    box_jump_joules = Column(Integer())
    air_squat_joules = Column(Integer())
    handstand_push_up_joules = Column(Integer())
    wall_ball_joules = Column(Integer())
    kettle_bell_swing_joules = Column(Integer())
    russian_kettle_bell_swing_joules = Column(Integer())
    thruster_joules = Column(Integer())
    row_dist_meters_joules = Column(Integer())
    row_calories_joules = Column(Integer())
    back_squat_joules = Column(Integer())
    muscle_up_joules = Column(Integer())
    push_press_joules = Column(Integer())
    overhead_squat_joules = Column(Integer())
    back_extension_joules = Column(Integer())
    GHD_sit_up_joules = Column(Integer())
    press_joules = Column(Integer())
    abmat_sit_up_joules = Column(Integer())
    front_squat_joules = Column(Integer())
    rope_climb_joules = Column(Integer())
    ring_dip_joules = Column(Integer())
    walking_lunge_joules = Column(Integer())
    knees_to_elbows_joules = Column(Integer())
    bench_press_joules = Column(Integer())
    push_jerk_joules = Column(Integer())
    clean_joules = Column(Integer())
    power_clean_joules = Column(Integer())
    jerk_joules = Column(Integer())
    sumo_dead_lift_joules = Column(Integer())
    cycling_avg_watts_joules = Column(Integer())
