import numpy as np
import pytest

from crunch.eyetracker.measurements import (compute_anticipation,
                                            compute_cognitive_load,
                                            compute_ipi,
                                            compute_perceived_difficulty,
                                            compute_thresholds)


@pytest.fixture(scope="module")
def fixation_fixture():
    init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967, 3447]
    end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142, 3675]
    fy = [720, 672, 653, 599, 621, 664, 566, 636, 652, 792, 810, 663]
    fx = [1054, 1166, 1087, 1052, 1048, 1069, 717, 856, 821, 527, 559, 938]

    return {"initTime": init, "endTime": end, "fx": fx, "fy": fy}


@pytest.fixture(scope="module")
def gaze_fixture():
    lpup = list(np.random.rand(500) * 2 + 4)
    rpup = list(np.random.rand(500) * 2 + 4)
    return {"lpup": lpup, "rpup": rpup}


def test_compute_information_processing_index(fixation_fixture):
    short, long = compute_thresholds(**fixation_fixture)
    assert compute_ipi(**fixation_fixture, short_threshold=short, long_threshold=long) > 0


def test_compute_anticipation(fixation_fixture):
    assert compute_anticipation(**fixation_fixture) in ["low", "medium", "high"]


def test_compute_cognitive_load(gaze_fixture):
    assert compute_cognitive_load(**gaze_fixture) > 0


def test_compute_perceived_difficulty(fixation_fixture):
    assert compute_perceived_difficulty(**fixation_fixture) > 0
