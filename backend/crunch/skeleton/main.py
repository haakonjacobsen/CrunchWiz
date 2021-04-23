import crunch.util as util
from crunch.skeleton.api import MockAPI, RealAPI  # noqa
from crunch.skeleton.handler import DataHandler
from crunch.skeleton.measurements import (amount_of_motion, fatigue,
                                          most_used_joints,
                                          stability_of_motion)


def start_skeleton():
    """
    start the eye tracker process control flow.
    """

    # Read config & Instantiate the api
    api = MockAPI() if util.config('skeleton', 'MockAPI') == "True" else RealAPI()

    stability_handler = DataHandler(measurement_func=stability_of_motion,
                                    measurement_path="stability_of_motion.csv",
                                    window_length=2,
                                    window_step=2,
                                    baseline_length=2)
    api.add_subscriber(stability_handler, "body")

    fatigue_handler = DataHandler(measurement_func=fatigue,
                                  measurement_path="fatigue.csv",
                                  window_length=2,
                                  window_step=2,
                                  baseline_length=2)
    api.add_subscriber(fatigue_handler, "body")

    amount_of_motion_handler = DataHandler(measurement_func=amount_of_motion,
                                           measurement_path="amount_of_motion.csv",
                                           window_length=20,
                                           window_step=20,
                                           baseline_length=2)
    api.add_subscriber(amount_of_motion_handler, "body")

    most_used_joint_handler = DataHandler(measurement_func=most_used_joints,
                                          measurement_path="most_used_joints.csv",
                                          window_length=2,
                                          window_step=2,
                                          calculate_baseline=False)
    api.add_subscriber(most_used_joint_handler, "body")

    # start up the api
    api.connect()
# except Exception:
#     print("Skeleton API connection failed")
