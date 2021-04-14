# flake8: noqa
from crunch.skeleton.measurements.amount_of_motion import amount_of_motion
import numpy as np

tol = 1e-5


def test_amount_of_motion():
    test_array = [[(4, 6), (1, 4)], [(5, 7), (2, 5)]]
    test_array2 = [[(6, 7), (8, 12)], [(7, 2), (6, 2)]]
    estimated = amount_of_motion(test_array)
    estimated2 = amount_of_motion(test_array2)
    exact = 0.176777
    exact2 = 0.849837
    assert np.abs(round(estimated, 6) - exact) < tol
    assert np.abs(round(estimated2, 6) - exact2) < tol
