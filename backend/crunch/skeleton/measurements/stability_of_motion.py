from .helpers import norm_by_array


def stability_of_motion(n):
    """Take norm of two points before applying
    a formula, and summing them up
    :param n: Datapoints
    :type n: list of 2d tuples
    :return total: List of stability
    :type stabilityList: list
    """
    stabilityList = []
    for i in range(len(n) - 1):
        joint_distance = 0
        for j in range(len(n[i])):
            euclid = norm_by_array(n[i][j], n[i + 1][j])
            joint_distance += 1 / (1 + euclid)
        stabilityList.append(joint_distance)
    return stabilityList
