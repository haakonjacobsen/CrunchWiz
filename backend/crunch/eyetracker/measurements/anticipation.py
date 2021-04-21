def saccade_duration(start_time, end_time):
    """
    Finds the duration of a saccade

    :param start_time: start of the saccade/fixation
    :type start_time: int
    :param end_time: end of the saccade/fixation
    :type end_time: int
    :return: duration of the saccade
    :rtype: int
    """
    return end_time - start_time


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
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def average_speed(initTime, endTime, fx, fy):
    """
    The average speed of the data points in the window

    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :return: The average speed between all the fixation points
    :rtype: float
    """
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
    """
    Find the variance of the fixation points

    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :param avg_speed: the average speed between the fixation points
    :type avg_speed: float
    :return: The variance between all the fixation points
    :rtype: float
    """
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
    """
    Computes anticipation based on the formula described in our report

    :param initTime: the start times of the saccade/fixation point
    :type initTime: list of int
    :param endTime: the end times of the saccade/fixation point
    :type endTime: list of int
    :param fx: the x positions in each saccade/fixation point
    :type fx: list of int
    :param fy: the y positions in each saccade/fixation point
    :type fy: list of int
    :return: The anticipation based on the data points
    :rtype: float
    """
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
