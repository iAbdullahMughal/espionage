from rich.console import Console
from rich.table import Table


class CDDns:
    """ Console domain history class for printing results."""

    def __init__(self, console: Console = None):
        """
        Initialize console parameter for printing results and reports
        :param console: console for printing results and reports
        :type console: Console
        """

        if not console:
            console = Console()
        self._console = console

    def print(self, dns_data):
        """
        This function prints result on terminal
        :param dns_data:a dictionary which contains dns history data
        :type dns_data: list
        """
        self._console.print("\n")
        if dns_data:

            table = Table(title="Detailed DNS Record Information", )

            table.add_column("Name", no_wrap=True, )
            table.add_column("Type", no_wrap=True)
            table.add_column("Class", no_wrap=True)
            table.add_column("TTL", justify="center", style="blue", no_wrap=True)
            table.add_column("Endpoint", no_wrap=False)
            for records in dns_data:
                for record in records:
                    endpoint = record["endpoint"]

                    if not isinstance(endpoint, dict):
                        endpoint = f'{record["endpoint"]}'
                    else:

                        keys = endpoint.keys()
                        sub_table = Table(show_header=False)

                        sub_table.add_column("", no_wrap=True)
                        sub_table.add_column("", no_wrap=True)
                        for key in keys:
                            sub_table.add_row(
                                str(key).title().replace("_", " "),
                                endpoint[key]
                            )

                        endpoint = sub_table

                    table.add_row(
                        f'{record["name"]}',
                        f'{record["type"]}',
                        f'{record["class"]}',
                        f'{record["ttl"]}',
                        endpoint,
                    )
                table.add_row(
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                )
            self._console.print(table)
