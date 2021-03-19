# import measurement_functions
import pandas as pd
# from .measurement_functions import compute_perceived_difficulty
from .measurement_functions import compute_information_processing_index


def _compute_information_processing_index():
    init = pd.read_csv("crunch/eyetracker/ET-data-S001.csv", usecols=["initTime"])
    end = pd.read_csv("crunch/eyetracker/ET-data-S001.csv", usecols=["endTime"])
    fx = pd.read_csv("crunch/eyetracker/ET-data-S001.csv", usecols=["fx"])
    fy = pd.read_csv("crunch/eyetracker/ET-data-S001.csv", usecols=["fy"])
    init = init.values.flatten().tolist()
    end = end.values.flatten().tolist()
    fx = fx.values.flatten().tolist()
    fy = fy.values.flatten().tolist()
    window_size = 10
    for i in range(1, len(init), window_size):
        if len(init[i:]) >= window_size:
            ipi = compute_information_processing_index(init[i:i+window_size], end[i:i+window_size],
                                                       fx[i:i + window_size], fy[i:i + window_size], 0.8, 3.2
                                                       )
            if ipi:
                pass


def _compute_perceived_difficulty():
    df = pd.read_csv("crunch/eyetracker/ET-data-S001.csv")

    def _get_vals(n):
        vals = []
        try:
            for i in range(n):
                vals.append(df.iloc[i])
        except IndexError:
            print("Error")
        return vals

    # TODO: What to send to percieved_difficulty function
    # window_size = 11
    # for i in range(1, len(df), window_size):
    #     if len(df.iloc[i:]) >= window_size:
    #         pd_ = compute_perceived_difficulty(_get_vals(i))
    #         print("PERCIEVED DIFFICULTY", pd_)


def eyetracker_main():
    """
    Get data from Tobii eye tracker API
    Preprocess
    Write to csv

    :return: void
    """
    print("eyetracker process succesfully started")
    _compute_information_processing_index()
    _compute_perceived_difficulty()

    # TODO: ADD Cognitive load & anticipation measurements
    # TODO: What to pass to compute_percieved_difficulty
