from .helpers import norm_by_array, array


def amount_of_motion(n):
    """Take norm of two points and
    averageing, before summing them up
    :param n: Datapoints
    :type n: list
    :return total: List of motions
    :type motionList: list
    """
    total_joints = 24
    total = 0
    motionList = []
    for i in range(len(n) - 1):
        total = 0
        jointTotal = 0
        for j in range(len(n[i])):
            jointTotal += norm_by_array(n[i][j], n[i + 1][j])
        total += jointTotal / total_joints
        motionList.append(total)
    return motionList
