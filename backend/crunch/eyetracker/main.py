from crunch import util
from crunch.eyetracker.api import EyetrackerAPI
from crunch.eyetracker.handler import DataHandler, ThresholdDataHandler
from crunch.eyetracker.measurements import (compute_anticipation,
                                            compute_cognitive_load,
                                            compute_ipi,
                                            compute_perceived_difficulty)


def start_eyetracker():
    """Defines the callback function, try to connect to eye tracker, create EyetrackerAPI and add handlers to api"""

    # Read config & Instantiate the api
    api = EyetrackerAPI() if util.config('eyetracker', 'MockAPI') == "True" else EyetrackerAPI()

    ipi_handler = ThresholdDataHandler(
        measurement_func=compute_ipi,
        measurement_path="information_processing_index.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        baseline_length=10,
        threshold_length=20
    )
    api.add_subscriber(ipi_handler, "fixation")

    perceived_difficulty_handler = DataHandler(
        measurement_func=compute_perceived_difficulty,
        measurement_path="perceived_difficulty.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        baseline_length=5
    )
    api.add_subscriber(perceived_difficulty_handler, "fixation")

    anticipation_handler = DataHandler(
        measurement_func=compute_anticipation,
        measurement_path="anticipation.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        calculate_baseline=False
    )
    api.add_subscriber(anticipation_handler, "fixation")

    cognitive_load_handler = DataHandler(
        measurement_func=compute_cognitive_load,
        measurement_path="cognitive_load.csv",
        subscribed_to=["initTime", "endTime", "lpup", "rpup"],
        window_length=500,
        window_step=250,
        baseline_length=5
    )
    api.add_subscriber(cognitive_load_handler, "gaze")

    api.connect()
