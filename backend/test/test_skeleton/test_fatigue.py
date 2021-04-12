# flake8: noqa
from crunch.skeleton.measurements.fatigue import fatigue
import numpy as np


tol = 1e-6


def test_fatigue():
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
            (699.9767, 674.45215),
        ],
        [
            (670.5192, 137.64388),
            (695.95966, 133.82387),
            (654.8586, 159.18672),
            (713.5559, 149.39342),
        ],
    ]
    estimated = fatigue(test_array)

    exact_total = 0.001712
    exact0 = 0.000320
    exact1 = 0.001712

    assert np.abs(round(estimated[0], 6) - exact_total) < tol
    assert np.abs(round(estimated[1][0], 6) - exact0) < tol
    assert np.abs(round(estimated[1][1], 6) - exact1) < tol
