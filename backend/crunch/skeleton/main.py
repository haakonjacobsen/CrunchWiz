from crunch.skeleton.api import SkeletonAPI
from crunch.skeleton.handler import DataHandler
from crunch.skeleton.measurements import (amount_of_motion, fatigue,
                                          most_used_joints,
                                          stability_of_motion)


def start_skeleton(api=SkeletonAPI):
    """
    start the eye tracker process control flow.
    """

    # Instantiate the api
    api = api()

    # Instantiate the stability of motion data handler and subscribe to the api
    stability_handler = DataHandler(measurement_func=stability_of_motion,
                                    measurement_path="stability_of_motion.csv",
                                    window_length=2,
                                    window_step=2,
                                    baseline_length=100)
    api.add_subscriber(stability_handler, "body")

    # Instantiate the fatigue data handler and subscribe to the api
    fatigue_handler = DataHandler(measurement_func=fatigue,
                                  measurement_path="fatigue.csv",
                                  window_length=2,
                                  window_step=2,
                                  baseline_length=100)
    api.add_subscriber(fatigue_handler, "body")

    # Instantiate the amount of motion data handler and subscribe to the api
    amount_of_motion_handler = DataHandler(measurement_func=amount_of_motion,
                                           measurement_path="amount_of_motion.csv",
                                           window_length=20,
                                           window_step=20,
                                           baseline_length=15)
    api.add_subscriber(amount_of_motion_handler, "body")

    # Instantiate the most used joint data handler and subscribe to the api
    most_used_joint_handler = DataHandler(measurement_func=most_used_joints,
                                          measurement_path="most_used_joints.csv",
                                          window_length=2,
                                          window_step=2,
                                          calculate_baseline=False)
    api.add_subscriber(most_used_joint_handler, "body")

    # start up the api
    api.connect()
