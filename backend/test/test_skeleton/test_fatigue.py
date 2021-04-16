# flake8: noqa
from crunch.skeleton.measurements.fatigue import fatigue
import numpy as np


tol = 1e-6


def test_fatigue():
    test_array = [[(3, 2)], [(7, -4)]]
    estimated = fatigue(test_array)
    exact0 = 17.3333333
    assert np.abs(round(estimated, 6) - exact0) < tol
