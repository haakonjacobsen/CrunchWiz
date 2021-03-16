import pandas as pd
# import numpy as np
from .measurement_functions import compute_stress
from .measurement_functions import compute_emotional_regulation
from .measurement_functions import compute_entertainment
from .measurement_eda import EDA_handler


def _compute_ibi_measurements():
    df = pd.read_csv("crunch/empatica/S001/IBI.csv", usecols=[" IBI"])
    ibi_data = df.values.flatten().tolist()
    for i in range(1, len(ibi_data), 11):
        if len(ibi_data[i:]) >= 11:
            em = compute_emotional_regulation(ibi_data[i:i+11])
            en = compute_entertainment(ibi_data[i:i+11])
            if em or en:
                pass


def _compute_eda_measurements():
    # READ DATA AND FORMAT
    data = pd.read_csv("crunch/empatica/S001/EDA.csv")
    # startTime = pd.to_datetime(float(data.columns.values[0]), unit="s")
    # sampleRate = float(data.iloc[0][0])
    data = data[data.index != 0]
    data.columns = ["EDA"]
    # data.index = pd.date_range(start=startTime, periods=len(data), freq='250L')

    # instantiate class
    eda_handler = EDA_handler()

    # add the first 161 data points, which is 40 seconds worth
    # after 30 seconds will create first measurement
    # after 10 more seconds (40 total) will create second measurement
    for d in data["EDA"][0:161]:
        ret = eda_handler.add_eda_point(d)
        if ret:
            pass


def _compute_stress():
    """
    Sends 8 temperature values from CSV file to compute_stress function
    :return: void
    """
    df = pd.read_csv("crunch/empatica/S001/TEMP2.csv")
    temperature_data = df.values.flatten().tolist()
    for i in range(1, len(temperature_data), 8):
        if len(temperature_data[i:]) >= 8:
            stress = compute_stress(temperature_data[i:i+8])
            if stress != 0.5:
                pass
            else:
                pass


def empatica_main():
    """
    Collect data from empatica E4 API
    Compute measurements
    Write to CSV
    :return: void
    """
    print("empatica process successfully started")
    _compute_stress()
    _compute_ibi_measurements()  # Emotional regulation & entertainment
    _compute_eda_measurements()  # Arousal & Engagement
