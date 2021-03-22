from .helpers import norm_by_array, get_joint_by_index


def amount_of_motion(t0, t1):
    """ Take norm of two points and
    averageing, before summing them up
    Parameters:
        t0 (int): Start time
        t1 (int): End time
    Returns:
        total (float): Total motion for given interval
    """
    total_joints = 24
    total = 0
    for i in range(25):
        jointTotal = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total += jointTotal / total_joints
    return total
