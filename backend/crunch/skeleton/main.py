import os

from crunch.skeleton.api import MockAPI, RealAPI # noqa
from crunch.skeleton.handler import DataHandler
from crunch.skeleton.measurements import stability_of_motion, fatigue, amount_of_motion, most_used_joints


def start_skeleton(api=MockAPI):
    """
    start the eye tracker process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    print("Skeleton process id: ", os.getpid())
    # Instantiate the api
    api = api()
    stabilityHandler = DataHandler(measurement_func=stability_of_motion,
                                   measurement_path="stability_of_motion.csv",
                                   window_length=2,
                                   window_step=2)
    api.add_subscriber(stabilityHandler, "body")

    fatigueHandler = DataHandler(measurement_func=fatigue,
                                 measurement_path="fatigue.csv",
                                 window_length=2,
                                 window_step=2)
    api.add_subscriber(fatigueHandler, "body")

    motionHandler = DataHandler(measurement_func=amount_of_motion,
                                measurement_path="amount_of_motion.csv",
                                window_length=2,
                                window_step=2)
    api.add_subscriber(motionHandler, "body")

    mostUsedJointHandler = DataHandler(measurement_func=most_used_joints,
                                       measurement_path="most_used_joints.csv",
                                       window_length=2,
                                       window_step=2,
                                       calculate_baseline=False)
    api.add_subscriber(mostUsedJointHandler, "body")

    # start up the api
    try:
        api.connect()
    except Exception as e:
        print("Skeleton API connection failed")
        print(e)
        os._exit()
