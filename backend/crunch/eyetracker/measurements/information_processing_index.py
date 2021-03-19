import numpy as np


def compute_information_processing_index(initTime=None, endTime=None, fx=None, fy=None, short_threshold=None, long_threshold=None):
    """
    Takes a list of init and and a list of end-times from a 10 second time window.
    Take the 25 percentile for the short (fixation duration/saccade length) and 75
    percentile for long (fixation duration/saccade length). Preferred window size
    is 10 seconds.
    """
    assert type(initTime) == type(endTime) == list
    assert len(initTime) == len(endTime) == len(fx) == len(fy)
    div = []
    for i in range(min(len(initTime), len(endTime)) - 1):
        current_fixation_duration = fixation_duration(initTime[i], endTime[i])
        current_saccade_length = saccade_length(fx[i], fy[i], fx[i + 1], fy[i + 1])
        div.append(current_fixation_duration / current_saccade_length)

    if np.sum(np.asarray(div) > long_threshold) == 0:
        # TODO handle divide by zero error
        return 1
    return np.sum(np.asarray(div) < short_threshold) / np.sum(np.asarray(div) > long_threshold)


def fixation_duration(start_time1, end_time1):
    return end_time1 - start_time1


def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
