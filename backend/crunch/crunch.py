from multiprocessing import Process

from .empatica import start_empatica
from .eyetracker import start_eyetracker
from .skeleton import start_skeleton
from .websocket import start_websocket
import os


def start_processes():
    print("Main process id: ", os.getpid())
    if not os.path.exists("crunch/output"):
        os.makedirs("crunch/output")
    p1 = Process(target=start_empatica)
    p2 = Process(target=start_eyetracker)
    p3 = Process(target=start_skeleton)
    p1.start()
    p2.start()
    p3.start()
    start_websocket()
