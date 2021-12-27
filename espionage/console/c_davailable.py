from rich.console import Console
from rich.panel import Panel


class CDAvailable:
    """
    We are using the class to print our data on console. This class get reference of console and
    prints content on that console. If reference is not passed then we create a new console, our
    data is printed on that console.
    """

    _console = None

    def __init__(self, console: Console = None):
        """
        Initialize console parameter for printing results and reports
        :param console: rich console terminal
        :type console: Console
        """
        
        if not console:
            console = Console()

        self._console = console

    def print(self, is_available: bool, domain: str) -> None:
        """
        This function prints results collected for domain available test.
        :param is_available: this variable contains information about domain available or not
        :type is_available: bool
        :param domain: value of domain address, on which testing was performed
        :type domain: str
        :return: None
        :rtype: None
        """

        if not is_available:
            self._console.print(
                Panel.fit(f"Domain {domain} is [red]not available [/red].",
                          title="Domain Availability Check", ))
        else:
            self._console.print(
                Panel.fit(f"Domain {domain}  is [green]available [/green].",
                          title="Domain Availability Check", ))
