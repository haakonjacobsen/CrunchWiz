import numpy as np


def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def fixation_duration(start_time1, end_time1):
    return end_time1 - start_time1


def compute_perceived_difficulty(vals):
    """
    calculates percieved difficulty
    :param vals: TODO: What is vals?
    :return:
    """
    count = 0
    sum = 0
    for i in range(1, len(vals)):
        sacc_dur = saccade_duration(vals[i][1], vals[i - 1][2])
        sacc_len = saccade_length(vals[i - 1][5], vals[i - 1][6], vals[i][5], vals[i][6])
        perceived_difficulty = 1 / (1 + (sacc_len / sacc_dur))
        count += 1
        sum += perceived_difficulty

    return sum / count


def compute_information_processing_index(list_of_init_times, list_of_end_times, list_of_fx, list_of_fy):
    """
    Takes a list of init and and a list of end-times from a 10 second time window.
    Take the 25 percentile for the short (fixation duration/saccade length) and 75
    percentile for long (fixation duration/saccade length). Preferred window size
    is 10 seconds.
    """

    assert type(list_of_init_times) == type(list_of_end_times) == list
    assert len(list_of_init_times) == len(list_of_end_times) == len(list_of_fx) == len(list_of_fy)
    div = []
    for i in range(min(len(list_of_init_times), len(list_of_end_times)) - 1):
        current_fixation_duration = fixation_duration(list_of_init_times[i], list_of_end_times[i])
        current_saccade_length = saccade_length(list_of_fx[i], list_of_fy[i], list_of_fx[i + 1], list_of_fy[i + 1])
        div.append(current_fixation_duration / current_saccade_length)

    short_treshold = np.percentile(np.asarray(div), 25)
    long_treshold = np.percentile(np.asarray(div), 75)

    return np.sum(np.asarray(div) < short_treshold) / np.sum(np.asarray(div) > long_treshold)
