from backend.device_output.monitor_output import Watcher
from backend.preprocessing.pre_process import PreProcessor
from multiprocessing import Queue, Process
from backend.websocket.websocket import start_websocket


# The flow control of the program
# - reads from the device files
# - sends to preprocessing
# - sends to measurements to calculate measurements
# - sends to web socket which sends to client
class CrunchWiz:
    def __init__(self, measurement_queue):
        self.watcher = Watcher()
        self.pre_processor = PreProcessor()
        self.measurements_queue = measurement_queue

    def run(self):
        self.connect_devices()
        self.read_device_output()

    def read_device_output(self):
        self.watcher.run(self.pre_process_output)

    def connect_devices(self):
        # For dummy data, read from the dummy csv files,
        # and output to (initially empty) csv files,
        # which watcher monitors,
        # in a thread
        # For real devices, just start up the device apis in seperate threads
        pass

    def pre_process_output(self, src_path, lines):
        device, raw_data, df = self.pre_processor.process(src_path, lines)
        self.measurements_queue.put({"device": device, "raw_data": raw_data, "data_frame": df})

    def derive_measurements(self):
        # Have a Calculate directory, where we derive measurements based on device,raw data,df
        pass


if __name__ == '__main__':
    q = Queue()
    ws = Process(target=start_websocket, args=(q,))
    ws.start()
    crunch_wiz = CrunchWiz(q)
    crunch_wiz.run()
    ws.join()
