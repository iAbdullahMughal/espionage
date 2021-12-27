from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.console import Group
from rich.pretty import Pretty


class CDBData:
    """
    This class prints data collected from domainbigdata site.
    """

    def __init__(self, console: Console = None):
        """
        Initialize console parameter for printing results and reports
        :param console: console for printing results and reports
        :type console: Console
        """
        if not console:
            console = Console()
        self._console = console

    @staticmethod
    def __extract_general_info__(whois: dict, data_key: str):
        """
        This function extracts general information from who is dictionary, this information
        is later added into table for console output.
        :param whois: a dictionary which contains whois data
        :type whois: dict
        :param data_key: a key for dictionary which is used to extract data
        :type data_key: str
        :return: data from whois it will return rich table as output, None in case of no data
        :rtype: Table
        """
        if data_key in whois:
            basic_info = whois[data_key]
            data_title = str(data_key).replace("_", " ").title()
            table_data = Table(
                title=f"{data_title} Information",
                show_header=False,
                expand=True
            )
            table_data.add_column("Type")
            table_data.add_column("Data", style="cyan")
            for key in basic_info:
                value = basic_info[key]
                table_data.add_row(key, value, )
            return table_data
        return None

    @staticmethod
    def __extract_name_servers__(whois: dict) -> list:
        """
        This function will extract name server records from whois dictionary
        :param whois: a dictionary which contains whois data
        :type whois: dict
        :return: a list of tables will be returned
        :rtype: list
        """
        name_server_panel = []
        for rtype in whois["name_server"]:
            r_table = Table(
                title=f"{rtype} Record",
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
                name_server_panel.append(
                    r_table
                )
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
                    for _type, _hostname, _preference, _ttl, _class in records:
                        r_table.add_row(_type, _hostname, _preference, _ttl, _class)

                name_server_panel.append(
                    r_table
                )
            elif "history" == rtype.lower():
                r_table.add_column("Date")
                r_table.add_column("Status", style="cyan")
                r_table.add_column("Name Server", style="cyan")
                for _date, _status, _nameserver in records[1:]:
                    r_table.add_row(_date, _status, _nameserver)
                name_server_panel.append(
                    r_table
                )
        return name_server_panel

    @staticmethod
    def __extract_tld__(whois: dict):
        """
        A function for extracting tld records from given whois dictionary.
        :param whois: a dictionary which contains whois data
        :type whois: dict
        :return:a table is returned for printing results.
        :rtype: Table
        """
        if "other_tld" in whois:
            other_tld = whois["other_tld"]
            table_data = Table(
                title="[bold]Other TLDs",
                show_header=False,
                expand=True,
            )

            table_data.add_column("TLD1")
            table_data.add_column("TLD2")
            table_data.add_column("TLD3")
            table_data.add_column("TLD4")
            table_data.add_column("TLD5")
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
                table_data.add_row(value_one, value_two, value_three, value_four, value_five)

            return table_data
        return None

    @staticmethod
    def __extract_whois_data__(whois: dict):
        """
        This function extracts raw text whois data from given dictionary.
        :param whois: a dictionary which contains whois data
        :type whois: dict
        :return:a table is returned for printing results.
        :rtype: Table
        """
        if "whois_data" in whois:
            basic_info = whois["whois_data"]
            table_data = Table(
                title="[bold]Raw Whois Information",
                show_header=False,
                expand=True
            )
            table_data.add_column("Data")

            table_data.add_row(Pretty(basic_info), )
            return table_data
        return None

    @staticmethod
    def __extract_historic_data__(whois):
        """
        This function extracts raw text whois data from given dictionary.
        :param whois: a dictionary which contains whois data
        :type whois: dict
        :return:a table is returned for printing results.
        :rtype: Table
        """
        if "historic_data" in whois:
            historic_data = whois["historic_data"]
            info_table = Table(
                title="[bold]Historic Records",
                show_header=False,
                expand=True
            )
            info_table.add_column("Data")

            for _record in historic_data:
                recorded_data = _record["recorded_date"]
                info_table.add_row(
                    Panel(Pretty(_record["whois_data"]),
                          title=f"[red]Recorded date at "f"{recorded_data}")
                )
            return info_table
        return None

    def print(self, whois):
        """
        This function prints result on terminal
        :param whois: a dictionary which contains whois data
        :type whois: dict
        """
        console = self._console
        console_panel = []

        domain_information = self.__extract_general_info__(whois, "basic_info")
        if domain_information:
            console_panel.append(
                Panel(domain_information),
            )

        registrant_information = self.__extract_general_info__(whois, "registrant_info")
        if registrant_information:
            console_panel.append(
                Panel(registrant_information),
            )
        whois_data = self.__extract_whois_data__(whois)
        if whois_data:
            console_panel.append(
                Panel(whois_data),
            )

        tld_information = self.__extract_tld__(whois)
        if tld_information:
            console_panel.append(
                Panel(tld_information),
            )

        if "name_server" in whois:
            name_server_records = self.__extract_name_servers__(whois=whois)
            if name_server_records:
                for nameserver_record in name_server_records:
                    console_panel.append(
                        Panel(nameserver_record)
                    )

        historic_data = self.__extract_historic_data__(whois)
        if historic_data:
            console_panel.append(
                Panel(historic_data),
            )
        result_group = Group(
            *console_panel
        )
        console.print(Panel.fit(result_group, title="Domain Whois Information"))
