from espionage.console.input import Input
from rich.console import Console
from espionage.console import cMain
from espionage.modules.osint.domain_available import DomainAvailable
from espionage.modules.osint.domain_big_data import DomainBigData
from espionage.console import cAvailable, cDomainWhois


def main():
    console = Console()
    c_main = cMain(console=console)
    c_main.banner()
    _input = Input()
    domain = _input.domain
    if isinstance(domain, str):
        # Check domain availability
        c_availability = DomainAvailable(domain=domain)
        da_console = cAvailable(console=console)
        da_console.print(c_availability.domain_available(), domain)

        # Check domain whois records
        c_whois = DomainBigData()
        db_console = cDomainWhois(console=console)
        db_console.print(c_whois.record_by_domain_address(domain=domain, extended_report=_input.extended))
    elif isinstance(domain, list):
        for _domain in domain:
            # Check domain availability
            c_availability = DomainAvailable(domain=_domain)
            da_console = cAvailable(console=console)
            da_console.print(c_availability.domain_available(), _domain)

            # Check domain whois records
            c_whois = DomainBigData()
            db_console = cDomainWhois(console=console)
            db_console.print(c_whois.record_by_domain_address(domain=_domain, extended_report=_input.extended))


if __name__ == '__main__':
    main()
