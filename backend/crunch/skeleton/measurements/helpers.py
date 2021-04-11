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
    t = sym.symbols("t")
    h = 0.25
    t0 = tstart
    t1 = tstart + h
    t2 = t1 + h
    t3 = t2 + h
    t4 = tend
    diff = (
        round(-0.5 * f.subs(t, t0), 4)
        + round(f.subs(t, t1), 4)
        - round(f.subs(t, t3), 4)
        + round(0.5 * f.subs(t, t4), 4)
    )
    deff = h ** 3
    return diff / deff
