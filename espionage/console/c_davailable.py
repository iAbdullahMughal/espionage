from rich.console import Console
from rich.panel import Panel


class CDAvailable:
    _console = None

    def __init__(self, console=None):
        if not console:
            console = Console()

        self._console = console

    def print(self, is_available, domain):
        if not is_available:
            self._console.print(
                Panel.fit("Domain {} is [red]not available [/red].".format(domain), title="Domain Availability Check",
                      ))
        else:
            self._console.print(
                Panel.fit("Domain {} is [green]available [/green].".format(domain), title="Domain Availability Check",
                      ))
