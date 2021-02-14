# driver code for project.
# import crunch, dashboard, preprocessing
# Spawns 4 threads:
# 3 producers: eyetracker, wristband, skeletal.  APIs and preprocessing runs in these threads
# 1 consumer: Crunch. reads preprocessed data from producers (doesnt require locking), syncs, computes measurements,
# sends measurement to dashboard
# OR: Only device APIs runs in parallel. Relatively.
# All code for
#
#
# references:
# consumer producer with python:
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Condition_Objects_Producer_Consumer.php
import time
from multiprocessing import Queue, Process

from crunch.crunch import Cruncher
from preprocessing.dummyCallbackFunction import callback


def main():
    def consumer(q):
        while True:
            1 + 1
            time.sleep(0.5)
            print(q.get())

    temperature_q = Queue()  # Eventually 1 queue per device, where each queue element is a dict or tuple.
    cruncher = Cruncher({"e4_q": temperature_q})
    p1 = Process(target=callback, args=(temperature_q,))
    p1.start()
    print("hei")
    cruncher.crunch_flow_control()
    p1.join()


if __name__ == '__main__':
    main()
