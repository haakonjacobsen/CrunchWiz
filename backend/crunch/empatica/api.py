import pandas as pd
from .handler import DataHandler  # noqa


class MockApi:
    """
    Mock api that reads from csv files instead of getting data from devices
    """
    eda_data = pd.read_csv("crunch/empatica/mock_data/EDA.csv")["EDA"]
    ibi_data = pd.read_csv("crunch/empatica/mock_data/IBI.csv")["IBI"]
    temp_data = pd.read_csv("crunch/empatica/mock_data/TEMP.csv")["TEMP"]
    hr_data = pd.read_csv("crunch/empatica/mock_data/HR.csv")["HR"]

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
            self._mock_eda_datapoint(i)
            self._mock_temp_datapoint(i)
            self._mock_ibi_datapoint(i)
            self._mock_hr_datapoint(i)

            # simulate delay of new data points by sleeping
            # time.sleep(0.1)

    def _mock_ibi_datapoint(self, index):
        if index < len(self.ibi_data):
            for handler in self.subscribers["IBI"]:
                data_point = self.ibi_data[index]
                handler.add_data_point(data_point)

    def _mock_eda_datapoint(self, index):
        if index < len(self.eda_data):
            for handler in self.subscribers["EDA"]:
                data_point = self.eda_data[index]
                handler.add_data_point(data_point)

    def _mock_temp_datapoint(self, index):
        if index < len(self.temp_data):
            for handler in self.subscribers["TEMP"]:
                data_point = self.temp_data[index]
                handler.add_data_point(data_point)

    def _mock_hr_datapoint(self, index):
        if index < len(self.hr_data):
            for handler in self.subscribers["HR"]:
                data_point = self.hr_data[index]
                handler.add_data_point(data_point)


# TODO implement real api
class RealAPI:
    pass
