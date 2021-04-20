import time
from collections import deque
import crunch.util as util


class DataHandler:
    """
    Class that subscribes to a specific raw data stream,
    handles storing the data,
    preprocessing the data,
    and calculating measurements from the data
    """
    def __init__(self, measurement_func=None, measurement_path=None,
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

        self.data_queue = deque(maxlen=window_length)
        self.data_counter = 0
        self.phase_func = self.baseline_phase if calculate_baseline else self.csv_phase
        self.window_step = window_step
        self.window_length = window_length
        self.measurement_func = measurement_func
        self.measurement_path = measurement_path
        self.calculate_baseline = calculate_baseline

        self.baseline = 0
        self.list_of_baseline_values = []
        self.baseline_phase_time_in_sec = 10
        self.baseline_end_time = time.time() + self.baseline_phase_time_in_sec
        self.time = util.Time()

    def __str__(self):
        return self.measurement_func.__name__

    def baseline_phase(self):
        """
        Appends a value to be used for calculating the baseline, then checks if it is time to
        transition to next phase
        """
        if self.data_counter % self.window_step == 0 and len(self.data_queue) == self.window_length:
            measurement = self.measurement_func(list(self.data_queue))
            self.list_of_baseline_values.append(measurement)
            if time.time() > self.baseline_end_time:
                self.transition_to_csv_phase()

    def add_data_point(self, datapoint):
        """ Receive a new data point, and call appropriate measurement function when we have enough points """
        self.data_queue.append(datapoint)
        self.phase_func()

    def transition_to_csv_phase(self):
        self.baseline = float(sum(self.list_of_baseline_values) / len(self.list_of_baseline_values))
        assert 0 <= self.baseline < float('inf') and type(self.baseline) == float
        self.phase_func = self.csv_phase

    def csv_phase(self):
        if self.data_counter % self.window_step == 0 and len(self.data_queue) == self.window_length:
            measurement = self.measurement_func(list(self.data_queue))
            if self.calculate_baseline:
                measurement = round(measurement/self.baseline, 6)
            util.write_csv(self.measurement_path, [self.time.delta_time(), measurement])
        self.data_counter += 1
