
def compute_perceived_difficulty(initTime, endTime, fx, fy):
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


""" Test Values
initTime = [309,467,809,1308,1609]
endTime = [399,539,1219,1499,1701]
fx = [1166,1087,1052,1048,1069]
fy = [672,653,599,621,664]
"""
