import os

import pandas as pd
import pytest

from crunch.skeleton.handler import DataHandler


@pytest.fixture(scope="module")
def skeleton_fixture():
    skeleton_data = []
    df = pd.pandas.read_csv(os.path.join(os.path.dirname(__file__), "../../mock_data/skeleton.csv"), header=None)
    row = df.iloc[0].tolist()
    for j in range(0, len(row) - 1, 2):
        skeleton_data.append((float(row[j].strip().strip("[]()")), float(row[j + 1].strip().strip("[]()"))))
    return skeleton_data


@pytest.mark.parametrize('window, baseline', [(2, 2), (2, 3), (5, 5), (2, 10)])
def test_skeleton_handler(skeleton_fixture, window, baseline):
    """ Test that the handler uses data points for baseline
    until it has received enough, and the use them for measurement """
    handler = DataHandler(
        measurement_func=lambda *args: 1,
        window_length=window,
        window_step=window,
        baseline_length=baseline
    )
    for i in range(window*baseline):
        assert handler.baseline == 0
        assert handler.phase_func == handler.baseline_phase
        handler.add_data_point(skeleton_fixture)

    assert handler.baseline != 0
    assert handler.phase_func == handler.csv_phase
