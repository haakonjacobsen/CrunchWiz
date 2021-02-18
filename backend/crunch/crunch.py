import time


class Cruncher:

    def __init__(self, dict_of_queues):
        # keys: {"empatica_q", "eyetracker_q", "skeleton_q"}
        self.dict_of_queues = dict_of_queues
        self.empatica_q = self.dict_of_queues["empatica_q"]
        self.eyetracker_q = self.dict_of_queues["eyetracker_q"]
        self.skeleton_q = self.dict_of_queues["skeleton_q"]

    def crunch_flow_control(self):
        time.sleep(1)
        if self.empatica_q.empty():  # TODO: set boolean values for each device
            print("empatica wristband is not producing data")
        if self.eyetracker_q.empty():
            print("the eyetracker is not producing data")
        if self.skeleton_q.empty():
            print("not receiving skeletal data")
        while True:
            if not self.empatica_q.empty():
                print(self.empatica_q.get())
                #  Call empatica calculations
            if not self.eyetracker_q.empty():
                print(self.eyetracker_q.get())
                #  call eyetracker stuff
            if not self.empatica_q.empty():
                print(self.eyetracker_q.get())
                #  call skeleton stuff

    # TODO: Define functions that compute measurements here

    # test
    def hello_crunch(self):
        print("hello")
