import numpy as np


def compute_information_processing_index(initTime, endTime, fx, fy,
                                         short_threshold, long_threshold):
    """
    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :return: a measure of the information processing index
    :param short_threshold: a baseline value for the low threshold
    :type short_threshold: float
    :param long_threshold: a baseline value for the high threshold
    :type long_threshold: float
    :rtype: float
    """

    assert type(initTime) == type(endTime) == list
    assert len(initTime) == len(endTime) == len(fx) == len(fy)
    div = ipi_helper(initTime, endTime, fx, fy)
    number_of_long_f_short_s = max(np.sum(np.asarray(div) > long_threshold), 1)
    return np.sum(np.asarray(div) < short_threshold) / number_of_long_f_short_s


def ipi_helper(initTime, endTime, fx, fy):
    """
    Find the ratio between the distance and duration of saccade/fixations

    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :return: ratios between distance and duration of saccade/fixations
    :rtype: list of float
    """
    div = []
    for i in range(min(len(initTime), len(endTime)) - 1):
        current_fixation_duration = fixation_duration(initTime[i], endTime[i])
        current_saccade_length = saccade_length(fx[i], fy[i], fx[i + 1], fy[i + 1])
        div.append(current_fixation_duration / current_saccade_length)
    return div


def compute_ipi_thresholds(initTime, endTime, fx, fy):
    """
    Computes threshold values for the 25th and 75th percentile of the ratio between distance and duration of saccades

    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :return: lower and higher threshold
    :rtype: (float, float)
    """
    assert type(initTime) == type(endTime) == list
    assert len(initTime) == len(endTime) == len(fx) == len(fy)
    div = ipi_helper(initTime, endTime, fx, fy)

    short_threshold = np.percentile(np.asarray(div), 25)
    long_threshold = np.percentile(np.asarray(div), 75)
    return short_threshold, long_threshold


def fixation_duration(startTime, endTime):
    """
    Finds the duration of a saccade

    :param startTime: start of the saccade/fixation
    :type startTime: int
    :param endTime: end of the saccade/fixation
    :type endTime: int
    :return: duration of the saccade
    :rtype: int
    """
    return endTime - startTime


def saccade_length(x1, y1, x2, y2):
    """
    finds the length of the saccade

    :param x1: x coordinate of the previous fixation point
    :type x1: int
    :param y1: y coordinate of the previous fixation point
    :type y1: int
    :param x2: x coordinate of the current fixation point
    :type x2: int
    :param y2: y coordinate of the current fixation point
    :type y2: int
    :return: the saccade length measured in euclidean distance
    :rtype: float
    """
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
