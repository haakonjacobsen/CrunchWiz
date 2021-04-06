from crunch.eyetracker.measurements import (compute_ipi,
                                            compute_baseline)


class TestCrunch:
    def test_crunch(self):
        assert (True)

    def test_compute_information_processing_index(self):
        init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967, 3447]
        end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142, 3675]
        fy = [720, 672, 653, 599, 621, 664, 566, 636, 652, 792, 810, 663]
        fx = [1054, 1166, 1087, 1052, 1048, 1069, 717, 856, 821, 527, 559, 938]
        short, long = compute_baseline(init, end, fx, fy)
        assert compute_ipi(init, end, fx, fy, short, long) == 1
