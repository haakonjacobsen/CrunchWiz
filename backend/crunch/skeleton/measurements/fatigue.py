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
    fatigeArray = []
    totalFatigue = 0.0
    totalJoint = 24
    t = sym.symbols("t")
    for i in range(len(n) - 1):
        jointFatigue = 0
        for j in range(len(n[i])):
            f, g = equation(n[i][j], n[i + 1][j])
            jointFatigue += np.abs(finite_diff(f, i, i + 1))
            jointFatigue += np.abs(finite_diff(g, i, i + 1))
        totalFatigue += jointFatigue / totalJoint
        fatigeArray.append(totalFatigue)
    return totalFatigue, fatigeArray


def equation(x, y):
    x1 = float(x[0])
    y1 = float(x[1])
    x2 = float(y[0])
    y2 = float(y[1])
    t = sym.symbols("t")
    vector = [x2 - x1, y2 - y1]
    x = x1 + (vector[0]) * t
    y = y1 + (vector[1]) * t
    return x, y
