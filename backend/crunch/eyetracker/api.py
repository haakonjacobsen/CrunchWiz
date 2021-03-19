import pandas as pd
from .handler import DataHandler  # noqa


class MockApi:
    """
    Mock api that reads from csv files instead of getting data from devices

    :type subscribers: list of (DataHandler, list of str)
    """
    eyetracker_data = pd.read_csv("crunch/eyetracker/mock_data/ET-data-S001.csv")

    # TODO key = handler, value is list of what they want
    raw_data = ["initTime", "endTime", "fx", "fy"]
    subscribers = []

    def add_subscriber(self, data_handler, requested_data):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        :param requested_data: The specific raw data that the data handler subscribes to
        :type requested_data: list(str)
        """
        assert all(data in self.raw_data for data in requested_data)
        self.subscribers.append((data_handler, requested_data))

    def connect(self):
        """ Simulates connecting to the device, starts reading from csv files and push data to handlers """
        for i in range(1000):
            self._mock_datapoint(i)

            # simulate delay of new data points by sleeping
            # time.sleep(0.1)

    def _mock_datapoint(self, index):
        if index < len(self.eyetracker_data):
            for subscriber, raw_datas in self.subscribers:
                data = {raw_data: self.eyetracker_data[raw_data][index] for raw_data in raw_datas}
                subscriber.add_data_point(data)


# TODO implement real api
class RealAPI:
    pass
