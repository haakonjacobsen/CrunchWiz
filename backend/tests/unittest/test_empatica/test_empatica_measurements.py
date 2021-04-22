# flake8: noqa
import os

import pandas as pd
import pytest

from crunch.empatica.measurements import (compute_arousal,
                                          compute_emotional_regulation,
                                          compute_engagement,
                                          compute_entertainment,
                                          compute_stress)


@pytest.fixture(scope="module")
def empatica_fixture():
    def _empatica_fixture_factory(n, m, name):
        data = pd.read_csv(os.path.join(os.path.dirname(__file__), "mock_data/" + name + ".csv"))[name]
        return [data[i] for i in range(n, m)]

    return _empatica_fixture_factory


@pytest.mark.parametrize('index', range(0, 40, 10))
def test_arousal(empatica_fixture, index):
    data = empatica_fixture(index, index + 10, "EDA")
    measurement = compute_arousal(data)

    assert type(measurement) == float and measurement > 0


@pytest.mark.parametrize('index', range(0, 40, 10))
def test_stress(empatica_fixture, index):
    data = empatica_fixture(index, index + 10, "TEMP")
    measurement = compute_stress(data)

    assert type(measurement) == float


@pytest.mark.parametrize('index', range(0, 242, 121))
def test_engagement(empatica_fixture, index):
    data = empatica_fixture(index, index + 121, "EDA")
    measurement = compute_engagement(data)

    assert type(float(sum(measurement))) == float


@pytest.mark.parametrize('index', range(0, 40, 10))
def test_entertainment(empatica_fixture, index):
    data = empatica_fixture(index, index + 10, "EDA")
    measurement = compute_entertainment(data)

    assert type(float(sum(measurement))) == float


@pytest.mark.parametrize('index', range(0, 48, 12))
def test_emotional_regulation(empatica_fixture, index):
    data = empatica_fixture(index, index + 12, "EDA")
    measurement = compute_emotional_regulation(data)

    assert type(float(sum(measurement))) == float
