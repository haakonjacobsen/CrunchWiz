from collections import deque
from .measurements import calculate_arousal


class HandlerEDA:
    eda_queue = deque(maxlen=121)
    counter = 0

    # public function that empatica control flow can call to add a new data point
    def add_eda_point(self, datapoint):
        self.eda_queue.append(datapoint)
        # calculate measurements if 10 seconds has passed, and we have enough data points (30 seconds worth)
        if self.counter % 40 == 0 and len(self.eda_queue) == 121:
            amplitude, nr_peaks, auc = calculate_arousal(list(self.eda_queue))

            # TODO write arousal to csv file, write engagement to csv file

        self.counter += 1


# TODO handler for other datapoints, IBI, etc.
