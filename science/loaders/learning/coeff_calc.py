import pandas as pd
import numpy as np

from utilities.postgres.connection import db_query

from science.loaders.learning.fit_curve import model_workouts

from science.modeling.curvefit import fit_athlte_results


class Correct_Workouts(object):

    def __init__(self, iterations):
        self.iterations = int(iterations)
        self.iteration = 2
        self.workout_wattage = None
        self.original_workout_joules = None

    def pull_workouts(self):
        """pull most recent workout joule calculations.
        """
        work = db_query.query(
            """
            SELECT *
            FROM workout_joules
            WHERE workout_type = 'metcon'
            """)
        df = pd.DataFrame()
        df["name"] = work.name
        df["workout_type"] = work.workout_type
        df["date"] = work.date
        df["workout_length_seconds"] = work.workout_length_seconds
        df["created_at"] = work.created_at
        df["wattage_total"] = (work.joules_total / work.workout_length_seconds)
        df["pull_up_wattage"] = (work.pull_up_joules / work.workout_length_seconds)
        df["push_up_wattage"] = (work.push_up_joules / work.workout_length_seconds)
        df["burpie_wattage"] = (work.burpie_joules / work.workout_length_seconds)
        df["double_under_wattage"] = (work.double_under_joules / work.workout_length_seconds)
        df["run_dist_meters_wattage"] = (work.run_dist_meters_joules / work.workout_length_seconds)
        df["deadlift_wattage"] = (work.deadlift_joules / work.workout_length_seconds)
        df["box_jump_wattage"] = (work.box_jump_joules / work.workout_length_seconds)
        df["air_squat_wattage"] = (work.air_squat_joules / work.workout_length_seconds)
        df["handstand_push_up_wattage"] = (work.handstand_push_up_joules / work.workout_length_seconds)
        df["wall_ball_wattage"] = (work.wall_ball_joules / work.workout_length_seconds)
        df["kettle_bell_swing_wattage"] = (work.kettle_bell_swing_joules / work.workout_length_seconds)
        df["russian_kettle_bell_swing_wattage"] = (work.russian_kettle_bell_swing_joules / work.workout_length_seconds)
        df["thruster_wattage"] = (work.thruster_joules / work.workout_length_seconds)
        df["row_dist_meters_wattage"] = (work.row_dist_meters_joules / work.workout_length_seconds)
        df["row_calories_wattage"] = (work.row_calories_joules / work.workout_length_seconds)
        df["back_squat_wattage"] = (work.back_squat_joules / work.workout_length_seconds)
        df["muscle_up_wattage"] = (work.muscle_up_joules / work.workout_length_seconds)
        df["push_press_wattage"] = (work.push_press_joules / work.workout_length_seconds)
        df["overhead_squat_wattage"] = (work.overhead_squat_joules / work.workout_length_seconds)
        df["back_extension_wattage"] = (work.back_extension_joules / work.workout_length_seconds)
        df["GHD_sit_up_wattage"] = (work.GHD_sit_up_joules / work.workout_length_seconds)
        df["press_wattage"] = (work.press_joules / work.workout_length_seconds)
        df["abmat_sit_up_wattage"] = (work.abmat_sit_up_joules / work.workout_length_seconds)
        df["front_squat_wattage"] = (work.front_squat_joules / work.workout_length_seconds)
        df["rope_climb_wattage"] = (work.rope_climb_joules / work.workout_length_seconds)
        df["ring_dip_wattage"] = (work.ring_dip_joules / work.workout_length_seconds)
        df["walking_lunge_wattage"] = (work.walking_lunge_joules / work.workout_length_seconds)
        df["knees_to_elbows_wattage"] = (work.knees_to_elbows_joules / work.workout_length_seconds)
        df["bench_press_wattage"] = (work.bench_press_joules / work.workout_length_seconds)
        df["push_jerk_wattage"] = (work.push_jerk_joules / work.workout_length_seconds)
        df["clean_wattage"] = (work.clean_joules / work.workout_length_seconds)
        df["power_clean_wattage"] = (work.power_clean_joules / work.workout_length_seconds)
        df["jerk_wattage"] = (work.jerk_joules / work.workout_length_seconds)
        df["sumo_dead_lift_wattage"] = (work.sumo_dead_lift_joules / work.workout_length_seconds)
        df["cycling_avg_watts_wattage"] = (work.cycling_avg_watts_joules / work.workout_length_seconds)
        df["snatch_wattage"] = (work.snatch_joules / work.workout_length_seconds)
        df["power_snatch_wattage"] = (work.power_snatch_joules / work.workout_length_seconds)
        self.watts = df

    def fit_curve(self):
        """fit_curve for current watts df
        """
        if self.iteration == 1:
            self.curve_coefs = model_workouts()

        elif self.iteration > 1:
            stats = {}
            workouts = self.watts
            grouped = workouts[workouts.workout_type == 'metcon'].groupby('name')
            for name, group in grouped:
                workout_times = group.workout_length_seconds.values

                # Calculate Workout Wattage
                workout_watts = group.wattage_total

                # fit curve from model to get coefficients
                curve_coeffs = fit_athlte_results(workout_times, workout_watts)
                stats[name] = {}
                stats[name]['a'] = curve_coeffs[0]
                stats[name]['b'] = curve_coeffs[1]
                stats[name]['c'] = curve_coeffs[2]
            modeled = pd.DataFrame(stats).transpose()
            self.curve_coefs = modeled

    def calc_wattage(self):

        def func(x, a, b, c):
            """Should return a standard log decline plot
            """
            return a + b*(np.log(c * x))

        df = self.watts
        cof = self.curve_coefs

        names = df.name.unique().tolist()
        for athlete in names:
            coefs = cof[cof.index == athlete].to_dict(orient='records')[0]
            df.loc[df.name == athlete, "calc_wattage"] = df.workout_length_seconds.apply(lambda x: func(x, coefs['a'], coefs['b'], coefs['c']))
        self.watts = df

    def find_movement_coeffs(self):
        

if __name__ == "__main__":
    calc = Correct_Workouts(1)
    calc.pull_workouts()
    calc.fit_curve()
    calc.calc_wattage()