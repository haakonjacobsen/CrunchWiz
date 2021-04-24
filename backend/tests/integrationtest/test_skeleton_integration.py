import os
from unittest.mock import patch

import pandas as pd

from crunch.skeleton.main import start_skeleton


class MockAPI:
    """
    Mock api that reads from csv files instead of getting data from devices

    :type subscribers: dict
    """

    subscribers = {"body": []}

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
        df = pd.pandas.read_csv(os.path.join(os.path.dirname(__file__), "../mock_data/skeleton.csv"), header=None)
        for i in range(len(df)):
            formatted_row = []
            row = df.iloc[i].tolist()
            for j in range(0, len(row) - 1, 2):
                formatted_row.append((float(row[j].strip().strip("[]()")), float(row[j + 1].strip().strip("[]()"))))
            self._mock_datapoint(formatted_row)

    def _mock_datapoint(self, data):
        for subscriber in self.subscribers["body"]:
            subscriber.add_data_point(data)


class MockCSV:
    measurements_written = set()

    def write_csv(self, path, *args, **kwargs):
        self.measurements_written.add(path)


def test_skeleton_integration():
    """ Test that all measurement files are written to, when executing the empatica program """
    mock_csv = MockCSV()
    with patch("crunch.util.write_csv", mock_csv.write_csv):
        start_skeleton(MockAPI)

    assert 'amount_of_motion.csv' in mock_csv.measurements_written
    assert 'fatigue.csv' in mock_csv.measurements_written
    assert 'most_used_joints.csv' in mock_csv.measurements_written
    assert 'stability_of_motion.csv' in mock_csv.measurements_written
