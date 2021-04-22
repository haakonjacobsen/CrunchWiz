import pytest

from crunch.skeleton.api import RealAPI


class DatumMock:
    poseKeypoints = [[(i, i + 1) for i in range(25)]]


class MockSubscriber:
    """ Mock subscriber to test that we receive data points from the api """
    nr_points_received = 0

    def add_data_point(self, _):
        self.nr_points_received += 1


@pytest.mark.parametrize('expected', [1, 5, 10, 50])
def test_skeleton_api(expected):
    """ Test that the api sends the gaze data that it receives to its subscribers """
    mock_subscriber = MockSubscriber()
    api = RealAPI()
    api.add_subscriber(mock_subscriber, "body")
    for i in range(expected):
        datum = DatumMock()
        api.add_datapoint([datum])

    assert mock_subscriber.nr_points_received == expected
