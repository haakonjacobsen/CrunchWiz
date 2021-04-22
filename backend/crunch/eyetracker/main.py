from crunch import util

from .api import EyetrackerAPI
from .handler import DataHandler
from .measurements.perceived_difficulty import compute_perceived_difficulty


def start_eyetracker(api=EyetrackerAPI):
    """Defines the callback function, try to connect to eye tracker, create EyetrackerAPI and add handlers to api"""

    # Read config & Instantiate the api
    api = EyetrackerAPI() if util.config('eyetracker', 'MockAPI') == "True" else EyetrackerAPI()
    """
    ipi_handler = IpiHandler("ipi.csv", ["initTime", "endTime", "fx", "fy"],
                             window_length=10, window_step=10)
    api.add_subscriber(ipi_handler, "fixation")
    """
    # TODO add baseline_length to all
    perceived_difficulty_handler = DataHandler(
        measurement_func=compute_perceived_difficulty,
        measurement_path="perceived_difficulty.csv",
        subscribed_to=["initTime", "endTime", "fx", "fy"],
        window_length=10,
        window_step=10,
        baseline_length=5
    )
    api.add_subscriber(perceived_difficulty_handler, "fixation")

    """
    anticipation_handler = DataHandler(
        compute_anticipation, "anticipation.csv", ["initTime", "endTime", "fx", "fy"],
        window_length=10, window_step=10
    )
    api.add_subscriber(anticipation_handler, "fixation")

    cognitive_load_handler = DataHandler(
        compute_anticipation, "cognitive_load.csv", ["initTime", "endTime", "lpup", "rpup"],
        window_length=500, window_step=500
    )
    api.add_subscriber(cognitive_load_handler, "gaze")
    """

    api.connect()
