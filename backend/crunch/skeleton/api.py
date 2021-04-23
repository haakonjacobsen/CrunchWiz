import os
import sys
import time
from sys import platform

import pandas as pd

import crunch.util as util
from crunch.skeleton.handler import DataHandler  # noqa


class MockAPI:
    """
    Mock api that reads from csv files instead of getting data from devices

    :type subscribers: dict
    """

    skeleton_data = []

    # Get test data from scuffed CSV
    df = pd.pandas.read_csv(
        os.path.join(os.path.dirname(__file__), "mock_data/test_data.csv"), header=None
    )
    for i in range(len(df)):
        temp_array = []
        row = df.iloc[i].tolist()
        tuple = set()
        i = 0
        while i < len(row):
            number = (
                float(row[i].strip().strip("[]()")),
                float(row[i + 1].strip().strip("[]()")),
            )
            i += 2
            temp_array.append(number)
        skeleton_data.append(temp_array)

    raw_data = ["body"]
    subscribers = {"body": []}

    def add_subscriber(self, data_handler, requested_data):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        :param requested_data: The specific raw data that the data handler subscribes to
        :type requested_data: str
        """
        assert requested_data in self.subscribers.keys()
        self.subscribers[requested_data].append(data_handler)

    def connect(self):
        """ Simulates connecting to the device, starts reading from csv files and push data to handlers """
        for i in range(1000):
            self._mock_datapoint(i)

            # simulate delay of new data points by sleeping
            time.sleep(1)

    def _mock_datapoint(self, index):
        if index < len(self.skeleton_data):
            for subscriber in self.subscribers["body"]:
                subscriber.add_data_point(self.skeleton_data[index])


class RealAPI:
    """
    Mock api that reads from csv files instead of getting data from devices
    """

    raw_data = ["body"]
    subscribers = {"body": []}

    def add_subscriber(self, data_handler, requested_data):
        """
        Adds a handler as a subscriber for a specific raw data

        :param data_handler: a data handler for a specific measurement that subscribes to a specific raw data
        :type data_handler: DataHandler
        :param requested_data: The specific raw data that the data handler subscribes to
        :type requested_data: str
        """
        assert requested_data in self.subscribers.keys()
        self.subscribers[requested_data].append(data_handler)
    prev_frame = [(0.0, 0.0) for _ in range(25)]

    def preprocess(self, frame):
        self.prev_frame = [(i, j) if i != 0 and j != 0 else self.prev_frame[m] for m, (i,j) in enumerate(frame)]
        print(self.prev_frame)
        return self.prev_frame

    def add_datapoint(self, datums):
        datum = datums[0]
        if datum.poseKeypoints is not None:
            fixed_data = [(row[0], row[1]) for row in datum.poseKeypoints[0]]
            data = self.preprocess(fixed_data)
            for handler in self.subscribers["body"]:
                handler.add_data_point(data)

    def connect(self):
        print("connected to realapi")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            if platform == "win32":
                # Change these variables to point to the correct folder (Release/x64 etc.)
                sys.path.append(dir_path + "/openpose/build/python/openpose/Release")
                y = dir_path + "/openpose/build/x64/Release;"
                z = dir_path + "/openpose/build/bin;"
                os.environ["PATH"] = os.environ["PATH"] + ";" + y + z
                import pyopenpose as op
            else:
                sys.path.append("/openpose/build/python")
                from openpose import pyopenpose as op
        except ImportError as e:
            print(
                "Error: OpenPose library could not be found. Did you install OpenPose and enable `BUILD_PYTHON` in"
                " CMake?"
            )
            raise e

        # Custom Params (refer to include/openpose/flags.hpp for more parameters)
        config = util.config("openpose")
        params = dict()
        params["model_folder"] = dir_path + "/openpose/models/"
        try:
            for key, value in config.items():
                params[key] = value
        except KeyError as e:
            raise KeyError(e)

        # Starting OpenPose
        opWrapper = op.WrapperPython(op.ThreadManagerMode.AsynchronousOut)
        opWrapper.configure(params)
        opWrapper.start()

        user_wants_to_exit = False
        while not user_wants_to_exit:
            dataframe = op.VectorDatum()
            time.sleep(1)
            opWrapper.setDefaultMaxSizeQueues(1)
            if opWrapper.waitAndPop(dataframe):
                if "no_display" not in params:
                    user_wants_to_exit = self.display(dataframe)
                self.add_datapoint(dataframe)
            else:
                break
        print("OpenPose Exited")

    def display(self, datums):
        import cv2
        data = datums[0]
        cv2.imshow("OpenPose 1.7.0 - CrunchWiz", data.cvOutputData)
        key = cv2.waitKey(1)
        return key == 27