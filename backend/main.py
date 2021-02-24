from multiprocessing import Queue, Process
#from .crunch.crunch import start_processes
from backend.crunch.crunch import start_processes

def main():
    start_processes()
if __name__ == '__main__':
    main()
