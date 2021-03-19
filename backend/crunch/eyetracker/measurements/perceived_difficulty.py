def compute_perceived_difficulty(vals):
    """
    calculates percieved difficulty
    :param vals: TODO: What is vals?
    :return:
    """
    count = 0
    sum = 0
    for i in range(1, len(vals)):
        sacc_dur = saccade_duration(vals[i][1], vals[i-1][2])
        sacc_len = saccade_length(vals[i-1][5], vals[i-1][6], vals[i][5], vals[i][6])
        perceived_difficulty = 1/(1+(sacc_len / sacc_dur))
        count += 1
        sum += perceived_difficulty

    return sum/count


def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
