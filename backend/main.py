import argparse

from crunch import start_processes

if __name__ == '__main__':
    # read system arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--static', action='store_true',
                        help='Set the environment to be static, default is mobile')
    parser.add_argument('--mobile', action='store_true',
                        help='Set the environment to be mobile, default is mobile (this argument is redundant)')
    args = vars(parser.parse_args())

    # Determine whether it is a mobile or static setup
    if args['static']:
        mobile = False
    else:
        mobile = True

    # start program
    start_processes(mobile)

"""
Use this to move csv to different folder on exit
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

import sys
signal.signal(signal.SIGINT, signal_handler)
"""
