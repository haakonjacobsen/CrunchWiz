import numpy as np

from crunch.eyetracker.measurements.anticipation import compute_anticipation
from crunch.eyetracker.measurements.cognitive_load import \
    compute_cognitive_load
from crunch.eyetracker.measurements.information_processing_index import (compute_information_processing_index,
                                                                         compute_ipi_thresholds)
from crunch.eyetracker.measurements.perceived_difficulty import \
    compute_perceived_difficulty


class TestCrunch:
    init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967, 3447]
    end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142, 3675]
    fy = [720, 672, 653, 599, 621, 664, 566, 636, 652, 792, 810, 663]
    fx = [1054, 1166, 1087, 1052, 1048, 1069, 717, 856, 821, 527, 559, 938]

    def test_compute_information_processing_index(self):
        short, long = compute_ipi_thresholds(self.init, self.end, self.fx, self.fy)
        assert compute_information_processing_index(self.init, self.end, self.fx, self.fy, short, long) > 0

    def test_compute_anticipation(self):
        assert True
        # TODO: Change to assert medium/low/high wehen anticipation measurement changes is merged
        # assert compute_anticipation(self.init, self.end, self.fx, self.fy) > 0

    def test_compute_perceived_difficulty(self):
        assert compute_perceived_difficulty(self.init, self.end, self.fx, self.fy) > 0

    def test_compute_cognitive_load(self):
        pup = list(np.random.rand(500) * 2 + 4)
        initTime = list(np.arange(0, 20000, 40))
        endTime = list(np.arange(0, 20000, 40) + 10)
        assert compute_cognitive_load(initTime, endTime, pup, pup) > 0
