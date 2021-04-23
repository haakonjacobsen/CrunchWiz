from multiprocessing import Process

from crunch.emotion import start_emotion
from crunch.empatica import start_empatica
from crunch.eyetracker import start_eyetracker
from crunch.skeleton import start_skeleton
from crunch.websocket import start_websocket


def start_processes(mobile):
    p1 = Process(target=start_empatica)
    p1.start()

    p2 = Process(target=start_eyetracker)
    p2.start()
    if mobile:
        p3 = Process(target=start_skeleton)
        p3.start()
    else:
        p3 = Process(target=start_emotion)
        p3.start()

    start_websocket()
