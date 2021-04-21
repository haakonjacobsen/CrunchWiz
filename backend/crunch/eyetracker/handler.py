import time

import crunch.util as util

from .measurements.cognitive_load import compute_cognitive_load
from .measurements.information_processing_index import (compute_information_processing_index,
                                                        compute_ipi_thresholds)


class DataHandler:
    """
    Class that subscribes to fixation data streams and gets 10 second time window slices of preprocessed data.
    The class has 2 phases:
        1. baseline_phase: phase_func is set to the function self.baseline_phase. This function is called and
        appends the result of the measurement function to self.list_of_baseline_values.
        If 60 seconds have passed and we have at least 30 measurement values, then transition to 2. phase by
        setting the phase_function to the send_measurement function, and setting the baseline to average of
        list_of_baseline_values

        2. csv phase: The ratio of the measurement result and the baseline is written to csv

    """

    def __init__(self, measurement_func, measurement_path,
                 list_of_raw_data_subscribed_to=["initTime", "endTime", "fx", "fy", "lpup", "rpup"]):
        """
        :param measurement_func: the function we call to compute measurements from the raw data
        :type measurement_func: (list) -> float
        :param measurement_path: path to the output csv file
        :type measurement_path: str
        :param list_of_raw_data_subscribed_to: list of all the raw data to listen on
        :type list_of_raw_data_subscribed_to: list of string
        """
        assert measurement_func and measurement_path and \
            "Need to supply the required parameters"

        self.measurement_func = measurement_func
        self.measurement_path = measurement_path
        self.phase_func = self.baseline_phase
        self.baseline = None
        self.list_of_raw_data_subscribed_to = list_of_raw_data_subscribed_to
        self.time = util.Time()

        # delete probably
        self.time_window_in_sec = 10

        # baseline phase:
        self.list_of_baseline_values = []
        self.baseline_phase_time_in_sec = 60
        self.baseline_end_time = time.time() + self.baseline_phase_time_in_sec

    def send_data_window(self, raw_data):
        """
        The function is called from EyetrackerAPI. It computes the measurement and calls the
        function bound to phase_func:
            the first 60 seconds, phase_func is bound to self.baseline_phase()
            After the baseline has been calculated, it is bound to self.csv_phase()
        :param raw_data: A window of fixation points accumulated over 10 seconds
        :type raw_data: dictionary of lists of floats
        """
        measurement_result = self.measurement_func(**raw_data)
        self.phase_func(measurement_result)

    def baseline_phase(self, measurement_result):
        """
        Appends a value to be used for calculating the baseline, then checks if it is time to
        transition to next phase
        :param measurement_result: the result of calling the measurement function
        :type measurement_result: float
        """
        self.list_of_baseline_values.append(measurement_result)
        if len(self.list_of_baseline_values) > 5 and time.time() > self.baseline_end_time:
            self.transition_to_csv_phase()

    def transition_to_csv_phase(self):
        """Sets the baseline to the average of the baseline values collected, and sets phase_func to csv_phase"""
        self.baseline = float(sum(self.list_of_baseline_values) / len(self.list_of_baseline_values))
        assert 0 <= self.baseline < float('inf') and type(self.baseline) == float
        self.phase_func = self.csv_phase

        #  Save memory
        self.list_of_baseline_values = None

    def csv_phase(self, measurement_result):
        """
        Compute ratio of measurement_result and baseline, then write to csv
        :param measurement_result: the result of calling the measurement function
        :type measurement_result: float
        """
        result_ratio = measurement_result / self.baseline
        util.write_csv(self.measurement_path, [self.time.delta_time(), result_ratio])

    def get_data_subscribtions(self):
        return self.list_of_raw_data_subscribed_to


