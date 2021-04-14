import pandas as pd
import time
import os

from math import isnan

from crunch.eyetracker.handler import DataHandler, IpiHandler # noqa


class GazedataToFixationdata:
    """
    Class that takes in gaze data points from the EyetrackerAPI, preprocesses the gaze points,
     and computes fixation_data.

    RealAPI calls insert_new_gaze_data, the rest is helper functions.
    For more information on gaze data and fixation data, see:
    https://www.tobiipro.com/learn-and-support/learn/eye-tracking-essentials/types-of-eye-movements/
    """
    list_of_gaze_data_points_in_a_fixation = []
    last_gaze_data_point = None
    last_velocity_was_fixation = None

    screen_proportions = (1920, 1080)
    velocity_threshold = 0.05
    first_time_stamp = None
    last_valid_pupil_data = (0.5, 0.5)
    # d temp, used for debugging and should be deleted:
    list_of_velocities = []
    list_of_high_velocities = []

    def insert_new_gaze_data(self, left_eye_fx, left_eye_fy, right_eye_fx, right_eye_fy, lpup, rpup, timestamp):
        """
        Called from RealAPI
        All parameters are float, but can be nan.
        return: fixation point or None

        """

        fixation_point = None
        fx = self.preprocess_eyetracker_gazepoint(left_eye_fx, right_eye_fx, is_fx=True) * self.screen_proportions[0]
        fy = self.preprocess_eyetracker_gazepoint(left_eye_fy, right_eye_fy, is_fx=False) * self.screen_proportions[1]
        lpup, rpup = self.preprocess_eyetracker_pupils(lpup, rpup)

        if self.last_gaze_data_point is not None:
            velocity = self.velocity(fx, fy, timestamp, self.last_gaze_data_point['fx'],
                                     self.last_gaze_data_point['fy'],
                                     self.last_gaze_data_point['timestamp'])

            self.list_of_velocities.append(velocity)  # d

            # Check if this is a saccade
            if velocity > self.velocity_threshold:
                if self.last_velocity_was_fixation and len(self.list_of_gaze_data_points_in_a_fixation) > 2:
                    fixation_point = self.end_fixation()
                self.last_velocity_was_fixation = False

            # If not a saccade, this is a fixation
            else:
                self.last_velocity_was_fixation = True
                self.list_of_gaze_data_points_in_a_fixation.append(
                    {"fx": fx, "fy": fy, "lpup": lpup, "rpup": rpup, "timestamp": timestamp}
                )

        self.last_gaze_data_point = {"fx": fx, "fy": fy, "lpup": lpup, "rpup": rpup, "timestamp": timestamp}
        if self.first_time_stamp is None:
            self.first_time_stamp = timestamp

        return fixation_point

        # still a fixation:

    def end_fixation(self):
        number_of_gazepoints = len(self.list_of_gaze_data_points_in_a_fixation)

        initTime = (self.list_of_gaze_data_points_in_a_fixation[0]["timestamp"] - self.first_time_stamp) / 1000
        endTime = (self.list_of_gaze_data_points_in_a_fixation[-1]["timestamp"] - self.first_time_stamp) / 1000
        fx = sum(gazepoint['fx'] for gazepoint in self.list_of_gaze_data_points_in_a_fixation) / number_of_gazepoints
        fy = sum(gazepoint['fy'] for gazepoint in self.list_of_gaze_data_points_in_a_fixation) / number_of_gazepoints
        lpup = sum(
            gazepoint['lpup'] for gazepoint in self.list_of_gaze_data_points_in_a_fixation) / number_of_gazepoints
        rpup = sum(
            gazepoint['rpup'] for gazepoint in self.list_of_gaze_data_points_in_a_fixation) / number_of_gazepoints
        fixation_point = {"initTime": initTime, "endTime": endTime, "fx": fx, "fy": fy, "lpup": lpup, "rpup": rpup}
        self.list_of_gaze_data_points_in_a_fixation = []

        return fixation_point

    def distance(self, fx1, fy1, fx2, fy2):
        """returns euclidean distance"""
        return ((fx1 - fx2) ** 2 + (fy1 - fy2) ** 2) ** 0.5

    def velocity(self, fx1, fy1, timestamp1, fx2, fy2, timestamp2):
        """Velocity measures how fast the eyes move from gazepoint 1 to gazepoint 2. euclidean distance/time"""
        return self.distance(fx1, fy1, fx2, fy2) / (abs(timestamp2 - timestamp1))

    def set_screen_proportions(self, width=1920, height=1080):
        self.screen_proportions = (width, height)

    def preprocess_eyetracker_gazepoint(self, left_eye_fx_or_fy, right_eye_fx_or_fy, is_fx=True):
        """
        Takes in either a left and a right fx value, or a left and a right fy value
        :return fx or fy: average of the left and right eye coordinate
        :type fx or fy: float
        """
        if isnan(left_eye_fx_or_fy) and isnan(right_eye_fx_or_fy):
            if is_fx and self.last_gaze_data_point is not None:
                return self.last_gaze_data_point["fx"]
            elif not is_fx and self.last_gaze_data_point is not None:
                return self.last_gaze_data_point["fy"]
            else:
                return 0

        elif isnan(left_eye_fx_or_fy):
            left_eye_fx_or_fy = right_eye_fx_or_fy
        elif isnan(right_eye_fx_or_fy):
            right_eye_fx_or_fy = left_eye_fx_or_fy
        return (left_eye_fx_or_fy + right_eye_fx_or_fy) / 2

    def preprocess_eyetracker_pupils(self, lpup, rpup):
        """If pupil data is invalid, use previous pupil data, or the other valid pupil"""
        if isnan(lpup) and isnan(rpup):
            return self.last_valid_pupil_data[0], self.last_valid_pupil_data[1]
        elif isnan(lpup) and not isnan(rpup):
            self.last_valid_pupil_data = (rpup, rpup)
            return rpup, rpup
        elif not isnan(lpup) and isnan(rpup):
            self.last_valid_pupil_data = (lpup, lpup)
            return lpup, lpup

        else:
            self.last_valid_pupil_data = (lpup, rpup)
            return lpup, rpup
            # use previous values

    def print_debug(self):
        print(self.list_of_high_velocities, self.list_of_velocities, self.list_of_gaze_data_points_in_a_fixation)

    def coordinate_is_valid(self, c):
        if type(c) == float and not isnan(c):
            return min(0, max(1, c))


