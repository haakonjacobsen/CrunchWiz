# from backend.crunch.eyetracker.handler import DataHandler
from crunch.eyetracker.measurements.information_processing_index import compute_information_processing_index
from crunch.eyetracker.measurements.information_processing_index import compute_ipi_thresholds
from crunch.eyetracker.measurements.anticipation import compute_anticipation
from crunch.eyetracker.measurements.perceived_difficulty import compute_perceived_difficulty
from crunch.eyetracker.measurements.information_processing_index import compute_ipi_thresholds
from crunch.eyetracker.handler import DataHandler, IpiHandler
from crunch.eyetracker.api import EyetrackerAPI, GazedataToFixationdata


class TestCrunch:
    init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967, 3447]
    end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142, 3675]
    fy = [720, 672, 653, 599, 621, 664, 566, 636, 652, 792, 810, 663]
    fx = [1054, 1166, 1087, 1052, 1048, 1069, 717, 856, 821, 527, 559, 938]

    def test_compute_information_processing_index(self):
        short, long = compute_ipi_thresholds(self.init, self.end, self.fx, self.fy)
        assert compute_information_processing_index(self.init, self.end, self.fx, self.fy, short, long) > 0

    def test_compute_anticipation(self):
        assert compute_anticipation(self.init, self.end, self.fx, self.fy) > 0

    def test_compute_perceived_difficulty(self):
        assert compute_perceived_difficulty(self.init, self.end, self.fx, self.fy) > 0

    def test_DataHandler(self):
        handler = DataHandler(compute_anticipation, "anticipation.csv", ["initTime", "endTime", "fx", "fy"])
        for i in range(1, 20):
            handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
            assert len(handler.list_of_baseline_values) == i
        # transition from baseline phase to csv phase
        assert handler.phase_func == handler.baseline_phase
        handler.baseline_end_time -= 120
        handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
        assert handler.phase_func == handler.csv_phase
        try:
            # should throw File not found error
            handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
            assert False
        except OSError as e:
            assert True

    def test_IpiHandler(self):
        handler = IpiHandler()
        for i in range(1, 20):
            handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
            assert len(handler.dict_of_lists_of_threshold_values["initTime"]) == 12 * i
        # transition from threshold phase to baseline phase
        assert handler.phase_func == handler.threshold_phase
        handler.threshold_phase_end -= 120
        handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
        assert handler.phase_func == handler.baseline_phase

        # transition from baseline phase to csv phase
        for i in range(1, 20):
            handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
            assert len(handler.list_of_baseline_values) == i

        handler.baseline_end_time -= 120
        handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
        assert handler.phase_func == handler.csv_phase
        try:
            # should throw File not found error
            handler.send_data_window({"initTime": self.init, "endTime": self.end, "fx": self.fx, "fy": self.fy})
            assert False
        except OSError as e:
            assert True

