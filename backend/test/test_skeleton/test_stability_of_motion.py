# flake8: noqa
from crunch.skeleton.measurements.stability_of_motion import stability_of_motion
import numpy as np

tol = 1e-5


def test_stability_of_motion():
    test_array = [[(4, 6), (1, 4)], [(5, 7), (2, 5)]]
    test_array2 = [[(6, 7), (8, 12)], [(7, 2), (6, 2)]]
    estimated = stability_of_motion(test_array)
    estimated2 = stability_of_motion(test_array2)
    exact0 = 1.242641
    exact1 = 0.417223
    assert np.abs(round(estimated, 6) - exact0) < tol
    assert np.abs(round(estimated2, 6) - exact1) < tol
 