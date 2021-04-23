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
    for i in range(len(pos)-1):
        for j in range(len(pos[0])):
            euclid = norm_by_array(pos[i][j], pos[i+1][j])
            stability += 1 / (1 + euclid)
    return float(stability/len(pos[0]))
