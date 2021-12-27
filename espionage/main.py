from espionage.console.input import Input
from rich.console import Console
import espionage.console
from espionage.modules.osint.domain_available import DomainAvailable
from espionage.modules.osint.domain_big_data import DomainBigData
from espionage.console import cAvailable, cDomainWhois


def main():
    """
    It's main function of project. It will invoke remaining modules of espionage.
    :return: None
    :rtype: None
    """

    console = Console()
    c_main = espionage.console.cMain(console=console)
    c_main.banner()
    _input = Input()
    domain = _input.domain
    if isinstance(domain, str):
        # Check domain availability
        c_availability = DomainAvailable(_domain=domain)
        da_console = cAvailable(console=console)
        da_console.print(c_availability.domain_available(), domain)

        # Check domain whois records
        c_whois = DomainBigData()
        db_console = cDomainWhois(console=console)
        db_console.print(c_whois.with_domain_name(domain, _input.extended))
    elif isinstance(domain, list):
        for _domain in domain:
            # Check domain availability
            c_availability = DomainAvailable(_domain=_domain)
            da_console = cAvailable(console=console)
            da_console.print(c_availability.domain_available(), _domain)

            # Check domain whois records
            c_whois = DomainBigData()
            db_console = cDomainWhois(console=console)
            db_console.print(c_whois.with_domain_name(_domain, _input.extended))


if __name__ == '__main__':
    main()
