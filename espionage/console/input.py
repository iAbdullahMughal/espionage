import argparse
from espionage.constants import Constants


class Input:
    """
    This class addresses user input, we get input from user using this class and parse those
    arguments.
    """
    _args = None

    def __init__(self):
        """
        Init function for preparing arguments for espionage usage.
        """
        constants = Constants()
        parser = argparse.ArgumentParser(
            description="Espionage " + constants.version)
        parser.add_argument("-d", dest="domain", required=True,
                            help="Domain address for recon operation.")
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
    def domain(self) -> str:
        """
        Property which holds information about domain
        :return: user entered domain name
        :rtype: str
        """
        return self._domain

    @property
    def extended(self) -> bool:
        """
        Does use wants an extended report of domain records
        :return: boolean data is returned
        :rtype: bool
        """
        return self._extended
