"""

def api():
    gets datapoints at different frequencies
    when they get datapoint, pass them to handlers?
"""
import pandas as pd

"""Mock api, reads from csv files and simulates real api, will be replaced by real api"""


class MockApi:
    def __init__(self):
        pass

    def connect(self, handler_eda):
        eda_data = pd.read_csv("crunch/empatica/S001/EDA.csv")
        eda_data = eda_data[eda_data.index != 0]
        eda_data.columns = ["EDA"]

        for d in eda_data["EDA"][0:161]:
            handler_eda.add_eda_point(d)


# This is where we will create the real api
class RealAPI:
    pass
