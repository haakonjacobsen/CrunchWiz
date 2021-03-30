from backend.crunch.skeleton.measurements.fatigue import fatigue
from backend.crunch.skeleton.measurements.stability_of_motion import stability_of_motion
import os

from .api import MockAPI, RealAPI
from .handler import DataHandler
from .measurements import stability_of_motion, fatigue, amount_of_motion, most_used_joints


def start_skeleton(api=MockAPI):
    """
    start the eye tracker process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    print("Skeleton process id: ", os.getpid())
    # Instantiate the api
    api = api()
    stabilityHandler = DataHandler(measurement_func=stability_of_motion,
                               measurement_path="test_data.csv",
                               window_length=2,
                               window_step=2)
    api.add_subscriber(stabilityHandler, "body")

    fatigueHandler = DataHandler(measurement_func=fatigue,
                               measurement_path="test_data.csv",
                               window_length=2,
                               window_step=2)
    api.add_subscriber(fatigueHandler, "body")

    motionHandler = DataHandler(measurement_func=amount_of_motion,
                               measurement_path="test_data.csv",
                               window_length=2,
                               window_step=2)
    api.add_subscriber(motionHandler, "body")
 
    mostUsedJointHandler = DataHandler(measurement_func=most_used_joints,
                               measurement_path="test_data.csv",
                               window_length=2,
                               window_step=2)
    api.add_subscriber(mostUsedJointHandler, "body")

    # start up the api
    try:
        api.connect()
    except Exception as e:
        print("Skeleton API connection failed")
        print(e)
        os._exit()

start_skeleton()