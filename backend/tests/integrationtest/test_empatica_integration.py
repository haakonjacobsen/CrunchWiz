import os
import pandas as pd

from crunch.empatica.main import start_empatica
from unittest.mock import patch


class MockAPI:
    """
    Mock api that reads from csv files instead of getting data from devices
    """

    subscribers = {"EDA": [], "IBI": [], "TEMP": [], "HR": []}

    def add_subscriber(self, data_handler, requested_data):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        :param requested_data: The specific raw data that the data handler subscribes to
        :type requested_data: str
        """
        assert requested_data in self.subscribers.keys()
        self.subscribers[requested_data].append(data_handler)

    def connect(self):
        """ Simulates connecting to the device, starts reading from csv files and push data to handlers """
        for i in range(1000):
            for name in self.subscribers:
                self._mock_datapoint(i, name)

    def _mock_datapoint(self, index, name):
        """ Simulate receiving and sending a datapoint """
        dirname = os.path.dirname(__file__)
        data = pd.read_csv(os.path.join(dirname, "../mock_data/" + name + ".csv"))[name]
        if index < len(data):
            for handler in self.subscribers[name]:
                data_point = data[index]
                handler.add_data_point(data_point)


class MockCSV:
    measurements_written = set()

    def write_csv(self, path, *args, **kwargs):
        self.measurements_written.add(path)


def test_empatica_integration():
    """ Test that all measurement files are written to, when executing the empatica program """
    mock_csv = MockCSV()
    with patch("crunch.util.write_csv", mock_csv.write_csv):
        start_empatica(MockAPI)

    assert 'engagement.csv' in mock_csv.measurements_written
    assert 'stress.csv' in mock_csv.measurements_written
    assert 'emotional_regulation.csv' in mock_csv.measurements_written
    assert 'arousal.csv' in mock_csv.measurements_written
    assert 'entertainment.csv' in mock_csv.measurements_written


