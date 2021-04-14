import numpy as np
from crunch.skeleton.measurements.helpers import finite_diff
import sympy as sym


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
    total_Joint = 24
    for i in range(len(n) - 1):
        joint_Fatigue = 0.0
        for j in range(len(n[i])):
            f, g = equation(n[i][j], n[i + 1][j])
            joint_Fatigue += np.abs(finite_diff(f, i, i + 1))
            joint_Fatigue += np.abs(finite_diff(g, i, i + 1))
    frameFatigue = joint_Fatigue / total_Joint
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
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]
    vector = [x2 - x1, y2 - y1]
    x = x1 + (vector[0]) * t
    y = y1 + (vector[1]) * t
    return x, y
