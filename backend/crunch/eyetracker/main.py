from .api import MockApi
from .handler import DataHandler
from .measurements import compute_ipi


def start_eyetracker(api=MockApi):
    """
    start the eye tracker process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    # Instantiate the api
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
