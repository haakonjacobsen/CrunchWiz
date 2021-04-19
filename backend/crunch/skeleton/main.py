import os

from config import CONFIG_PATH
from crunch.skeleton.api import MockAPI, RealAPI  # noqa
from crunch.skeleton.handler import DataHandler
from crunch.skeleton.measurements import (amount_of_motion, fatigue,
                                          most_used_joints,
                                          stability_of_motion)
import configparser


def start_skeleton():
    """
    start the eye tracker process control flow.
    """

    # Read config & Instantiate the api
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_PATH)
        api = MockAPI if config['skeleton'].getboolean('MockAPI') else RealAPI
    except KeyError:
        raise KeyError("Error in config file, could not find value skeleton")
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found")
    api = api()

    print("Started ", api)

    stabilityHandler = DataHandler(
        measurement_func=stability_of_motion,
        measurement_path="stability_of_motion.csv",
        window_length=int(config['stability_of_motion']['window length']),
        window_step=int(config['stability_of_motion']['window step'])
    )
    api.add_subscriber(stabilityHandler, "body")

    fatigueHandler = DataHandler(
        measurement_func=fatigue,
        measurement_path="fatigue.csv",
        window_length=int(config['fatigue']['window length']),
        window_step=int(config['fatigue']['window step'])
    )
    api.add_subscriber(fatigueHandler, "body")

    motionHandler = DataHandler(
        measurement_func=amount_of_motion,
        measurement_path="amount_of_motion.csv",
        window_length=int(config['amount_of_motion']['window length']),
        window_step=int(config['amount_of_motion']['window step'])
    )
    api.add_subscriber(motionHandler, "body")

    mostUsedJointHandler = DataHandler(
        measurement_func=most_used_joints,
        measurement_path="most_used_joints.csv",
        window_length=int(config['most_used_joints']['window length']),
        window_step=int(config['most_used_joints']['window step']),
        calculate_baseline=False
    )
    api.add_subscriber(mostUsedJointHandler, "body")

    # start up the api
    try:
        api.connect()
    except Exception as e:
        print("Skeleton API connection failed")
        print(e)
        os._exit()
