import numpy as np


def compute_percentage_of_ibi_that_differ(list_of_ibi_values):
    # Percentage of successive IBI that differ by more than 50 ms."
    window_size = 10
    assert type(list_of_ibi_values) == list
    assert len(list_of_ibi_values) > window_size
    differs_more = 0
    differs_less = 0
    for i in range(1, window_size):
        if abs(list_of_ibi_values[i] - list_of_ibi_values[i - 1]) > 0.05:
            differs_more += 1
        else:
            differs_less += 1
    return differs_more / (differs_more + differs_less)


def compute_rmssd(list_of_ibi_values):
    """
    :param list_of_ibi_values:
    :return: Root mean square of successive differences (RMSSD)
    """
    window_size = 10
    assert list == type(list_of_ibi_values)
    assert len(list_of_ibi_values) > window_size
    total = 0
    for i in range(1, window_size):
        total += (list_of_ibi_values[i] - list_of_ibi_values[i - 1]) ** 2
    return (total / (window_size - 1)) ** 0.5


def compute_normal_ibi(list_of_ibi_values):
    """
    Removes IBI values that are too large or too small
    :param list_of_ibi_values:
    :return: list of normalized IBI values
    """
    min_ibi = 0.49  # Q: What is too short and too large?
    max_ibi = 0.52
    in_range_ibi_values = [ibi for ibi in list_of_ibi_values if min_ibi < ibi < max_ibi]

    # TODO handle this in a better way, throws error since sometimes list is empty
    if not in_range_ibi_values:
        return [0]

    #  Q: I have now removed "too short and too large" intervals. What do I do now?
    return in_range_ibi_values


def compute_emotional_regulation(list_of_ibi_values):
    """
    Computes emotional regulation based on a list of IBI values
    :param list_of_ibi_values:
    :return:
    """

    rmssd = compute_rmssd(list_of_ibi_values)
    percentage_that_differ = compute_percentage_of_ibi_that_differ(list_of_ibi_values)
    normal = compute_normal_ibi(list_of_ibi_values)
    return (rmssd + percentage_that_differ + np.average(normal))/3
