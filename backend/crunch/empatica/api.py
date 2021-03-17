import pandas as pd
import time


class MockApi:
    """
    Mock api that reads from csv files instead of getting data from devices
    """
    eda_data = pd.read_csv("crunch/empatica/S001/EDA.csv")["EDA"]
    ibi_data = pd.read_csv("crunch/empatica/S001/IBI.csv")["IBI"]
    temp_data = pd.read_csv("crunch/empatica/S001/TEMP.csv")["TEMP"]
    hr_data = pd.read_csv("crunch/empatica/S001/HR.csv")["HR"]

    def __init__(self, handler_eda, handler_ibi, handler_temp, handler_hr):
        self.handler_eda = handler_eda
        self.handler_ibi = handler_ibi
        self.handler_temp = handler_temp
        self.handler_hr = handler_hr

    def connect(self):
        """ Simulates connecting to the device, starts reading from csv files and push data to handlers """
        for i in range(1000):
            self._mock_eda_datapoint(i)
            self._mock_temp_datapoint(i)
            self._mock_ibi_datapoint(i)
            self._mock_hr_datapoint(i)

            # simulate delay of new data points by sleeping
            time.sleep(0.1)

    def _mock_ibi_datapoint(self, index):
        if index < len(self.ibi_data):
            data_point = self.ibi_data[index]
            self.handler_ibi.add_data_point(data_point)

    def _mock_eda_datapoint(self, index):
        if index < len(self.eda_data):
            data_point = self.eda_data[index]
            self.handler_eda.add_data_point(data_point)

    def _mock_temp_datapoint(self, index):
        if index < len(self.temp_data):
            data_point = self.temp_data[index]
            self.handler_temp.add_data_point(data_point)

    def _mock_hr_datapoint(self, index):
        if index < len(self.hr_data):
            data_point = self.hr_data[index]
            self.handler_hr.add_data_point(data_point)


# TODO implement real api
class RealAPI:
    pass
