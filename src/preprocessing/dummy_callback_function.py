import os
import time


def callback(q):
    wristband = open(os.path.dirname(__file__) + r"\\TEMP.csv", "r")
    print(wristband.readline())
    print(wristband.readline())  # prints and gets beyond meta information
    print("Now starting to produce temperature values:")
    while True:
        last_point = wristband.readline()
        if last_point == '':
            print("break")
            break
        q.put(last_point)
        time.sleep(0.5)
