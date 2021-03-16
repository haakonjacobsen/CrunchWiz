from backend.crunch.eyetracker.measurement_functions import compute_information_processing_index


class TestCrunch:
    def test_crunch(self):
        assert (True)

    def test_compute_information_processing_index(self):
        init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967]
        end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142]
        assert compute_information_processing_index(init, end) > 0
