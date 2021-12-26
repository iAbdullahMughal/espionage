from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.console import Group
from rich.pretty import Pretty


class CDBData:

    def __init__(self, console=None):
        if not console:
            console = Console()
        self._console = console

    def print(self, whois):
        console = self._console

        if not whois:
            return {}
        _group_basic = ""
        _group_registrant = ""
        _group_a = ""
        _group_aaaa = ""
        _group_history = ""
        _group_mx = ""
        _group_whois = ""
        _group_historic_data = ""
        _group_tld = ""

        if "basic_info" in whois:
            basic_info = whois["basic_info"]
            basic_info_table = Table(
                title="Domain basic information",
                show_header=False,
                expand=True
            )
            basic_info_table.add_column("Type")
            basic_info_table.add_column("Data", style="cyan")
            for key in basic_info:
                value = basic_info[key]
                basic_info_table.add_row(key, value, )
            del whois["basic_info"]
            _group_basic = basic_info_table

        if "registrant_info" in whois:
            registrant_info = whois["registrant_info"]
            registrant_info_table = Table(
                title="Domain Registrant Information",
                show_header=False, expand=True

            )
            registrant_info_table.add_column("Type")
            registrant_info_table.add_column("Data", style="cyan")
            for key in registrant_info:
                value = registrant_info[key]
                registrant_info_table.add_row(key, value, )
            _group_registrant = registrant_info_table
            del whois["registrant_info"]

        if "name_server" in whois:
            for rtype in whois["name_server"]:
                r_table = Table(
                    title="{} Record".format(rtype),
                    expand=True
                )
                records = whois["name_server"][rtype]
                if "a" == rtype.lower() or "aaaa" == rtype.lower():
                    r_table.add_column("Type")
                    r_table.add_column("Hostname", style="cyan")
                    r_table.add_column("Address", style="blue")
                    r_table.add_column("TTL", )
                    r_table.add_column("Class", )
                    for _type, _hostname, _address, _ttl, _class in records:
                        r_table.add_row(_type, _hostname, _address, _ttl, _class)
                    _group_a = r_table
                elif "aaaa" == rtype.lower():

                    r_table.add_column("Type")
                    r_table.add_column("Hostname", style="cyan")
                    r_table.add_column("Address", style="blue")
                    r_table.add_column("TTL", )
                    r_table.add_column("Class", )
                    for _type, _hostname, _address, _ttl, _class in records:
                        r_table.add_row(_type, _hostname, _address, _ttl, _class)

                    _group_aaaa = r_table
                elif "mx" == rtype.lower():
                    r_table.add_column("Type")
                    r_table.add_column("Hostname", style="cyan")

                    r_table.add_column("Preference", )
                    r_table.add_column("TTL", )
                    r_table.add_column("Class", )
                    if len(records[0]) == 6:
                        r_table.add_column("Address", style="cyan")
                        for _type, _hostname, _address, _preference, _ttl, _class in records:
                            r_table.add_row(_type, _hostname, _address, _preference, _ttl, _class)

                    if len(records[0]) == 5:
                        for _type, _hostname,  _preference, _ttl, _class in records:
                            r_table.add_row(_type, _hostname,  _preference, _ttl, _class)

                    _group_mx = r_table
                elif "history" == rtype.lower():
                    r_table.add_column("Date")
                    r_table.add_column("Status", style="cyan")
                    r_table.add_column("Name Server", style="cyan")
                    for _date, _status, _nameserver in records[1:]:
                        r_table.add_row(_date, _status, _nameserver)
                    _group_history = r_table

            del whois["name_server"]

        if "other_tld" in whois:
            other_tld = whois["other_tld"]
            info_table = Table(
                title="[bold]Other TLDs",
                show_header=False,
                expand=True,
            )

            info_table.add_column("TLD1")
            info_table.add_column("TLD2")
            info_table.add_column("TLD3")
            info_table.add_column("TLD4")
            info_table.add_column("TLD5")
            other_tld = sorted(other_tld)
            if len(other_tld) > 50:
                other_tld = other_tld[:50]
            missing_records = len(other_tld) % 5

            while missing_records > 1:
                other_tld.append(
                    " - "
                )
                missing_records = missing_records - 1
            while other_tld:
                value_one, value_two, value_three, value_four, value_five = other_tld[:5]
                other_tld.remove(value_one)
                other_tld.remove(value_two)
                other_tld.remove(value_three)
                other_tld.remove(value_four)
                other_tld.remove(value_five)
                info_table.add_row(value_one, value_two, value_three, value_four, value_five)
            _group_tld = info_table
            del whois["other_tld"]

        if "whois_data" in whois:
            basic_info = whois["whois_data"]
            info_table = Table(
                title="[bold]Raw Whois Information",
                show_header=False,
                expand=True
            )
            info_table.add_column("Data")

            info_table.add_row(Pretty(basic_info), )
            _group_whois = info_table
            del whois["whois_data"]

        if "historic_data" in whois:
            historic_data = whois["historic_data"]
            info_table = Table(
                title="[bold]Historic Records",
                show_header=False,
                expand=True
            )
            info_table.add_column("Data")

            for _record in historic_data:
                info_table.add_row(
                    Panel(Pretty(_record["whois_data"]),
                          title="[red]Recorded date at {}".format(_record["recorded_date"])), )
            _group_historic_data = info_table
            del whois["historic_data"]

        _panel = []

        if _group_basic:
            _panel.append(
                Panel(_group_basic),
            )
        if _group_registrant:
            _panel.append(
                Panel(_group_registrant),
            )
        if _group_a:
            _panel.append(
                Panel(_group_a),
            )
        if _group_aaaa:
            _panel.append(
                Panel(_group_aaaa),
            )
        if _group_mx:
            _panel.append(
                Panel(_group_mx),
            )
        if _group_history:
            _panel.append(
                Panel(_group_history),
            )
        if _group_whois:
            _panel.append(
                Panel(_group_whois),
            )
        if _group_tld:
            _panel.append(
                Panel(_group_tld),
            )
        if _group_historic_data:
            _panel.append(
                Panel(_group_historic_data),
            )
        panel_group = Group(
            *_panel
        )
        console.print(Panel.fit(panel_group, title="Domain Whois Information"))
