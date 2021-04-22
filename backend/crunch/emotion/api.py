from PyEmotion import *
import cv2 as cv
import time
import crunch.util as util


def start_emotion():
    # Open you default camera
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_BUFFERSIZE, 1)
    er = DetectFace(device="cpu", gpu_id=0)

    timer = util.Time()

    while True:
        _, frame = cap.read()
        _, emotion = er.predict_emotion(frame)
        util.write_csv("emotion.csv", [timer.delta_time(), emotion])

        # only find emotion once every second
        time.sleep(1)
