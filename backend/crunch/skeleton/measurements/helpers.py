import numpy as np


def norm_by_array(a, b):
    """
    Calculating the L2 norm of two given lists

    :param a: x and y coordinates of joints (previous position)
    :type a: list of tuples
    :param b: x and y coordinates of joints (current position)
    :type b: list of tuples
    :return: L2 norm
    :rtype: float
    """
    x1 = float(a[0])
    y1 = float(a[1])
    x2 = float(b[0])
    y2 = float(b[1])
    norm_x = (x1 - x2) ** 2
    norm_y = (y1 - y2) ** 2
    return np.sqrt(norm_x + norm_y)
