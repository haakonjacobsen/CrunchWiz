from .helpers import norm_by_array, get_joint_by_index


def most_used_joints(t0, t1, list):
    """ Putting the norm in a list such that
    list[0] = joint 0, list[1 = joint 1 etc.  """
    for i in range(25):
        list[i] += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return list
