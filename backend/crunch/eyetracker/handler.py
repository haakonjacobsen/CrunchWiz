import csv
import datetime
from collections import deque


class DataHandler:
    """
    Class that subscribes to a specific raw data stream,
    handles storing the data,
    preprocessing the data,
    and calculating measurements from the data
    """
    def __init__(self, measurement_func=None, measurement_path=None, window_length=None, window_step=None, listen_on=None, baseline={}):
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
        assert window_length and window_step and measurement_func and measurement_path and listen_on, \
            "Need to supply the required parameters"

        self.data_queues = {key: deque(maxlen=window_length) for key in listen_on}
        self.data_counter = 0
        self.window_step = window_step
        self.window_length = window_length
        self.measurement_func = measurement_func
        self.measurement_path = measurement_path
        self.baseline = baseline
        self.time = datetime.datetime.now()

    def add_data_point(self, data):
        """ Receive a new data point, and call appropriate measurement function when we have enough points """
        assert len(self.data_queues) != 0, "Need to listen to at least one raw data"

        # TODO call eventual preprocessing here, should also take preprocessing function as argument in init
        for key, value in data.items():
            self.data_queues[key].append(value)

        if self.data_counter % self.window_step == 0 and all(len(queue) == self.window_length for _, queue in self.data_queues.items()):
            measurement = self.measurement_func(**{key: list(queue) for key, queue in self.data_queues.items()}, **self.baseline)
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
        with open("crunch/output/" + path, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(row)
