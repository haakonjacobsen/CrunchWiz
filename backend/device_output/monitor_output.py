import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "./device_output/test_data"

    def __init__(self):
        self.observer = Observer()

    def run(self, callback):
        event_handler = Handler(callback)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(100)
        except:
            self.observer.stop()
            print("Stopped processing device data from .csv files")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
        self.tails = {}
        super().__init__()

    def on_modified(self, event):
        if event.is_directory:
            return None

        with open(event.src_path, 'r') as f:
            # Can possibly use pd.read_csv instead of readlines, if we are using a csv file
            if event.src_path in self.tails:
                f.seek(self.tails[event.src_path])
                data = f.readlines()
                self.tails[event.src_path] = f.tell()
            else:
                data = f.readlines()
                self.tails[event.src_path] = f.tell()

        self.callback(event.src_path, data)
