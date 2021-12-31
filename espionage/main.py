import itertools
import json
import sys
import threading
import time
from rich.console import Console

from espionage.console.input import Input
from espionage.console import cAvailable, cDomainWhois, cDomainHistory, cMain
from espionage.modules.osint import DomainAvailable, DnsHistory, DomainBigData


class Main:
    """Main class for handling thread and animation."""

    _done = False

    def animate(self):
        """
        Function prints animation on console screen.
        """
        for symbol in itertools.cycle(['|', '/', '-', '\\']):
            if self._done:
                break
            sys.stdout.write('\rSearching record ' + symbol)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r')

    def json_record(self, domain, extended=False):
        """
        This function will collect data from all remaining functions and generates a json dump for
        user.
        :param domain: domain address which will be used for testing
        :type domain: str
        :param extended: User want an extended report
        :type extended: bool
        :return: None
        :rtype: dict
        """
        animation_thread = threading.Thread(target=self.animate)
        animation_thread.start()
        report = {
            'domain_address': domain,
            'domain_availability': None,
            'whois_record': None,
            'domain_history': None
        }
        # Check domain availability
        c_availability = DomainAvailable(_domain=domain)
        report["domain_availability"] = c_availability.domain_available()

        # Check domain whois records
        c_whois = DomainBigData()
        report["whois_record"] = c_whois.with_domain_name(domain, extended)

        # Check domain dns historical records
        c_dns_historical = DnsHistory(domain)
        report["domain_history"] = c_dns_historical.historical_data()
        self._done = True
        time.sleep(.5)
        return report

    @staticmethod
    def print_report(report, console, domain=""):
        """
        This function will print result on console.
        :param report: a dictionary which contains data
        :type report: dict | None
        :param console: console object where we will print our data
        :type console: Console
        :param domain: domain address which was searched
        :type domain: str| None
        :return: Nothing
        :rtype: None
        """
        da_console = cAvailable(console=console)
        da_console.print(report["domain_availability"], domain)

        if report["whois_record"]:
            db_console = cDomainWhois(console=console)
            db_console.print(report["whois_record"])

        if report["domain_history"]:
            dh_console = cDomainHistory(console=console)
            dh_console.print(report["domain_history"])


def main():
    """
    It's main function of project. It will invoke remaining modules of espionage.
    :return: None
    :rtype: None
    """

    _input = Input()
    domain = _input.domain
    extended = _input.extended
    is_json = _input.json
    console = Console()
    c_main = cMain(console=console)
    c_main.banner()
    if isinstance(domain, str):
        c_report = Main()
        report = c_report.json_record(domain=domain, extended=extended)
        if is_json:
            console.print(json.dumps(report, indent=2))
        else:
            c_report.print_report(report, console, domain)

    elif isinstance(domain, list):
        for _domain in domain:
            c_report = Main()
            report = c_report.json_record(domain=_domain, extended=extended)
            if is_json:
                console.print(json.dumps(report, indent=2))
            else:
                c_report.print_report(report, console, _domain)


if __name__ == '__main__':
    main()
