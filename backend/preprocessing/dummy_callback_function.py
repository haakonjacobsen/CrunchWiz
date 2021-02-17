import os
import time


def eyetracker_callback(q):
    """
    Pushes dictionaries to a queue on the following format:
    {'index': 386.0, 'initTime': 111.0, 'endTime': 203.0,
    'lpup': 3.664, 'rpup': 3.572, 'fx': 1054.0, 'fy': 720.0}
    :param q: Multiprocessing queue
    :return:
    """

    def fileline_to_dictionary(line):
        # 1 csv fileline -> dictionary
        dictionary_strings = ["index", "initTime", "endTime",
                              "lpup", "rpup", "fx", "fy"]
        eyetracker_data = {}
        line = line[:-1].split(",")
        for key, val in zip(dictionary_strings, line):
            eyetracker_data[key] = safe_conversion_to_float(val)
        return eyetracker_data

    def safe_conversion_to_float(str):
        try:
            return float(str)
        except ValueError:
            assert str == "NA"
            return "NA"

    eyetracker = open(
        os.path.join(os.path.dirname(__file__),
                     'dummy_data',
                     'eye-tracking',
                     'ET-data-S001.csv'), "r")

    # pass meta info: index,initTime,endTime,lpup,rpup,fx,fy
    eyetracker.readline()

    while True:
        last_point = eyetracker.readline()
        if last_point == '':  # end of file
            print("end of file")
            break

        # push a dict to the multistream queue & sleep to simulate real devices
        q.put(fileline_to_dictionary(last_point))
        time.sleep(0.5)  # sleep to simulate real devices

    eyetracker.close()
