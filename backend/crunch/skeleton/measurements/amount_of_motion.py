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
    jointTotal = 0
    for j in range(total_joints):
        jointTotal += norm_by_array(n[0][j], n[1][j])
        total += jointTotal / total_joints
    return round(total, 6)
