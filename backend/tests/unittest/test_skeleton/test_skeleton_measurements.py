# flake8: noqa
import os

import pandas as pd
import pytest

from crunch.skeleton.measurements import (amount_of_motion, fatigue,
                                          most_used_joints,
                                          stability_of_motion)


@pytest.fixture(scope="module")
def skeleton_fixture():
    def _skeleton_fixture_factory(n, m):
        skeleton_data = []
        df = pd.pandas.read_csv(os.path.join(os.path.dirname(__file__), "mock_data/test_data.csv"), header=None)
        n = min(n, len(df))
        for i in range(n, m):
            temp_array = []
            row = df.iloc[i].tolist()
            for j in range(0, len(row) - 1, 2):
                temp_array.append((float(row[j].strip().strip("[]()")), float(row[j + 1].strip().strip("[]()"))))
            skeleton_data.append(temp_array)
        return skeleton_data

    return _skeleton_fixture_factory


@pytest.mark.parametrize('index', range(0, 10))
def test_amount_of_motion(skeleton_fixture, index):
    test_array = skeleton_fixture(index, index + 2)
    measurement = amount_of_motion(test_array)

    assert type(measurement) == float and measurement > 0


@pytest.mark.parametrize('index', range(0, 10))
def test_stability_of_motion(skeleton_fixture, index):
    test_array = skeleton_fixture(index, index + 2)
    measurement = stability_of_motion(test_array)

    assert type(measurement) == float and measurement > 0


@pytest.mark.parametrize('index', range(0, 10))
def test_fatigue(skeleton_fixture, index):
    test_array = skeleton_fixture(index, index + 2)
    print(skeleton_fixture(index, index + 2))
    measurement = fatigue(test_array)

    assert type(measurement) == float and measurement > 0


@pytest.mark.parametrize('index', range(0, 10))
def test_most_used_joints(skeleton_fixture, index):
    test_array = skeleton_fixture(index, index + 2)
    measurement = most_used_joints(test_array)

    joint_map = ["Nose",
                 "Neck",
                 "RShoulder",
                 "RElbow",
                 "RWrist",
                 "LShoulder",
                 "LElbow",
                 "LWrist",
                 "MidHip",
                 "RHip",
                 "RKnee",
                 "RAnkle",
                 "LHip",
                 "LKnee",
                 "LAnkle",
                 "REye",
                 "LEye",
                 "REar",
                 "LEar",
                 "LBigToe",
                 "LSmallToe",
                 "LHeel",
                 "RBigToe",
                 "RSmallToe",
                 "RHeel"]
    assert measurement in joint_map
