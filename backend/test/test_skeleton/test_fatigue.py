# flake8: noqa
from crunch.skeleton.measurements.fatigue import fatigue
import numpy as np


tol = 1e-6


def test_fatigue():
    test_array = [
        [
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
            (1, 2),
        ],
        [
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
            (3, 4),
        ],
    ]
    estimated = fatigue(test_array)
    exact0 = 200
    print(estimated)
    assert np.abs(round(estimated, 6) - exact0) < tol
