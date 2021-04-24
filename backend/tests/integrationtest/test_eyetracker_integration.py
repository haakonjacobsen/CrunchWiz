import os
from unittest.mock import patch

import pandas as pd

from crunch.eyetracker.main import start_eyetracker


class MockAPI:
    """
    Mock api that reads from csv files instead of getting data from devices
    """
    dirname = os.path.dirname(__file__)
    data = pd.read_csv(os.path.join(dirname, "../mock_data/eyetracker.csv"))
    raw_data = {"fixation": ["initTime", "endTime", "fx", "fy"], "gaze": ["lpup", "rpup"]}
    subscribers = {"fixation": [], "gaze": []}

    def add_subscriber(self, data_handler, requested_data):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        :param requested_data: The specific raw data that the data handler subscribes to
        :type requested_data: str
        """
        assert requested_data in self.subscribers
        self.subscribers[requested_data].append(data_handler)

    def connect(self):
        """ Simulates connecting to the device, starts reading from csv files and push data to handlers """
        for i in range(1, 1000):
            self._mock_datapoint(i, "fixation")
            for _ in range(20):
                self._mock_datapoint(i, "gaze")

    def _mock_datapoint(self, index, name):
        if index < len(self.data):
            datapoint = {raw_data: self.data[raw_data][index] for raw_data in self.raw_data[name]}
            for subscriber in self.subscribers[name]:
                subscriber.add_data_point(datapoint)


class MockCSV:
    measurements_written = set()

    def write_csv(self, path, *args, **kwargs):
        self.measurements_written.add(path)


def test_eyetracker_integration():
    """ Test that all measurement files are written to, when executing the empatica program """
    mock_csv = MockCSV()
    with patch("crunch.util.write_csv", mock_csv.write_csv):
        start_eyetracker(MockAPI)

    assert 'anticipation.csv' in mock_csv.measurements_written
    assert 'cognitive_load.csv' in mock_csv.measurements_written
    assert 'perceived_difficulty.csv' in mock_csv.measurements_written
    assert 'information_processing_index.csv' in mock_csv.measurements_written
