from .api import MockApi
from .handler import HandlerEDA

# reason we have api=MockApi() in default argument, is so we can replace it when testing.
# In producting we will have real api as default argument, and test will call start_empatica with mockapi
def start_empatica(api=MockApi()):
    # send the datapoint handler to the api
    api.connect(HandlerEDA())
