from multiprocessing import Process
from .empatica.empatica_control_flow import empatica_main
from .eyetracker.eyetracker_control_flow import eyetracker_main
from .skeleton.skeleton_control_flow import skeleton_main


def start_processes():

    p1 = Process(target=empatica_main)
    p2 = Process(target=eyetracker_main)
    p3 = Process(target=skeleton_main)
    p1.start()
    p2.start()
    p3.start()

    # start socket here in main process
