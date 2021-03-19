import numpy as np


def ipi_helper(initTime, endTime, fx, fy):
    """
    Returns a list of (fixation duration/saccade length)
    Used by both compute_information_processing_index and compute_ipi_thresholds.
    """
    div = []
    for i in range(min(len(initTime), len(endTime)) - 1):
        current_fixation_duration = fixation_duration(initTime[i], endTime[i])
        current_saccade_length = saccade_length(fx[i], fy[i], fx[i + 1], fy[i + 1])
        div.append(current_fixation_duration / current_saccade_length)
    return div


def compute_information_processing_index(initTime, endTime, fx, fy,
                                         short_threshold, long_threshold):
    """
    Takes 4 lists as input about fixation start and finish times, and coordinates of the gaze.
    It takes 2 float values as threshold values, made by compute_ipi_thresholds.
     The time windows should be 10 second about 10 seconds.
    Take the 25 percentile for the short (fixation duration/saccade length) and 75
    percentile for long (fixation duration/saccade length). Preferred window size
    is 10 seconds.
    """

    assert type(initTime) == type(endTime) == list
    assert len(initTime) == len(endTime) == len(fx) == len(fy)
    div = ipi_helper(initTime, endTime, fx, fy)
    number_of_long_f_short_s = max(np.sum(np.asarray(div) > long_threshold), 1)
    return np.sum(np.asarray(div) < short_threshold) / number_of_long_f_short_s


def compute_ipi_thresholds(initTime, endTime, fx, fy):
    """
    Computes threshold values used in ipi. Should be used on the baseline.
    """
    assert type(initTime) == type(endTime) == list
    assert len(initTime) == len(endTime) == len(fx) == len(fy)
    div = ipi_helper(initTime, endTime, fx, fy)

    short_threshold = np.percentile(np.asarray(div), 25)
    long_threshold = np.percentile(np.asarray(div), 75)
    return short_threshold, long_threshold


def fixation_duration(start_time1, end_time1):
    return end_time1 - start_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
