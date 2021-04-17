from crunch.eyetracker.measurements.anticipation import compute_anticipation
from crunch.eyetracker.handler import DataHandler, IpiHandler, CognitiveLoadHandler


class TestCrunch:
    init = [111, 309, 467, 809, 1308, 1609, 1927, 2088, 2267, 2670, 2967, 3447]
    end = [203, 399, 539, 1219, 1499, 1701, 2044, 2239, 2358, 2940, 3142, 3675]
    fy = [720, 672, 653, 599, 621, 664, 566, 636, 652, 792, 810, 663]
    fx = [1054, 1166, 1087, 1052, 1048, 1069, 717, 856, 821, 527, 559, 938]
    lpup = [5.865643312591299, 5.621267932349722, 6.475100734197543, 6.435508747237865, 5.738807515279154,
            5.866333053663887, 5.5276617791315505, 6.396126568864948, 6.015525805085095, 5.018811207449451,
            5.80114773948062, 6.331987806077699]
    rpup = [6.320752450026039, 6.2198903801194785, 5.958988741552015, 6.696598496460487, 6.442410271547491,
            5.743347633692244, 5.430037397359653, 6.5972075001625035, 5.499173507095739, 6.103474780858872,
            5.221226103401899, 6.750097979894939]

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
            assert e

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
            assert e

    def test_CognitiveLoadHandler(self):
        handler = CognitiveLoadHandler()
        for i in range(1, 42):
            handler.send_data_window(
                {"initTime": self.init, "endTime": self.end, "lpup": self.lpup, "rpup": self.rpup}
            )
            assert len(handler.list_of_baseline_values) == 0
            assert len(handler.dict_of_lists_of_values["initTime"]) == 12 * i
        # calculate first measurement
        assert len(handler.dict_of_lists_of_values["initTime"]) == 41 * 12
        assert len(handler.list_of_baseline_values) == 0
        handler.send_data_window(
            {"initTime": self.init, "endTime": self.end, "lpup": self.lpup, "rpup": self.rpup}
        )
        assert len(handler.dict_of_lists_of_values["initTime"]) == 0
        assert len(handler.list_of_baseline_values) == 1

        for i in range(210):
            handler.send_data_window(
                {"initTime": self.init, "endTime": self.end, "lpup": self.lpup, "rpup": self.rpup}
            )
        assert len(handler.dict_of_lists_of_values["initTime"]) == 0
        assert len(handler.list_of_baseline_values) == 6

        # transition to csv phase:
        handler.baseline_end_time -= 100
        for i in range(1, 45):
            handler.send_data_window(
                {"initTime": self.init, "endTime": self.end, "lpup": self.lpup, "rpup": self.rpup}
            )
        assert handler.phase_func == handler.csv_phase
        assert type(handler.baseline) == float and 0 < handler.baseline < 1
        try:
            # should throw File not found error
            for i in range(1, 45):
                handler.send_data_window(
                    {"initTime": self.init, "endTime": self.end, "lpup": self.lpup, "rpup": self.rpup}
                )
            assert False
        except OSError as e:
            assert e
