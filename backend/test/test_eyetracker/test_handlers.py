from crunch.eyetracker.measurements.anticipation import compute_anticipation
from crunch.eyetracker.handler import DataHandler, IpiHandler
from random import randint


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

    def test_Handler(self):
        assert True

    def test_IpiHandler(self):
        def timestamp_generator():
            time = 0
            while True:
                yield time
                time += randint(3, 50)

        handler = IpiHandler("ipi.csv", ["initTime", "endTime", "fx", "fy"],
                             window_length=10, window_step=10)
        time_generator = timestamp_generator()
        assert len(handler.data_queues["initTime"]) == 0
        for i in range(0, 30):
            handler.add_data_point({"initTime": next(time_generator), "endTime": next(time_generator),
                                    "fx": 720, "fy": 1054})

        # transition from threshold phase to baseline phase
        assert len(handler.dict_of_lists_of_threshold_values["initTime"]) == 30
        assert handler.phase_func == handler.threshold_phase
        handler.threshold_phase_end -= 120
        handler.add_data_point({"initTime": next(time_generator), "endTime": next(time_generator),
                                "fx": 720, "fy": 1054})
        assert handler.phase_func == handler.baseline_phase
        assert handler.long_threshold > 0
        assert handler.long_threshold > 0
        # transition from baseline phase to csv phase
        for i in range(1, 10):
            handler.add_data_point({"initTime": next(time_generator), "endTime": next(time_generator),
                                    "fx": 720, "fy": 1054})
            assert len(handler.data_queues["initTime"]) == i
        handler.baseline_end_time -= 120
        handler.add_data_point({"initTime": next(time_generator), "endTime": next(time_generator),
                                "fx": 720, "fy": 1054})
        assert handler.phase_func == handler.csv_phase
        try:
            # should throw File not found error
            for i in range(10):
                handler.add_data_point({"initTime": next(time_generator), "endTime": next(time_generator),
                                    "fx": 720, "fy": 1054})
            assert False
        except OSError as e:
            assert e
