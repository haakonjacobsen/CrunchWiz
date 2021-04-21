import os
import sys
import time
from sys import platform

import cv2
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


def display(datums):
    data = datums[0]
    cv2.imshow("OpenPose 1.7.0 - CrunchWiz", data.cvOutputData)
    key = cv2.waitKey(1)
    return key == 27


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

    def add_datapoint(self, datums):
        datum = datums[0]
        if datum.poseKeypoints is not None:
            fixed_data = [(row[0], row[1]) for row in datum.poseKeypoints[0]]
            for handler in self.subscribers["body"]:
                handler.add_data_point(fixed_data)

    def connect(self):
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
            for key in config["openpose"]:
                params[key] = config["openpose"][key]
        except ValueError as e:
            raise ValueError(e)

        # Starting OpenPose
        opWrapper = op.WrapperPython(op.ThreadManagerMode.AsynchronousOut)
        opWrapper.configure(params)
        opWrapper.start()

        user_wants_to_exit = False
        while not user_wants_to_exit:
            dataframe = op.VectorDatum()
            if opWrapper.waitAndPop(dataframe):
                if "no_display" not in params:
                    user_wants_to_exit = display(dataframe)
                self.add_datapoint(dataframe)
            else:
                break
        print("OpenPose Exited")