class EyetrackerAPI:
    """
    Responsible for receiving data from the eyetracker, cleaning it, and send a 10 second time window
    of fixation data to every handler.
    """
    list_of_raw_data_names = ["initTime", "endTime", "fx", "fy", "lpup", "rpup"]
    dict_of_lists_of_fixation_data = {"initTime": [], "endTime": [], "fx": [], "fy": [], "lpup": [], "rpup": []}
    list_of_handlers = []
    window_size_in_sec = 10
    last_window_time = time.time()
    gaze_to_fixation = GazedataToFixationdata()

    # handle preprocessing

    def insert_new_gaze_data(self, left_eye_fx, left_eye_fy, right_eye_fx, right_eye_fy, lpup, rpup, timestamp):
        fixation_point_or_none = self.gaze_to_fixation.insert_new_gaze_data(left_eye_fx, left_eye_fy,
                                                                            right_eye_fx, right_eye_fy,
                                                                            lpup, rpup, timestamp)
        if fixation_point_or_none is not None:
            # print("realAPI fixation: ", self.dict_of_lists_of_fixation_data)
            self.insert_new_fixation_data(fixation_point_or_none['initTime'],
                                          fixation_point_or_none['endTime'],
                                          fixation_point_or_none['lpup'],
                                          fixation_point_or_none['rpup'],
                                          fixation_point_or_none['fx'],
                                          fixation_point_or_none['fy'])
            if self.is_time_to_send_next_window():
                self.send_data_to_handlers()

    def is_time_to_send_next_window(self):
        return (time.time() > self.last_window_time + self.window_size_in_sec and
                len(self.dict_of_lists_of_fixation_data["initTime"]) > 5)

    def send_data_to_handlers(self):
        """Send data to all handlers, reset lists raw data lists, update timer """
        for handler in self.list_of_handlers:
            handler.send_data_window(
                {key: self.dict_of_lists_of_fixation_data[key] for key in handler.get_data_subscribtions()}
            )
        self.last_window_time = time.time()
        self.reset_fixation_data_lists()

    def insert_new_fixation_data(self, initTime, endTime, lpup, rpup, fx, fy):
        self.dict_of_lists_of_fixation_data["initTime"].append(initTime)
        self.dict_of_lists_of_fixation_data["endTime"].append(endTime)
        self.dict_of_lists_of_fixation_data["lpup"].append(lpup)
        self.dict_of_lists_of_fixation_data["rpup"].append(rpup)
        self.dict_of_lists_of_fixation_data["fx"].append(fx)
        self.dict_of_lists_of_fixation_data["fy"].append(fy)

    def reset_fixation_data_lists(self):
        self.dict_of_lists_of_fixation_data = {"initTime": [], "endTime": [], "fx": [], "fy": [], "lpup": [],
                                               "rpup": []}

    def add_subscriber(self, handler):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        """
        self.list_of_handlers.append(handler)
