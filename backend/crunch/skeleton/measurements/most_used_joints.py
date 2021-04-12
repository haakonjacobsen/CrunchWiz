from crunch.skeleton.measurements.helpers import norm_by_array


def most_used_joints(n):
    """Calculating the norms. And check for the highest
    value to output the according used joint.
    :param n: Datapoints
    :type n: list of 2d tuples
    :return used_List: List of most used joint, and its value
    :type used_List: list of tuple (joint_Nr, value)
    """
    used_List = []
    for i in range(len(n) - 1):
        joint_Nr = 0
        highest = 0
        total = 0
        for j in range(len(n[i])):
            used = norm_by_array(n[i][j], n[i + 1][j])
            if highest <= used:
                highest = used
                joint_Nr = j
            total += used
        total = total / 24
        used_List.append((joint_Nr, round(total, 6)))
    return used_List
