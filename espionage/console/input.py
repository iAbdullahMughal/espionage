import argparse
from espionage.constants import Constants


class Input:
    """Class addresses user input, we get input from user using this class and parse arguments."""

    _args = None

    def __init__(self):
        """
        Init function for preparing arguments for espionage usage.
        """

        constants = Constants()
        parser = argparse.ArgumentParser(
            description="Espionage " + constants.version)
        parser.add_argument("-d", dest="domain", required=True, nargs='+',
                            help="Domain address for recon operation.")
        parser.add_argument('-e', '--extended', dest='extended', action='store_true',
                            help="Get extended report against domain.")
        parser.add_argument('-j', '--json', dest='json', action='store_true',
                            help="Add -j --json to create a json report.")

        parser.set_defaults(extended=False)
        parser.set_defaults(json=False)

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

        if args.json:
            self.json = True
        else:
            self.json = False

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
