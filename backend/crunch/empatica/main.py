from .api import MockApi
from .handler import HandlerEDA, HandlerIBI, HandlerTemp, HandlerHR


def start_empatica(api=MockApi):
    """
    start the empatica process control flow.
    TODO change default api argument to realAPI, and use MockApi when integration testing only
    """
    # Instantiate the api with all the handlers supplied
    api = api(HandlerEDA(), HandlerIBI(), HandlerTemp(), HandlerHR())
    # start up the api
    api.connect()
