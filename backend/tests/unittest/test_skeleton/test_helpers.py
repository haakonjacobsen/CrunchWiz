# flake8: noqa
import numpy as np
import sympy as sym

from crunch.skeleton.measurements.fatigue import finite_diff
from crunch.skeleton.measurements.helpers import norm_by_array

tol = 1e-5
t = sym.symbols("t")


def test_norm_by_array():
    a = [1, 2, 3]
    b = [3, 2, 1]
    estimate = norm_by_array(a, b)
    exact = 2.0
    assert np.abs(round(estimate, 4) - exact) < tol


def test_finite_diff():
    eq = t + 1
    assert finite_diff(eq, 1, 2) - 128 < tol
