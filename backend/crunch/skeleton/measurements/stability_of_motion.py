from crunch.skeleton.measurements.helpers import norm_by_array


def stability_of_motion(n):
    """Take norm of two points before applying
    a formula, and summing them up
    :param n: Datapoints
    :type n: list of 2d tuples
    :return total: List of stability
    :type stabilityList: list
    """
    stability = 0
    total_joints = 24
    joint_distance = 0
    for j in range(len(n[0])):
        euclid = norm_by_array(n[0][j], n[1][j])
        joint_distance += 1 / (1 + euclid)
        stability += joint_distance
    return round(stability, 6)
