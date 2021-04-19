from crunch.eyetracker.api import EyetrackerAPI, GazedataToFixationdata
from crunch.eyetracker.handler import DataHandler, IpiHandler
from crunch.eyetracker.measurements.perceived_difficulty import compute_perceived_difficulty


class TestGazeDataToFixAndAPI:
    gaze_data = {
        'device_time_stamp': 312133244857,
        'left_pupil_diameter': -1.0,
        'left_gaze_point_on_display_area': (0.753740668296814, -0.11630667001008987),
        'right_gaze_point_on_display_area': (1.1366922855377197, -0.03179898485541344),
        'right_pupil_diameter': -1.0
    }

    def gaze_data_generator(self):
        gaze_data = {
            'device_time_stamp': 312133244857,
            'left_pupil_diameter': -1.0,
            'left_gaze_point_on_display_area': (0.753740668296814, -0.11630667001008987),
            'right_gaze_point_on_display_area': (1.1366922855377197, -0.03179898485541344),
            'right_pupil_diameter': -1.0
        }
        while True:
            yield gaze_data
            gaze_data['device_time_stamp'] += 1000000 / 120

    def timestamp_generator(self):
        timestamp = 312133244857
        while True:
            yield timestamp
            timestamp += 1000000 / 120

    def test_GazedataToFixationdata(self):

        gd = GazedataToFixationdata()
        gazedata_gen = self.timestamp_generator()
        left_eye_fx, left_eye_fy = self.gaze_data['left_gaze_point_on_display_area']
        right_eye_fx, right_eye_fy = self.gaze_data['right_gaze_point_on_display_area']
        # inserting 50 gazepoints that should be part of a fixation, because no eye movement
        for i in range(50):
            assert gd.insert_new_gaze_data(left_eye_fx, left_eye_fy, right_eye_fx, right_eye_fy,
                                           self.gaze_data['left_pupil_diameter'],
                                           self.gaze_data['right_pupil_diameter'],
                                           next(gazedata_gen)) is None
            assert len(gd.list_of_gaze_data_points_in_a_fixation) == i
        # move eyes to the left, should be saccade
        assert type(gd.insert_new_gaze_data(left_eye_fx - 0.3, left_eye_fy, right_eye_fx - 0.3, right_eye_fy,
                                            self.gaze_data['left_pupil_diameter'],
                                            self.gaze_data['right_pupil_diameter'],
                                            next(gazedata_gen))) == dict

    def test_EyetrackerAPI(self):
        def insert_one_fixation_point():
            # inserting 20 gazepoints that should be part of a fixation, because no eye movement
            for j in range(20):
                api.insert_new_gaze_data(left_eye_fx, left_eye_fy, right_eye_fx, right_eye_fy,
                                         self.gaze_data['left_pupil_diameter'],
                                         self.gaze_data['right_pupil_diameter'],
                                         next(gazedata_gen))

            # move eyes to the left, should be saccade
            api.insert_new_gaze_data(left_eye_fx - 0.3, left_eye_fy, right_eye_fx - 0.3, right_eye_fy,
                                     self.gaze_data['left_pupil_diameter'],
                                     self.gaze_data['right_pupil_diameter'],
                                     next(gazedata_gen))

        # set up, add handlers
        api = EyetrackerAPI()
        #ipi_handler = IpiHandler()
        #api.add_subscriber(ipi_handler)

        perceived_difficulty_handler = DataHandler(
            compute_perceived_difficulty, "perceived_difficulty.csv", ["initTime", "endTime", "fx", "fy"],
            window_length=10, window_step=10

        )
        api.add_subscriber(perceived_difficulty_handler)
        gazedata_gen = self.timestamp_generator()

        left_eye_fx, left_eye_fy = self.gaze_data['left_gaze_point_on_display_area']
        right_eye_fx, right_eye_fy = self.gaze_data['right_gaze_point_on_display_area']
        # inserting 20 gazepoints that should be part of a fixation, because no eye movement
        # 5 fixation data points
        for i in range(20):
            insert_one_fixation_point()
        # api should now send first time window
        insert_one_fixation_point()
        assert len(api.dict_of_lists_of_fixation_data["initTime"]) == 0
        for handler in api.list_of_handlers:
            if type(handler) == DataHandler:
                assert len(handler.list_of_baseline_values) == 12
                handler.baseline_end_time -= 200
                insert_one_fixation_point()
                assert handler.phase_func == handler.csv_phase
                try:
                    # should throw File not found error
                    insert_one_fixation_point()
                    assert False
                except OSError as e:
                    assert e

            elif type(handler) == IpiHandler:
                assert len(handler.list_of_baseline_values) == 0
                assert len(handler.dict_of_lists_of_threshold_values["initTime"]) == 6
