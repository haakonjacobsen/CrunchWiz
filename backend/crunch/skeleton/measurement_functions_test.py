import pandas as pd
import numpy as np
import sympy as sym

import measurement_functions as mf

tol = 1e-14
t = sym.symbols("t")


def get_joint_by_index_test():
    pass


def norm_by_array_test():
    a = [1, 2, 3]
    b = [3, 2, 1]
    estimate = mf.norm_by_array(a, b)
    exact = 2.8284
    if np.abs(np.round(estimate, 4) - exact) < tol:
        print("Within accepted threshold")
    else:
        print("Not within threshold")


def func_test():
    a = [2, 4, 6]
    b = [1, 3, 5]
    x, y, z = mf.func(a, b)
    # t = 2 gives 0
    x_exact = 0
    # t = 4 gives 0
    y_exact = 0
    # t = 6 gives 0
    z_exact = 0

    if np.abs(x.subs(t, 2)) - x_exact < tol:
        print("Within accepted threshold")
    else:
        print("Not within threshold")

    if np.abs(y.subs(t, 4)) - y_exact < tol:
        print("Within accepted threshold")
    else:
        print("Not within threshold")

    if np.abs(z.subs(t, 6)) - z_exact < tol:
        print("Within accepted threshold")
    else:
        print("Not within threshold")


func_test()


def finiteDiff_test():
    pass


def fatigue_test():
    pass


def amount_of_motion_test():
    pass


def most_used_joints_test():
    pass


def stability_of_motion_test():
    pass
