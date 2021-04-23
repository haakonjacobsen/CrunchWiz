from crunch.skeleton.measurements.helpers import norm_by_array


def amount_of_motion(pos):
    """
    Find the total amount of distance travelled by each join

    :param pos: positions of each joint
    :type pos: list of list of tuples
    :return: amount of motion
    :rtype: float
    """
    total_joints = 24
    total = 0
    joint_Total = 0
    for j in range(len(pos[0])):
        joint_Total += norm_by_array(pos[0][j], pos[1][j])
        total += joint_Total / total_joints
    return float(total)
