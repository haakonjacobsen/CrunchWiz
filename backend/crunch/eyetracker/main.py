from crunch.eyetracker.api import EyetrackerAPI
from crunch.eyetracker.handler import DataHandler, ThresholdDataHandler
from crunch.eyetracker.measurements import (compute_anticipation,
                                            compute_cognitive_load,
                                            compute_ipi,
                                            compute_perceived_difficulty)


def start_eyetracker(api=EyetrackerAPI):
    """Defines the callback function, try to connect to eye tracker, create EyetrackerAPI and add handlers to api"""

    # Instantiate the api
    api = api()

    # Instantiate the information processing index data handler and subscribe to the api
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

    # Instantiate the perceived difficulty data handler and subscribe to the api
    perceived_difficulty_handler = DataHandler(
        measurement_func=compute_perceived_difficulty,
        measurement_path="perceived_difficulty.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        baseline_length=5
    )
    api.add_subscriber(perceived_difficulty_handler, "fixation")

    # # Instantiate the anticipation data handler and subscribe to the api
    anticipation_handler = DataHandler(
        measurement_func=compute_anticipation,
        measurement_path="anticipation.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        calculate_baseline=False
    )
    api.add_subscriber(anticipation_handler, "fixation")

    # Instantiate the cognital load data handler and subscribe to the api
    cognitive_load_handler = DataHandler(
        measurement_func=compute_cognitive_load,
        measurement_path="cognitive_load.csv",
        subscribed_to=["lpup", "rpup"],
        window_length=1000,
        window_step=250,
        baseline_length=5
    )
    api.add_subscriber(cognitive_load_handler, "gaze")

    # start up the api
    api.connect()
