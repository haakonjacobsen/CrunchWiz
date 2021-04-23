from crunch.skeleton.measurements.helpers import norm_by_array


def stability_of_motion(pos):
    """Take norm of two points before applying
    a formula, and summing them up

    :param pos: positions of each joint
    :type pos: list of list of tuples
    :return: stability of motion
    :rtype: float
    """
    stability = 0
    joint_distance = 0
    for j in range(len(pos[0])):
        euclid = norm_by_array(pos[0][j], pos[1][j])
        joint_distance += 1 / (1 + euclid)
        stability += joint_distance
    return float(stability)
