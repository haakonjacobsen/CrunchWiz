from .helpers import norm_by_array, get_joint_by_index


def stability_of_motion(t0, t1):
    """ Take norm of two points before applying
    a formula, and summing them up """
    total_distance = 0
    for i in range(25):
        euclid = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total_distance += 1 / (1 + euclid)
    return total_distance


