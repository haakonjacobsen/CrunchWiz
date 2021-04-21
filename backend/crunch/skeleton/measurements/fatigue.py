import numpy as np
import sympy as sym

from crunch.skeleton.measurements.helpers import finite_diff


def fatigue(n):
    """Measures fatigue for every joint
    by finding their functions, and applying
    finite differences
    :param n: Datapoints
    :type n: list of 2d tuples
    :return totalFatigue: Total fatigue
    :type totalFatigue: float
    :return fatigeArray: List of fatigue
    :type fatigeArray: list
    """
    total_joints = 24
    joint_fatigue = 0.0
    for i in range(len(n) - 1):
        joint_fatigue = 0.0
        for j in range(len(n[i])):
            if n[i][j] == (0.0, 0.0) or n[i + 1][j] == (0.0, 0.0):
                continue
            f = equation(n[i][j], n[i + 1][j])
            joint_fatigue += np.abs(finite_diff(f, i, i + 1))
    frameFatigue = joint_fatigue / total_joints
    return round(frameFatigue, 6)


def equation(x, y):
    """A helper function to calculate
    the equation given two points
    :param x: Datapoints for x
    :type x: list
    :param y: Datapoints for y
    :type y: list
    :return x: equation for x with respect to t
    :type sympy: equation
    :return x: equation for x with respect to t
    :type sympy: equation
    """
    t = sym.symbols("t")
    x1, y1 = x[0], x[1]
    x2, y2 = y[0], y[1]
    m = (y2 - y1) / (x2 - x1)
    f = m * (t - x1) + y1
    return f
