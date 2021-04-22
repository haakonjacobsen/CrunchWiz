import pytest

from crunch.empatica.api import RealAPI
import random


class MockSubscriber:
    """ Mock subscriber to test that we receive data points from the api """
    nr_points_received = 0

    def add_data_point(self, _):
        self.nr_points_received += 1


@pytest.fixture(scope="module")
def wristband_fixture():
    return random.random()


@pytest.mark.parametrize('expected, type', [(1, "HR"), (5, "IBI"), (10, "EDA"), (50, "TEMP")])
def test_empatica_api(expected, type):
    """ Test that the api sends the gaze data that it receives to its subscribers """
    mock_subscriber = MockSubscriber()
    api = RealAPI()
    api.add_subscriber(mock_subscriber, type)
    for i in range(expected):
        api._send_data_to_subscriber(type, wristband_fixture)

    assert mock_subscriber.nr_points_received == expected
