from crunch.crunch import start_processes
import argparse
import configparser


def main():
    # read system arguments and write config accordingly
    parser = argparse.ArgumentParser()
    parser.add_argument('--static', action='store_true',
                        help='Set the environment to be static, default is mobile')
    parser.add_argument('--mobile', action='store_true',
                        help='Set the environment to be mobile, default is mobile (this argument is redundant)')
    args = vars(parser.parse_args())
    config = configparser.ConfigParser()
    try:
        config.read('setup.cfg')
    except FileNotFoundError:
        raise FileNotFoundError("Couldnt find config file")

    # write config
    if args['static']:
        config['general']['environment'] = 'static'
    else:
        config['general']['environment'] = 'mobile'
    with open('setup.cfg', 'w') as cfg:
        config.write(cfg)
    start_processes()


if __name__ == '__main__':
    main()


"""
Use this to move csv to different folder on exit
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

import sys
signal.signal(signal.SIGINT, signal_handler)
"""
