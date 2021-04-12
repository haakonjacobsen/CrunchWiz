# flake8: noqa
from crunch.skeleton.measurements.amount_of_motion import amount_of_motion
import numpy as np
import sympy as sym

tol = 1e-5


def test_amount_of_motion():
    test_array = [[(4, 6)], [(5, 7)], [(1, 3)]]
    estimated = amount_of_motion(test_array)
    assert len(estimated) == 2
    exact0 = 0.0589
    exact1 = 0.2357
    assert np.abs(round(estimated[0], 4) - exact0) < tol
    assert np.abs(round(estimated[1], 4) - exact1) < tol
