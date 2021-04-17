from crunch.skeleton.measurements.helpers import norm_by_array


def amount_of_motion(n):
    """Take norm of two points and
    averageing, before summing them up
    :param n: Datapoints
    :type n: list
    :return total: Total amount of motion
    :type total: float
    """
    total_joints = 24
    total = 0
    joint_Total = 0
    for j in range(len(n[0])):
        joint_Total += norm_by_array(n[0][j], n[1][j])
        total += joint_Total / total_joints
    return round(total, 6)
