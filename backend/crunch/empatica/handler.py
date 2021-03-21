import csv
import datetime
import os
from collections import deque


class DataHandler:
    """
    Class that subscribes to a specific raw data stream,
    handles storing the data,
    preprocessing the data,
    and calculating measurements from the data
    """
    def __init__(self, measurement_func=None, measurement_path=None, window_length=None, window_step=None):
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
        self.window_step = window_step
        self.window_length = window_length
        self.measurement_func = measurement_func
        self.measurement_path = measurement_path
        self.time = datetime.datetime.now()

    def add_data_point(self, datapoint):
        """ Receive a new data point, and call appropriate measurement function when we have enough points """
        # TODO call eventual preprocessing here, should also take preprocessing function as argument in init
        self.data_queue.append(datapoint)
        if self.data_counter % self.window_step == 0 and len(self.data_queue) == self.window_length:
            measurement = self.measurement_func(list(self.data_queue))
            delta_time = self._get_delta_time()
            self._write_csv(self.measurement_path, [delta_time, measurement])
        self.data_counter += 1

    def _get_delta_time(self):
        """ finds delta time from last computed measurement """
        new_time = datetime.datetime.now()
        delta_time = (new_time - self.time).total_seconds()
        self.time = new_time
        return delta_time

    def _write_csv(self, path, row):
        """ write result to csv file """
        file_exists = os.path.isfile(path)
        with open("crunch/output/" + path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            if not file_exists:
                header = ['time', 'value']
                writer.writerow(header)
            writer.writerow(row)
