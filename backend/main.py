from multiprocessing import Queue, Process
from backend.crunch.crunch import Cruncher
from backend.preprocessing.dummy_callback_function import eyetracker_callback


def main():
    #  One queue for each device. An element is a dictionary of values
    eyetracker_q = Queue()
    skeleton_q = Queue()
    empatica_q = Queue()
    cruncher = Cruncher({"empatica_q": empatica_q, "eyetracker_q":eyetracker_q, "skeleton_q":skeleton_q})
    p1 = Process(target=eyetracker_callback, args=(eyetracker_q,))
    p1.start()
    cruncher.crunch_flow_control()
    p1.join()



if __name__ == '__main__':
    main()
