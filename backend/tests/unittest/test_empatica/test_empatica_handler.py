import random

import pytest

from crunch.empatica.handler import DataHandler


@pytest.fixture(scope="module")
def wristband_fixture():
    return random.random()


@pytest.mark.parametrize('window, baseline', [(2, 2), (2, 3), (5, 5), (2, 10)])
def test_empatica_handler(wristband_fixture, window, baseline):
    """ Test that the handler uses data points for baseline
    until it has received enough, and the use them for measurement """
    handler = DataHandler(
        measurement_func=lambda *args: 1,
        window_length=window,
        window_step=window,
        baseline_length=baseline
    )
    for i in range(baseline):
        assert handler.baseline is None or type(handler.baseline) == list
        assert handler._handle_datapoint == handler._calculate_baseline
        handler.add_data_point(wristband_fixture)

    assert handler.baseline != 0
    assert handler._handle_datapoint == handler._calculate_measurement
