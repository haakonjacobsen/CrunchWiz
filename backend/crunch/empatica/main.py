from crunch.empatica.api import MockAPI, RealAPI  # noqa
from crunch.empatica.handler import DataHandler
from crunch.empatica.measurements import (compute_arousal,
                                          compute_emotional_regulation,
                                          compute_engagement,
                                          compute_entertainment,
                                          compute_stress)
import configparser


def start_empatica():
    """
    start the empatica process control flow.
    """
    # Read config & Instantiate the api
    config = configparser.ConfigParser()
    try:
        config.read('setup.cfg')
        api = MockAPI if config['empatica'].getboolean('MockAPI') else RealAPI
    except KeyError:
        raise KeyError("Error in config file, could not find value empatica")
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found")
    api = api()

    # Instantiate the arousal data handler and subscribe to the api
    arousal_handler = DataHandler(
        measurement_func=compute_arousal,
        measurement_path="arousal.csv",
        window_length=int(config['compute_arousal']['window length']),
        window_step=int(config['compute_arousal']['window step'])
    )
    api.add_subscriber(arousal_handler, "EDA")

    # Instantiate the engagement data handler and subscribe to the api
    engagement_handler = DataHandler(
        measurement_func=compute_engagement,
        measurement_path="engagement.csv",
        window_length=int(config['compute_engagement']['window length']),
        window_step=int(config['compute_engagement']['window step'])
    )
    api.add_subscriber(engagement_handler, "EDA")

    # Instantiate the emotional regulation data handler and subscribe to the api
    emreg_handler = DataHandler(
        measurement_func=compute_emotional_regulation,
        measurement_path="emotional_regulation.csv",
        window_length=int(config['compute_emotional_regulation']['window length']),
        window_step=int(config['compute_emotional_regulation']['window step'])
    )
    api.add_subscriber(emreg_handler, "IBI")

    # Instantiate the entertainment data handler and subscribe to the api
    entertainment_handler = DataHandler(
        measurement_func=compute_entertainment,
        measurement_path="entertainment.csv",
        window_length=int(config['compute_entertainment']['window length']),
        window_step=int(config['compute_entertainment']['window step'])
    )
    api.add_subscriber(entertainment_handler, "HR")

    # Instantiate the stress data handler and subscribe to the api
    stress_handler = DataHandler(
        measurement_func=compute_stress,
        measurement_path="stress.csv",
        window_length=int(config['compute_stress']['window length']),
        window_step=int(config['compute_stress']['window step'])
    )
    api.add_subscriber(stress_handler, "TEMP")

    # start up the api
    api.connect()
