"""Athlete Model for Postgresql

Should include relevent athlete data
"""

from sqlalchemy import Column, String, DateTime, Float, Integer
from utilities.postgres import Base


class Athlete(Base):
    __tablename__ = 'athletes'

    name = Column(String(), nullable=False, primary_key=True)
    created_at = Column(DateTime(), nullable=False)
    weight = Column(Float())
    height = Column(Integer(), primary_key=True)
    shoulder_height = Column(Integer())
    arm_length = Column(Integer())
    leg_length = Column(Integer())
    upper_leg_length = Column(Integer())
    lower_leg_length = Column(Integer())
    back_squat = Column(Integer())
    front_squat = Column(Integer())
    overhead_squat = Column(Integer())
    snatch = Column(Integer())
    clean = Column(Integer())
    jerk = Column(Integer())
    bench = Column(Integer())
    mile_run_seconds = Column(Integer())
    row_500_time = Column(Integer())
