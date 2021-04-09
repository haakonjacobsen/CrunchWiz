from multiprocessing import Process

from crunch.empatica.main import start_empatica
from crunch.eyetracker.main import start_eyetracker
from crunch.skeleton.main import start_skeleton
from crunch.websocket.websocket import start_websocket
import os


def start_processes():
    print("Main process id: ", os.getpid())
    if not os.path.exists("crunch/output"):
        os.makedirs("crunch/output")
    # p1 = Process(target=start_empatica)
    # p2 = Process(target=start_eyetracker)
    p3 = Process(target=start_skeleton)
    # p1.start()
    # p2.start()
    p3.start()
    start_websocket()
