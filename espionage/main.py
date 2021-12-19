import os
import argparse
import time

from espionage.modules.extra.banner import Banner

__version__ = "0.0.1"


def init():
    parser = argparse.ArgumentParser(
        description="Espionage " + __version__)
    parser.add_argument("-d", dest="domain", required=True, type=str, help="Domain address for recon operation.")
    args = parser.parse_args()


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = Banner(version=__version__)
    banner.banner()
    time.sleep(.5)
    init()
