from .measurements.information_processing_index import compute_information_processing_index, compute_ipi_thresholds
from .measurements.cognitive_load import compute_cognitive_load
import csv
import datetime
import os
import time
from collections import deque


class DataHandler:
    """
    Class that subscribes to a specific raw data stream,
    handles storing the data,
    preprocessing the data,
    and calculating measurements from the data
    """

    def __init__(self, measurement_func=None, measurement_path=None,
                 list_of_raw_data_subscribed_to=["initTime", "endTime", "fx", "fy", "lpup", "rpup"],
                 window_length=None, window_step=None,
                 calculate_baseline=True):
        """
        :param measurement_func: the function we call to compute measurements from the raw data
        :type measurement_func: (list) -> float
        :param measurement_path: path to the output csv file
        :type measurement_path: str
        :param window_length: length of the window, i.e number of data points for the function
        :type window_length: int
        :param window_step: how many steps for a new window, i.e for 6 steps,
        a new measurement is computed every 6 data points
        :type window_step: int
        """
        assert window_length and window_step and measurement_func and measurement_path, \
            "Need to supply the required parameters"

        self.data_queues = {key: deque(maxlen=window_length) for key in list_of_raw_data_subscribed_to}
        self.data_counter = 0
        self.window_step = window_step
        self.window_length = window_length
        self.measurement_func = measurement_func
        self.measurement_path = measurement_path
        self.list_of_raw_data_subscribed_to = list_of_raw_data_subscribed_to

        self.phase_func = self.baseline_phase if calculate_baseline else self.csv_phase
        self.calculate_baseline = calculate_baseline
        self.baseline = 0
        self.list_of_baseline_values = []
        self.baseline_phase_time_in_sec = 60
        self.baseline_end_time = time.time() + self.baseline_phase_time_in_sec
        self.time = datetime.datetime.now()

    def __str__(self):
        return self.measurement_func.__name__

    def add_data_point(self, datapoint):
        """ Receive a new data point, and call appropriate measurement function when we have enough points """

        for key, value in datapoint.items():
            self.data_queues[key].append(value)
        if self.data_counter % self.window_step == 0 \
                and all(len(queue) == self.window_length for _, queue in self.data_queues.items()):
            self.phase_func()

        self.data_counter += 1

    def baseline_phase(self):
        """
        Appends a value to be used for calculating the baseline, then checks if it is time to
        transition to next phase
        """
        if self.data_counter % self.window_step == 0 and len(self.data_queues["initTime"]) == self.window_length:
            measurement = self.measurement_func(
                **{key: list(queue) for key, queue in self.data_queues.items()}
            )
            self.list_of_baseline_values.append(measurement)
            if time.time() > self.baseline_end_time:
                self.transition_to_csv_phase()

    def transition_to_csv_phase(self):
        self.baseline = float(sum(self.list_of_baseline_values) / len(self.list_of_baseline_values))
        assert 0 <= self.baseline < float('inf') and type(self.baseline) == float
        self.phase_func = self.csv_phase

        # Save memory
        self.list_of_baseline_values = None

    def csv_phase(self):
        if self.data_counter % self.window_step == 0 and len(self.data_queues["initTime"]) == self.window_length:
            measurement = self.measurement_func(
                **{key: list(queue) for key, queue in self.data_queues.items()}
            )
            if self.calculate_baseline:
                measurement = round(measurement / self.baseline, 6)
            delta_time = self._get_delta_time()
            self._write_csv(self.measurement_path, [delta_time, measurement])

    def _get_delta_time(self):
        """ finds delta time from last computed measurement """
        new_time = datetime.datetime.now()
        delta_time = (new_time - self.time).total_seconds()
        self.time = new_time
        return delta_time

    def _write_csv(self, path, row):
        """ write result to csv file """
        file_exists = os.path.isfile("crunch/output/" + path)
        with open("crunch/output/" + path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            if not file_exists:
                header = ['time', 'value']
                writer.writerow(header)
            writer.writerow(row)

    def get_list_of_raw_data_subscribed_to(self):
        return self.list_of_raw_data_subscribed_to


class IpiHandler(DataHandler):
    """
    Computing the information processing index requires 3 phases, as threshold values are needed to
    compute the first measurement value. This makes a specialized handler necessary.
    IpiHandler inherits from DataHandler as the baseline_phase and csv_phase are very similar
    """

    def __init__(self, measurement_path=None,
                 list_of_raw_data_subscribed_to=["initTime", "endTime", "fx", "fy"],
                 window_length=None, window_step=None,
                 calculate_baseline=True):
        """
        :param measurement_func: the function we call to compute measurements from the raw data
        :type measurement_func: (list) -> float
        :param measurement_path: path to the output csv file
        :type measurement_path: str
        """
        DataHandler.__init__(self, compute_information_processing_index, measurement_path,
                             ["initTime", "endTime", "fx", "fy"],
                             window_length, window_step, calculate_baseline)
        self.phase_func = self.threshold_phase

        self.short_threshold = None
        self.long_threshold = None

        #  threshold phase
        self.dict_of_lists_of_threshold_values = {"initTime": [], "endTime": [], "fx": [], "fy": []}
        self.threshold_time_in_sec = 30  # change to 60?
        self.threshold_phase_end = time.time() + self.threshold_time_in_sec

    def add_data_point(self, datapoint):
        """
        Receive a new data point, and store
        :param raw_data: A fixation point
        :type raw_data: dictionary of floats
         """

        self.phase_func(datapoint)

    def threshold_phase(self, datapoint):
        """
        Check if a minute has passed so we can compute threshold values

        :param datapoint: A fixation data point
        :type datapoint: dictionary of floats
        """
        for key, value in datapoint.items():
            self.dict_of_lists_of_threshold_values[key].append(value)

        # check if 60 seconds have passed and we have at least 30 values. If true, transition to baseline phase
        if time.time() > self.threshold_phase_end and len(self.dict_of_lists_of_threshold_values["initTime"]) > 10:
            self.transition_to_baseline_phase()

    def transition_to_baseline_phase(self):
        """Compute and set threshold values, set phase_func to baseline_phase, set baseline timer"""
        self.short_threshold, self.long_threshold = compute_ipi_thresholds(
            **self.dict_of_lists_of_threshold_values
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

    def baseline_phase(self, datapoint):
        """
        Appends a value to be used for calculating the baseline, then checks if it is time to
        transition to next phase
        """
        for key, value in datapoint.items():
            self.data_queues[key].append(value)
        self.data_counter += 1
        if self.data_counter % self.window_step == 0 and len(self.data_queues["initTime"]) == self.window_length:
            argument_dictionary = {key: list(queue) for key, queue in self.data_queues.items()}
            argument_dictionary["short_threshold"] = self.short_threshold
            argument_dictionary["long_threshold"] = self.long_threshold
            measurement = self.measurement_func(
                **argument_dictionary
            )
            self.list_of_baseline_values.append(measurement)
            if time.time() > self.baseline_end_time:
                self.transition_to_csv_phase()

    def csv_phase(self, datapoint):
        for key, value in datapoint.items():
            self.data_queues[key].append(value)
        self.data_counter += 1
        if self.data_counter % self.window_step == 0 and len(self.data_queues["initTime"]) == self.window_length:
            argument_dictionary = {key: list(queue) for key, queue in self.data_queues.items()}
            argument_dictionary["short_threshold"] = self.short_threshold
            argument_dictionary["long_threshold"] = self.long_threshold
            measurement = self.measurement_func(
                **argument_dictionary
            )
            if self.calculate_baseline:
                measurement = round(measurement / self.baseline, 6)
            delta_time = self._get_delta_time()
            self._write_csv(self.measurement_path, [delta_time, measurement])
