import time

import crunch.util as util


def start_emotion():
    """
    This function reads a frame from the webcam,
    finds the emotion from the PyEmotion package
    And writes it to it's csv file
    """
    import cv2 as cv
    import PyEmotion

    # Open you default camera
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_BUFFERSIZE, 1)
    er = PyEmotion.DetectFace(device='cpu', gpu_id=0)
    while True:
        _, frame = cap.read()
        _, emotion = er.predict_emotion(frame)
        util.write_csv("emotion.csv", [emotion])
        # only find emotion once every second
        time.sleep(1)
