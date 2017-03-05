import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm

from utilities.postgres.connection import db_query

from science.loaders.learning.fit_curve import model_workouts
from science.loaders.helpers.movements import movements

from science.modeling.curvefit import fit_athlte_results


class Correct_Workouts(object):

    def __init__(self, iterations):
        self.iterations = int(iterations)
        self.iteration = 2
        self.workout_wattage = None
        self.original_workout_joules = None
        self.movements = [
            "pull_up",
            "push_up",
            "burpie",
            "double_under",
            "run_dist_meters",
            "deadlift",
            "box_jump",
            "air_squat",
            "handstand_push_up",
            "wall_ball",
            "kettle_bell_swing",
            "russian_kettle_bell_swing",
            "thruster",
            "row_dist_meters",
            "row_calories",
            "back_squat",
            "muscle_up",
            "push_press",
            "overhead_squat",
            "back_extension",
            "GHD_sit_up",
            "press",
            "abmat_sit_up",
            "front_squat",
            "rope_climb",
            "ring_dip",
            "walking_lunge",
            "knees_to_elbows",
            "bench_press",
            "push_jerk",
            "clean",
            "power_clean",
            "jerk",
            "sumo_dead_lift",
            "cycling_avg_watts",
            "snatch",
            "power_snatch"
        ]
        self.movement_coeffs = {}

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

        for name, group in df.groupby('name'):
            self.movement_coeffs[name] = {'pull_up_wattage': 1,
                                          'push_up_wattage': 1,
                                          'burpie_wattage': 1,
                                          'double_under_wattage': 1,
                                          'run_dist_meters_wattage': 1,
                                          'deadlift_wattage': 1,
                                          'box_jump_wattage': 1,
                                          'air_squat_wattage': 1,
                                          'handstand_push_up_wattage': 1,
                                          'wall_ball_wattage': 1,
                                          'kettle_bell_swing_wattage': 1,
                                          'russian_kettle_bell_swing_wattage': 1,
                                          'thruster_wattage': 1,
                                          'row_dist_meters_wattage': 1,
                                          'row_calories_wattage': 1,
                                          'back_squat_wattage': 1,
                                          'muscle_up_wattage': 1,
                                          'push_press_wattage': 1,
                                          'overhead_squat_wattage': 1,
                                          'back_extension_wattage': 1,
                                          'GHD_sit_up_wattage': 1,
                                          'press_wattage': 1,
                                          'abmat_sit_up_wattage': 1,
                                          'front_squat_wattage': 1,
                                          'rope_climb_wattage': 1,
                                          'ring_dip_wattage': 1,
                                          'walking_lunge_wattage': 1,
                                          'knees_to_elbows_wattage': 1,
                                          'bench_press_wattage': 1,
                                          'push_jerk_wattage': 1,
                                          'clean_wattage': 1,
                                          'power_clean_wattage': 1,
                                          'jerk_wattage': 1,
                                          'sumo_dead_lift_wattage': 1,
                                          'cycling_avg_watts_wattage': 1,
                                          'snatch_wattage': 1,
                                          'power_snatch_wattage': 1,
                                          'calc_wattage': 1}

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
                group.sort_values(by='workout_length_seconds', inplace=True)
                workout_times = group.workout_length_seconds.values

                # Calculate Workout Wattage
                workout_watts = group.wattage_total

                plt.scatter(workout_times, workout_watts)
                plt.title(name)

                # fit curve from model to get coefficients
                curve_coeffs = fit_athlte_results(workout_times, workout_watts)
                stats[name] = {}
                stats[name]['a'] = curve_coeffs[0]
                stats[name]['b'] = curve_coeffs[1]
                stats[name]['c'] = curve_coeffs[2]
                x = np.linspace(1, workout_times.max())
                plt.plot(x, (curve_coeffs[0] + curve_coeffs[1] * (np.log(np.abs(curve_coeffs[2]) * x))))
                plt.show()
            modeled = pd.DataFrame(stats).transpose()
            self.curve_coefs = modeled

    def calc_wattage(self):

        def func(x, a, b, c):
            """Should return a standard log decline plot
            """
            return a + b * (np.log(c + x))

        df = self.watts
        cof = self.curve_coefs

        names = df.name.unique().tolist()
        for athlete in names:
            coefs = cof[cof.index == athlete].to_dict(orient='records')[0]
            df.loc[df.name == athlete, "calc_wattage"] = df.workout_length_seconds.apply(lambda x: func(x, coefs['a'], coefs['b'], coefs['c']))
        self.watts = df

    def find_movement_coeffs(self):

        def shorten(df):
            """ Takes dataframe and returns only the data without zeros

            Aargs:
                d(pandas.dataframe) df

            Returns:
                d(pandas.dataframe) dataframe without columns with all zeros
            """
            mov = []
            for move in calc.movements:
                mov.append(move + "_wattage")
            mov.append('calc_wattage')

            d = df[mov]
            for m in mov:
                if d[m].sum() <= 0:
                    d.drop(m, axis=1, inplace=True)
            return d

        def prepare(df):
            """ Takes pandas dataframe and returns X and y vectors for linear
                model

            Aargs:
                d(pandas.dataframe) df

            Returns:
                d(numpy.array): X, values for exog in model
                d(numpu.array): y, values in endog in model
            """
            y = df.calc_wattage
            movs = [x for x in shorten(group).columns.tolist() if x != "calc_wattage"]
            X = df[movs]
            return X, y

        df = self.watts
        for name, group in df.groupby('name'):
            import pdb; pdb.set_trace()
            X, y = prepare(group)
            X = sm.add_constant(X)
            params = sm.OLS(y, X).fit().params.to_dict()
            del params['const']

            for move in params.keys():

                self.movement_coeffs[name][move] = self.movement_coeffs[name][move] * params[move]

    def calculate_new_wattages(self):

        if self.iteration == self.iterations:
            df = self.watts
        else:
            df = self.calc_watts

        # pull workouts from coefficient data
        for athlete in self.workout_coeffs:

            # multiply current watts by coefficients for each athlete
            for movement in self.workout_coeffs[athlete].keys():
                df.loc[df.name == athlete, movement] = df[movement] * self.workout_coeffs[athlete][movement]
        df.wattage_total = df[self.workout_coeffs[athlete].keys()].sum(axis=1)
        self.calc_watts = df

    def calc_error(self):
        error = np.sum(np.square(self.calc_watts.wattage_total - self.calc_watts.calc_wattage))

        if self.iteration == self.iterations:
            self.error = error
        else:
            if self.error < error:
                pass
            self.error = error

    def _model_workouts(self):

        self.iteration = self.iterations
        self.pull_workouts()
        while self.iteration > 0:
            self.fit_curve()
            self.calc_wattage()
            self.find_movement_coeffs()
            self.calculate_new_wattages()
            self.calc_error()
            self.iteration = self.iteration - 1
            print "iteration {}: error = {}".format(self.iteration, self.error)
        pass

if __name__ == "__main__":
    calc = Correct_Workouts(1)
    calc.pull_workouts()
    calc.fit_curve()
    calc.calc_wattage()
