import time

import crunch.util as util


def start_emotion():
    import cv2 as cv
    import PyEmotion

    # Open you default camera
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_BUFFERSIZE, 1)
    er = PyEmotion.DetectFace(device='cpu', gpu_id=0)
    timer = util.Time()
    while True:
        _, frame = cap.read()
        _, emotion = er.predict_emotion(frame)
        util.write_csv("emotion.csv", [timer.delta_time(), emotion])
        # only find emotion once every second
        time.sleep(1)


def mock_emotion():
    import random
    vals = ['Neutral', 'Sad', 'Fear', 'Angry', 'Surprise', 'Happy']
    timer = util.Time()
    while True:
        val = random.choice(vals)
        util.write_csv("mock_emotion.csv", [timer.delta_time(), val])
        time.sleep(1)


def mock_anticipation():
    import random
    vals = ['high', 'medium', 'low']
    timer = util.Time()
    while True:
        val = random.choice(vals)
        util.write_csv("mock_anticipation.csv", [timer.delta_time(), val])
    time.sleep(1)
