from multiprocessing import Process

from crunch.emotion import start_emotion
from crunch.empatica import start_empatica
from crunch.eyetracker import start_eyetracker
from crunch.skeleton import start_skeleton
from crunch.websocket import start_websocket


def start_processes(mobile):
    p4 = Process(target=start_websocket)
    p4.start()

    p1 = Process(target=start_empatica)
    p1.start()

    p2 = Process(target=start_eyetracker)
    p2.start()

    if mobile:
        p3 = Process(target=start_skeleton)
        p3.start()
    else:
        from crunch.emotion import mock_emotion
        from crunch.emotion import mock_anticipation
        p5 = Process(target=mock_emotion)
        p5.start()
        p6 = Process(target=mock_anticipation)
        p6.start()
    # start_emotion()
    #start_websocket()