class IpiHandler(DataHandler):
    """
    Computing the information processing index requires 3 phases, as threshold values are needed to
    compute the first measurement value. This makes a specialized handler necessary.
    IpiHandler inherits from DataHandler as the baseline_phase and csv_phase are very similar
    """

    def __init__(self, measurement_func=compute_information_processing_index, measurement_path="ipi.csv", ):
        """
        :param measurement_func: the function we call to compute measurements from the raw data
        :type measurement_func: (list) -> float
        :param measurement_path: path to the output csv file
        :type measurement_path: str
        """
        DataHandler.__init__(self, measurement_func, measurement_path, ["initTime", "endTime", "fx", "fy"])
        self.phase_func = self.threshold_phase

        self.short_threshold = None
        self.long_threshold = None

        #  threshold phase
        self.dict_of_lists_of_threshold_values = {"initTime": [], "endTime": [], "fx": [], "fy": []}
        self.threshold_time_in_sec = 30  # change to 60?
        self.threshold_phase_end = time.time() + self.threshold_time_in_sec

    def send_data_window(self, raw_data):
        """
        Called by real api. Call phase_func, which is 1. threshold_phase, 2. baseline_phase, 3. csv_phase

        :param raw_data: A window of fixation points accumulated over 10 seconds
        :type raw_data: dictionary of lists of floats
        """
        self.phase_func(raw_data)

    def threshold_phase(self, raw_data):
        """
        Store the fixation data points and check if enough time has passed to transition to baseline phase

        :param raw_data: A window of fixation points accumulated over 10 seconds
        :type raw_data: dictionary of lists of floats
        """
        # print("HANDLER threshold phase: ", len(self.dict_of_lists_of_threshold_values["initTime"]),raw_data)

        self.dict_of_lists_of_threshold_values["initTime"].extend(raw_data["initTime"])
        self.dict_of_lists_of_threshold_values["endTime"].extend(raw_data["endTime"])
        self.dict_of_lists_of_threshold_values["fx"].extend(raw_data["fx"])
        self.dict_of_lists_of_threshold_values["fy"].extend(raw_data["fy"])

        # check if 60 seconds have passed and we have at least 30 values. If true, transition to baseline phase
        if time.time() > self.threshold_phase_end and len(self.dict_of_lists_of_threshold_values["initTime"]) > 10:
            self.transition_to_baseline_phase()

    def transition_to_baseline_phase(self):
        """Compute and set threshold values, set phase_func to baseline_phase, set baseline timer"""
        self.short_threshold, self.long_threshold = compute_ipi_thresholds(
            self.dict_of_lists_of_threshold_values["initTime"],
            self.dict_of_lists_of_threshold_values["endTime"],
            self.dict_of_lists_of_threshold_values["fx"],
            self.dict_of_lists_of_threshold_values["fy"]
        )
        self.short_threshold = float(self.short_threshold)
        self.long_threshold = float(self.long_threshold)
        assert type(self.short_threshold) == float and 0 < self.short_threshold < float('inf')
        assert type(self.long_threshold) == float and 0 < self.long_threshold < float('inf')
        assert self.short_threshold < self.long_threshold
        # transition to baseline phase
        self.phase_func = self.baseline_phase
        self.baseline_end_time = time.time() + self.baseline_phase_time_in_sec

        # save memory
        self.dict_of_lists_of_threshold_values = None

    def baseline_phase(self, raw_data):
        """
        Compute result and send to parent method of same name.

        :param raw_data: A window of fixation points accumulated over 10 seconds
        :type raw_data: dictionary of lists of floats
        """
        measurement_result = self.measurement_func(raw_data["initTime"], raw_data["endTime"],
                                                   raw_data["fx"], raw_data["fy"],
                                                   self.short_threshold, self.long_threshold)

        DataHandler.baseline_phase(self, measurement_result)

    def csv_phase(self, raw_data):
        """
        Compute result and send to parent method of same name.

        :param raw_data: A window of fixation points accumulated over 10 seconds
        :type raw_data: dictionary of lists of floats
        """
        DataHandler.csv_phase(self, self.measurement_func(raw_data["initTime"], raw_data["endTime"],
                                                          raw_data["fx"], raw_data["fy"],
                                                          self.short_threshold, self.long_threshold))


class CognitiveLoadHandler(DataHandler):
    """
    Cognitive load needs 500 values to calculate one measurement value. It is otherwise identical
    to the DataHandler
    """

    def __init__(self):
        DataHandler.__init__(
            self, compute_cognitive_load, "cognitive_load.csv", ["initTime", "endTime", "lpup", "rpup"]
        )
        self.dict_of_lists_of_values = {"initTime": [], "endTime": [], "lpup": [], "rpup": []}

    def send_data_window(self, raw_data):
        self.dict_of_lists_of_values["initTime"].extend(raw_data["initTime"])
        self.dict_of_lists_of_values["endTime"].extend(raw_data["endTime"])
        self.dict_of_lists_of_values["lpup"].extend(raw_data["lpup"])
        self.dict_of_lists_of_values["rpup"].extend(raw_data["rpup"])

        if len(self.dict_of_lists_of_values["initTime"]) >= 500:
            measurement_result = self.measurement_func(**self.dict_of_lists_of_values)
            self.phase_func(measurement_result)
            self.dict_of_lists_of_values = {"initTime": [], "endTime": [], "lpup": [], "rpup": []}
