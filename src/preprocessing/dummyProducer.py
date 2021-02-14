#  This file is not in use as of 12.02. Look at something else, please
import csv, os, time
class DummyProducer:
    """A simple example class"""
    last_point = None
    my_wristband = None

    def get_last_point(self):
        return self.last_point
    def process_next_point(self):
        last_point = self.my_wristband.readline()
        return self.last_point
    def callback(self):
        while True:
            self.last_point = self.my_wristband.readline()
            if self.last_point == '':
                print("break")
                break
            print(self.last_point)
            time.sleep(0.5)

    #  Unimportant:
    def preprocess(self, data):
        return int(data)
    def dumb(self, q):
        q.put(2)

    def f(self):
        return "hei"




    def connect_to_raw_data(self):
        print(2)
        self.my_wristband = open(os.path.dirname(__file__)+r"\\TEMP.csv", "r")
        print(self.my_wristband.readline())
        print(self.my_wristband.readline())
    def unconnect(self):
        self.my_wristband.close()



class DummyProducerThatStoresTheStream:
    """A simple example class"""
    stream = []
    my_wristband = None

    def f(self):
        return 'hello world'
    def collect_raw_data(self):
        self.stream.append(self.my_wristband)

    def get_last_processed_point(self):
        return self.stream

    def connect_to_raw_data(self):
        self.my_wristband = open("TEMP.csv", "r")
    def unconnect(self):
        self.my_wristband.close()



def callback(q):
    wristband = open(os.path.dirname(__file__) + r"\\TEMP.csv", "r")
    print(wristband.readline())
    print(wristband.readline())
    while True:
        last_point = wristband.readline()
        if last_point == '':
            print("break")
            break
        print(last_point)
        q.put(last_point)
        time.sleep(0.5)