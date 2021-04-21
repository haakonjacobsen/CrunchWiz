def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


def saccade_length(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def average_speed(initTime, endTime, fx, fy):
    count = 0
    speed_sum = 0
    for i in range(1, len(initTime)):
        sacc_dur = saccade_duration(initTime[i], endTime[i - 1])
        sacc_len = saccade_length(
            fx[i - 1],
            fy[i - 1],
            fx[i],
            fy[i],
        )
        sacc_speed = sacc_len / sacc_dur
        speed_sum += sacc_speed
        count += 1
    return speed_sum / count


def variance(initTime, endTime, fx, fy, avg_speed):
    sum_square_difference = 0
    count = 0
    for i in range(1, len(initTime)):
        sacc_dur = saccade_duration(initTime[i], endTime[i - 1])
        sacc_len = saccade_length(
            fx[i - 1],
            fy[i - 1],
            fx[i],
            fy[i],
        )
        sacc_speed = sacc_len / sacc_dur
        sum_square_difference += (sacc_speed - avg_speed) ** 2
        count += 1
    return sum_square_difference / (count - 1)


def compute_anticipation(initTime, endTime, fx, fy):
    avg_speed = average_speed(initTime, endTime, fx, fy)
    var = variance(initTime, endTime, fx, fy, avg_speed)
    count = 0
    sum_cube_difference = 0
    for i in range(1, len(initTime)):
        sacc_dur = saccade_duration(initTime[i], endTime[i - 1])
        sacc_len = saccade_length(
            fx[i - 1],
            fy[i - 1],
            fx[i],
            fy[i],
        )
        sacc_speed = sacc_len / sacc_dur
        sum_cube_difference += (sacc_speed - avg_speed) ** 3
        count += 1
    return sum_cube_difference / ((count - 1) * (var ** 0.5) ** 3)
