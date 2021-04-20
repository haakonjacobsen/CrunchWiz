import time
import os
import csv


class Time:
    def __init__(self):
        self.curr_time = time.time()

    def delta_time(self):
        new_time = time.time()
        delta = new_time - self.curr_time
        self.curr_time = new_time
        return delta


def write_csv(path, row, header_features=[]):
    """ write result to csv file """
    if not os.path.exists("crunch/output"):
        os.makedirs("crunch/output")

    file_exists = os.path.isfile("crunch/output/" + path)
    with open("crunch/output/" + path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if not file_exists:
            header = ['time', 'value']
            writer.writerow(header + header_features)
        writer.writerow(row)


def to_list(x):
    if isinstance(x, list):
        return x
    try:
        return list(x)
    except TypeError:
        return [x]
