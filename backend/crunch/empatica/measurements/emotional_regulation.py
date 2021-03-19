import numpy as np


def compute_percentage_of_ibi_that_differ(list_of_ibi_values):
    """
    Helper for emotional regulation
    Percentage of successive IBI that differ by more than 50 ms. 50 ms == 0.05 seconds
    """
    assert type(list_of_ibi_values) == list
    assert len(list_of_ibi_values) > 2
    differs_more = 0
    differs_less = 0
    for i in range(1, len(list_of_ibi_values)):
        if abs(list_of_ibi_values[i] - list_of_ibi_values[i - 1]) > 0.05:
            differs_more += 1
        else:
            differs_less += 1
    return differs_more / (differs_more + differs_less)


def compute_rmssd(list_of_ibi_values):
    """
    Helper for emotional regulation
    One way to measure heart rate variability.
    :param list_of_ibi_values:
    :return: Root mean square of successive differences (RMSSD)
    """
    assert list == type(list_of_ibi_values)
    assert len(list_of_ibi_values) > 2
    total = 0
    for i in range(1, len(list_of_ibi_values)):
        total += (list_of_ibi_values[i] - list_of_ibi_values[i - 1]) ** 2
    return (total / (len(list_of_ibi_values) - 1)) ** 0.5


def compute_normal_ibi(list_of_ibi_values):
    """
    Helper for emotional regulation
    Removes IBI values that are below the 10th percentile and above the 90th percentile.
    :param list_of_ibi_values:
    :return: list of normalized IBI values
    """

    min_ibi = np.percentile(np.asarray(list_of_ibi_values), 10)
    max_ibi = np.percentile(np.asarray(list_of_ibi_values), 90)
    return [ibi for ibi in list_of_ibi_values if min_ibi < ibi < max_ibi]


def compute_emotional_regulation(list_of_ibi_values):
    """
    Computes emotional regulation based on a list of IBI values
    :param list_of_ibi_values: window size = 10 seconds
    :return:
    """
    """
    mr K: "The root mean square of successive differences (RMSSD)
    ”normal” Inter-Beat Interval (IBI) à remove too short and too large
    intervals.
    Percentage of successive IBI that differ by more than 50 ms."
    """
    rmssd = compute_rmssd(list_of_ibi_values)
    percentage_that_differ = compute_percentage_of_ibi_that_differ(list_of_ibi_values)
    normal = compute_normal_ibi(list_of_ibi_values)
    return (rmssd + percentage_that_differ + np.average(normal)) / 3
