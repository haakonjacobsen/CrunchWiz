import os

from .api import MockAPI, RealAPI
from .handler import DataHandler
from .measurements import test_function


def start_skeleton(api=MockAPI):
    """
    start the eye tracker process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    print("Skeleton process id: ", os.getpid())
    # Instantiate the api
    api = api()
    test_handler = DataHandler(measurement_func=test_function,
                               measurement_path="test_data.csv",
                               window_length=2,
                               window_step=2)
    api.add_subscriber(test_handler, "body")

    # start up the api
    try:
        api.connect()
    except Exception as e:
        print("Skeleton API connection failed")
        print(e)
        os._exit()

