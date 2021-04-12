# flake8: noqa
from crunch.skeleton.measurements.stability_of_motion import stability_of_motion
import numpy as np

tol = 1e-5


def test_stability_of_motion():
    test_array = [[(4, 6)], [(5, 7)], [(1, 3)]]
    estimated = stability_of_motion(test_array)
    exact0 = 0.4142
    exact1 = 0.1502
    assert np.abs(round(estimated[0], 4) - exact0) < tol
    assert np.abs(round(estimated[1], 4) - exact1) < tol
