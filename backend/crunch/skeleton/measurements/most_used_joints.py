from .helpers import norm_by_array, get_joint_by_index


def most_used_joints(t0, t1, list):
    """ Putting the norm in a list such that
    list[0] = joint 0, list[1] = joint 1 etc.
    Parameters:
        t0 (int): Start time
        t1 (int): End time
        list (list): List requires a list to append values to i.e [0] * 25
    Returns:
        list (list): The inputted array with used joints appended
    """
    for i in range(25):
        list[i] += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return list
