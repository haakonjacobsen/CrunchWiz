from crunch.skeleton.measurements.helpers import norm_by_array


def amount_of_motion(pos):
    """
    Find the total amount of distance travelled by each join

    :param pos: positions of each joint
    :type pos: list of list of tuples
    :return: amount of motion
    :rtype: float
    """
    joint_Total = 0
    for i in range(len(pos)-1):
        for j in range(len(pos[0])):
            joint_Total += norm_by_array(pos[i][j], pos[i+1][j])
    return float(joint_Total/len(pos[0]))
