from multiprocessing import Process
from .empatica import start_empatica
from .eyetracker import start_eyetracker
from .skeleton.skeleton_control_flow import skeleton_main
from .websocket.websocket import start_websocket


def start_processes():
    p1 = Process(target=start_empatica)
    p2 = Process(target=start_eyetracker)
    p3 = Process(target=skeleton_main)
    p1.start()
    p2.start()
    p3.start()

    start_websocket()
