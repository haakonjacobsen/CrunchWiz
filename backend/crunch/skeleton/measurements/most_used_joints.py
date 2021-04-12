from crunch.skeleton.measurements.helpers import norm_by_array


def most_used_joints(n):
    """Calculating the norms. And check for the highest
    value to output the according used joint.
    :param n: Datapoints
    :type n: list of 2d tuples
    :return usedList: List of most used joint, and its value
    :type usedList: list of tuple (jointNr, value)
    """
    usedList = []
    for i in range(len(n) - 1):
        jointNr = 0
        highest = 0
        total = 0
        for j in range(len(n[i])):
            used = norm_by_array(n[i][j], n[i + 1][j])
            if highest <= used:
                highest = used
                jointNr = j
            total += used
        total = total / 24
        usedList.append((jointNr, round(total, 6)))
    return usedList
