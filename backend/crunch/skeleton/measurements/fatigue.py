import numpy as np
import sympy as sym


def fatigue(pos):
    """
    Measures fatigue for every joint by using finite differences

    :param pos: positions of each joint
    :type pos: list of list of tuple
    :return: total fatigue
    :rtype: float
    """
    total_joint = 24
    joint_fatigue = 0.0
    for i in range(len(pos) - 1):
        for j in range(len(pos[i])):
            x1, x2 = pos[i][j]
            y1, y2 = pos[i+1][j]
            if x1 - x2 == 0 or y1-y2 == 0:
                continue
            f = equation(pos[i][j], pos[i + 1][j])
            joint_fatigue += np.abs(finite_diff(f, i, i + 1))
    frame_fatigue = joint_fatigue / total_joint
    return float(frame_fatigue)


def equation(pos1, pos2):
    """
    Creates a symbolic equation

    :param pos1: x and y coordinate for first position
    :type pos1: tuple
    :param pos2: x and y coordinate for second position
    :type pos2: tuple
    :return: symbolic equation with respect to t
    :rtype: equation
    """
    t = sym.symbols("t")
    x1, y1 = pos1[0], pos1[1]
    x2, y2 = pos2[0], pos2[1]
    m = (y2 - y1) / (x2 - x1)
    f = m * (t - x1) + y1
    return f


def finite_diff(f, tstart, tend):
    """
    Uses finite difference of the third
    derivate, of second order to estimate jerk
    error. coefficient is ommited in this calculation
    h is default set to 0.25, since an interval 1 second
    it will get 4 evenly splits

    :param f: function with respect to t
    :type f: equation
    :param tstart: start of interval
    :type tstart: int
    :param tend: end of interval
    :type tend: int
    :return: Estimated jerk
    :rtype: float
    """

    t = sym.symbols("t")
    h = 0.25
    t0 = tstart
    t1 = tstart + h
    t2 = t1 + h
    t3 = t2 + h
    t4 = tend
    numerator = (f.evalf(6, subs={t: t0}) / 2 + f.evalf(6, subs={t: t1})
                 - f.evalf(6, subs={t: t3}) + f.evalf(6, subs={t: t4}) / 2)
    denominator = h ** 3
    diff = numerator / denominator
    return diff
