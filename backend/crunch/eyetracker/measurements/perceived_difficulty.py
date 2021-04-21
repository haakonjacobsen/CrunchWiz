def compute_perceived_difficulty(initTime, endTime, fx, fy):
    """
    Calculates perceived difficulty measurement.

    :param initTime: list of timestamps for start time of each data point
    :type initTime: list

    :param endTime: list of timestamps for end time of each data point
    :type endTime: list

    :param fx: list of x-values
    :type fx: list

    :param fy: list of y-values
    :type fy: list'
    :return: Measure of perceived difficulty
    """
    count = 0
    sum = 0
    for i in range(1, len(initTime)):
        sacc_dur = saccade_duration(initTime[i], endTime[i - 1])
        sacc_len = saccade_length(
            fx[i - 1],
            fy[i - 1],
            fx[i],
            fy[i],
        )
        pd = 1 / (1 + (sacc_len / sacc_dur))
        count += 1
        sum += pd
    return sum / count


def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
