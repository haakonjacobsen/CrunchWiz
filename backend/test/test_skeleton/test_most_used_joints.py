# flake8: noqa
import numpy as np

from crunch.skeleton.measurements.most_used_joints import most_used_joints
from skeleton_util import get_n_skeleton_points


tol = 1e-5


def test_most_used_joints():
    test_array = get_n_skeleton_points(2)
    exact0_joint = "LSmallToe"
    estimated = most_used_joints(test_array)

    assert estimated == exact0_joint
