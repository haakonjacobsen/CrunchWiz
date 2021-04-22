import time

import tobii_research as tr

from .api import EyetrackerAPI
from .handler import IpiHandler, DataHandler
from .measurements.anticipation import compute_anticipation
from .measurements.perceived_difficulty import compute_perceived_difficulty


def start_eyetracker(api=EyetrackerAPI):
    """Defines the callback function, try to connect to eye tracker, create EyetrackerAPI and add handlers to api"""

    def gaze_data_callback(gaze_data):
        """Callback function that the eyetracker device calls 120 times a second. Inserts data to EyetrackerAPI"""
        left_eye_fx, left_eye_fy = gaze_data['left_gaze_point_on_display_area']
        right_eye_fx, right_eye_fy = gaze_data['right_gaze_point_on_display_area']
        api.insert_new_gaze_data(left_eye_fx, left_eye_fy, right_eye_fx, right_eye_fy,
                                 gaze_data['left_pupil_diameter'], gaze_data['right_pupil_diameter'],
                                 gaze_data['device_time_stamp'])

    #  Try to connect to eyetracker
    if len(tr.find_all_eyetrackers()) == 0:
        print("No eyetracker was found")
    if len(tr.find_all_eyetrackers()) > 0:
        my_eyetracker = tr.find_all_eyetrackers()[0]
        print("Now connected to eyetracker model: " + my_eyetracker.model + " with address: " + my_eyetracker.address)

        api = api()
        # add handlers
        ipi_handler = IpiHandler("ipi.csv", ["initTime", "endTime", "fx", "fy"],
                                 window_length=10, window_step=10)
        api.add_subscriber(ipi_handler)

        perceived_difficulty_handler = DataHandler(
            compute_perceived_difficulty, "perceived_difficulty.csv", ["initTime", "endTime", "fx", "fy"],
            window_length=10, window_step=10
        )
        api.add_subscriber(perceived_difficulty_handler)

        anticipation_handler = DataHandler(
            compute_anticipation, "anticipation.csv", ["initTime", "endTime", "fx", "fy"],
            window_length=10, window_step=10, calculate_baseline=False
        )
        api.add_subscriber(anticipation_handler)

        cognitive_load_handler = DataHandler(
            compute_anticipation, "cognitive_load.csv", ["initTime", "endTime", "lpup", "rpup"],
            window_length=500, window_step=500
        )
        api.add_subscriber(cognitive_load_handler)

        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
        #  TODO: the following snippet stops the program after x seconds. Remove this when finished developing
        time.sleep(400)  # change to how long you want the program to run
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
