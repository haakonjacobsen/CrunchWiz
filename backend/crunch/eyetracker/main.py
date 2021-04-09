import os

from crunch.eyetracker.api import MockApi, RealAPI # noqa
from crunch.eyetracker.handler import DataHandler
from crunch.eyetracker.measurements.__init__ import compute_ipi


def start_eyetracker(api=MockApi):
    """
    start the eye tracker process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    # Instantiate the api
    print("Eyetracker process id: ", os.getpid())
    api = api()

    ipi_handler = DataHandler(measurement_func=compute_ipi,
                              measurement_path="ipi.csv",
                              window_length=10,
                              window_step=10,
                              listen_on=["initTime", "endTime", "fx", "fy"],
                              baseline={"short_threshold": 0.5, "long_threshold": 2.0})
    api.add_subscriber(ipi_handler, ["initTime", "endTime", "fx", "fy"])

    # TODO rest of measurements
    # anticipation_handler
    # perdiff_handler

    # start up the api
    api.connect()
