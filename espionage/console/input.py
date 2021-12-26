import argparse
from espionage.constants import Constants


class Input:
    _args = None

    def __init__(self):
        constants = Constants()
        parser = argparse.ArgumentParser(
            description="Espionage " + constants.version)
        parser.add_argument("-d", dest="domain", required=True, help="Domain address for recon operation.")
        parser.add_argument("-e", dest="extended", required=False, type=bool,
                            help="Get extended report against domain.")
        args = parser.parse_args()
        if args.domain:
            if isinstance(args.domain, str):
                self._domain = args.domain
            elif isinstance(args.domain, list):
                self._domain = args.domain
            elif "," in args.domain:
                self._domain = args.domain.split(",")

        if args.extended:
            self._extended = True
        else:
            self._extended = False

    @property
    def domain(self):
        return self._domain

    @property
    def extended(self):
        return self._extended
