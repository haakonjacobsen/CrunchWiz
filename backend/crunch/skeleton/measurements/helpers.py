import numpy as np
import sympy as sym


def norm_by_array(a, b):
    """Calculating the L2 norm of two given lists
    :param a:
    :type a: list with tuples
    :param b:
    :type b: list with tuples
    :return total: L2 norm
    :type total: float
    """
    x1 = float(a[0])
    y1 = float(a[1])
    x2 = float(b[0])
    y2 = float(b[1])
    norm_x = (x1 - x2) ** 2
    norm_y = (y1 - y2) ** 2
    return np.sqrt(norm_x + norm_y)


def finite_diff(f, tstart, tend):
    """Uses finite difference of the third
    derivate, of second order to estimate jerk
    error coefficient is ommited in this calculation
    h is default set to 0.25, since an interval 1 second
    it will get 4 evenly splits
    :param f: function with respect to t
    :type f: sympy
    :param tstart: start of interval
    :type tstart: int
    :param tend: end of interval
    :type tend: int
    :return diff: Estimated jerk
    :type diff: float
    """

    t = sym.symbols("t")
    h = 0.25
    t0 = tstart
    t1 = tstart + h
    t2 = t1 + h
    t3 = t2 + h
    t4 = tend
    numerator = (
        f.evalf(6, subs={t: t0}) / 2
        + f.evalf(6, subs={t: t1})
        - f.evalf(6, subs={t: t3})
        + f.evalf(6, subs={t: t4}) / 2
    )
    denominator = h ** 3
    diff = numerator / denominator
    return diff
