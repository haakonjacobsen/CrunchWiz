from collections import deque
from .measurements import compute_engagement, compute_arousal, \
    compute_emotional_regulation, compute_entertainment, compute_stress
import csv

# TODO fix handlers for all data point types.
# TODO replace hardcoded 10 with timestamp
# TODO since all handlers are so similar, we might make just one handler class, which takes compute_fucntion etc as parameter


class HandlerEDA:
    """
    Receives EDA data points from the api,
    calls appropriate measurement functions when it has enough data points
    """
    eda_queue = deque(maxlen=121)
    counter = 0

    # TODO normalize, sum, and divide by number of values
    def add_data_point(self, datapoint):
        self.eda_queue.append(datapoint)
        # calculate measurements if 10 seconds has passed, and we have enough data points (30 seconds worth)
        if self.counter % 40 == 0 and len(self.eda_queue) == 121:
            # calculate engagement and write to csv
            engagement = compute_engagement(list(self.eda_queue))
            write_csv("Engagement", [10, engagement])
            # calculate arousal and write to csv
            arousal = compute_arousal(list(self.eda_queue))
            write_csv("Arousal", [15, arousal])
        self.counter += 1


class HandlerIBI:
    """
    Receives IBI data points from the api,
    calls appropriate measurement functions when it has enough data points
    """
    ibi_queue = deque(maxlen=12)
    counter = 0

    def add_data_point(self, datapoint):
        self.ibi_queue.append(datapoint)
        if self.counter % 12 == 0 and len(self.ibi_queue) == 12:
            # calculate emotional regulation and write to csv
            emotional_regulation = compute_emotional_regulation(list(self.ibi_queue))
            write_csv("Emotional_Regulation", [10, emotional_regulation])
        self.counter += 1


class HandlerTemp:
    """
    Receives HR data points from the api,
    calls appropriate measurement functions when it has enough data points
    """
    temp_queue = deque(maxlen=10)
    counter = 0

    def add_data_point(self, datapoint):
        self.temp_queue.append(datapoint)
        if self.counter % 10 == 0 and len(self.temp_queue) == 10:
            # calculate emotional regulation and write to csv
            stress = compute_stress(list(self.temp_queue))
            write_csv("Stress", [10, stress])
        self.counter += 1


class HandlerHR:
    """
    Receives HR data points from the api,
    calls appropriate measurement functions when it has enough data points
    """
    hr_queue = deque(maxlen=20)
    counter = 0

    def add_data_point(self, datapoint):
        self.hr_queue.append(datapoint)
        if self.counter % 20 == 0 and len(self.hr_queue) == 20:
            # calculate emotional regulation and write to csv
            entertainment = compute_entertainment(list(self.hr_queue))
            write_csv("Entertainment", [10, entertainment])
        self.counter += 1


"""
No measurement using bvp
class HandlerBVP:
    pass
"""


def write_csv(path, row):
    with open("crunch/output/" + path + ".csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(row)
