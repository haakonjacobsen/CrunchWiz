import time


class Cruncher:

    def __init__(self, dict_of_queues):
        self.dict_of_queues = dict_of_queues

    def crunch_flow_control(self):
        while True:
            time.sleep(0.5)
            print(self.get_temp_queue().get())

    # Helpers

    # access queues
    def get_temp_queue(self):
        return self.dict_of_queues["e4_q"]

    def get_last_point(self):
        return self.last_point
