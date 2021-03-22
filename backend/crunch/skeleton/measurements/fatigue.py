import numpy as np
from .helpers import finite_diff, get_joint_by_index
import sympy as sym


def fatigue(t0, t1):
    """ Measures fatigue for every joint
    by finding their functions, and applying
    finite differences """
    totalFatigue = 0
    totalJoint = 24
    for i in range(25):
        jointFatigue = 0
        x, y, z = func(get_joint_by_index(t0, i), get_joint_by_index(t1, i))
        # we apply absolute value since we are interested in positive movement
        jointFatigue += np.abs(finite_diff(x, t0, t1))
        jointFatigue += np.abs(finite_diff(y, t0, t1))
        jointFatigue += np.abs(finite_diff(z, t0, t1))
        totalFatigue += jointFatigue / totalJoint
    return totalFatigue


def func(a, b):
    """Takes two point, and makes a direction vector,
    then using said vector to calculate three
    equations responsible for x,y,z.
    Since they are dynamic, we use sympy
    to create the mathematical expressions"""
    t = sym.symbols("t")
    vector = [
        b[0] - a[0],
        b[1] - a[1],
        b[2] - a[2],
        ]
    x = a[0] + (vector[0]) * t
    y = a[1] + (vector[1]) * t
    z = a[2] + (vector[2]) * t
    return x, y, z

