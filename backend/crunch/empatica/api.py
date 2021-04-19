import os
import socket

import pandas as pd

from crunch.empatica.handler import DataHandler  # noqa

import configparser


class MockAPI:
    """
    Mock api that reads from csv files instead of getting data from devices
    """
    dirname = os.path.dirname(__file__)
    eda_data = pd.read_csv(os.path.join(dirname, "mock_data/EDA.csv"))["EDA"]
    ibi_data = pd.read_csv(os.path.join(dirname, "mock_data/IBI.csv"))["IBI"]
    temp_data = pd.read_csv(os.path.join(dirname, "mock_data/TEMP.csv"))["TEMP"]
    hr_data = pd.read_csv(os.path.join(dirname, "mock_data/HR.csv"))["HR"]

    subscribers = {"EDA": [], "IBI": [], "TEMP": [], "HR": []}

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
            self._mock_eda_datapoint(i)
            self._mock_temp_datapoint(i)
            self._mock_ibi_datapoint(i)
            self._mock_hr_datapoint(i)

            # simulate delay of new data points by sleeping
            # time.sleep(0.1)

    def _mock_ibi_datapoint(self, index):
        if index < len(self.ibi_data):
            for handler in self.subscribers["IBI"]:
                data_point = self.ibi_data[index]
                handler.add_data_point(data_point)

    def _mock_eda_datapoint(self, index):
        if index < len(self.eda_data):
            for handler in self.subscribers["EDA"]:
                data_point = self.eda_data[index]
                handler.add_data_point(data_point)

    def _mock_temp_datapoint(self, index):
        if index < len(self.temp_data):
            for handler in self.subscribers["TEMP"]:
                data_point = self.temp_data[index]
                handler.add_data_point(data_point)

    def _mock_hr_datapoint(self, index):
        if index < len(self.hr_data):
            for handler in self.subscribers["HR"]:
                data_point = self.hr_data[index]
                handler.add_data_point(data_point)


# TODO proper error handling on missing connection etc. probably time.wait 5 sec and try again
class RealAPI:
    try:
        config = configparser.ConfigParser()
        config.read('setup.cfg')
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found")

    try:
        print(config.sections())
        serverAddress = config['empatica']['address']
        serverPort = int(config['empatica']['port'])
        bufferSize = int(config['empatica']['buffersize'])
        deviceID = config['empatica']['deviceid']
    except KeyError:
        raise KeyError("ERROR reading from config file setup.cfg[empatica]")

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False

    subscribers = {"EDA": [], "IBI": [], "TEMP": [], "HR": []}

    def connect(self):
        self.socket.settimeout(3)
        self.connect_socket()
        self.subscribe_to_socket()
        self.stream()

    def connect_socket(self):
        if not self.connected:
            self.socket.connect((self.serverAddress, self.serverPort))
            self.connected = True

        self.socket.send("device_list\r\n".encode())
        response = self.socket.recv(self.bufferSize)

        if self.deviceID not in response.decode("utf-8"):
            print("throw error here, device not available")

        self.socket.send(("device_connect " + self.deviceID + "\r\n").encode())
        self.socket.recv(self.bufferSize)

        self.socket.send("pause ON\r\n".encode())
        self.socket.recv(self.bufferSize)

    def subscribe_to_socket(self):
        self.socket.send(("device_subscribe " + 'gsr' + " ON\r\n").encode())
        self.socket.recv(self.bufferSize)

        self.socket.send(("device_subscribe " + 'tmp' + " ON\r\n").encode())
        self.socket.recv(self.bufferSize)

        self.socket.send(("device_subscribe " + 'ibi' + " ON\r\n").encode())
        self.socket.recv(self.bufferSize)

        """
        UNUSED DATA POINTS
        self.socket.send(("device_subscribe " + 'bvp' + " ON\r\n").encode())
        self.socket.recv(self.bufferSize)

        self.socket.send(("device_subscribe " + 'acc' + " ON\r\n").encode())
        self.socket.recv(self.bufferSize)
        """

        self.socket.send("pause OFF\r\n".encode())
        self.socket.recv(self.bufferSize)

    def stream(self):
        while True:
            try:
                response = self.socket.recv(self.bufferSize).decode("utf-8")
                if "connection lost to device" in response:
                    print("LOST CONNECTION TO DEVICE")
                    return self.connect()
                if "turned off via button" in response:
                    print("The wristband was turned off, please reconnect it")
                    return self.connect()

                samples = response.split("\n")
                for i in range(len(samples) - 1):
                    name = samples[i].split()[0]
                    data = float(samples[i].split()[2].replace(',', '.'))
                    if name == "E4_Temperature":
                        self.send_data_to_subscriber("TEMP", data)
                    elif name == "E4_Gsr":
                        self.send_data_to_subscriber("EDA", data)
                    elif name == "E4_Hr":
                        self.send_data_to_subscriber("HR", data)
                    elif name == "E4_Ibi":
                        self.send_data_to_subscriber("IBI", data)

                    """
                    UNUSED DATA POINTS
                    if name == "E4_Bvp":
                        self.send_data_to_subscriber("BVP", data)
                    if name == "E4_Acc":
                        self.send_data_to_subscriber("ACC", data)
                    """

            except socket.timeout:
                print("Socket timeout")
                return self.connect()

    def send_data_to_subscriber(self, name, data):
        for handler in self.subscribers[name]:
            handler.add_data_point(data)

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
