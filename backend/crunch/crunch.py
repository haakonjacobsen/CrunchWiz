import os
from multiprocessing import Process

from config import CONFIG_PATH
from crunch.empatica.main import start_empatica
from crunch.eyetracker.main import start_eyetracker
from crunch.skeleton.main import start_skeleton
from crunch.websocket.websocket import start_websocket

import configparser


def start_processes():
    if not os.path.exists("crunch/output"):
        os.makedirs("crunch/output")

    p1 = Process(target=start_empatica)
    p1.start()

    p2 = Process(target=start_eyetracker)
    p2.start()

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    mobile = (config['general']['environment'] == 'mobile')
    if mobile:
        p3 = Process(target=start_skeleton)
        p3.start()

    start_websocket()
