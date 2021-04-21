# flake8: noqa
import numpy as np

from crunch.skeleton.measurements.most_used_joints import most_used_joints

tol = 1e-5


def test_most_used_joints():
    test_array = [
        [
            (682.33496, 147.34991),
            (682.3375, 221.9163),
            (633.3446, 219.936),
            (590.20074, 288.53638),
        ],
        [
            (713.6236, 374.71902),
            (680.24756, 382.5819),
            (695.9468, 515.76013),
            (500.9767, 500.45215),
        ],
        [
            (13.5559, 49.39342),
            (70.5192, 37.64388),
            (534.8586, 593.18672),
            (5.95966, 3.82387),
        ],
    ]
    exact0_joint = 2
    exact0_number = 38.4375
    exact1_joint = 0
    exact1_number = 98.017995
    estimated = most_used_joints(test_array)

    assert estimated[0][0] == exact0_joint
    assert np.abs(round(estimated[0][1], 4) - exact0_number) < tol
    assert estimated[1][0] == exact1_joint
    assert np.abs(round(estimated[1][1], 4) - exact1_number) < tol
