import datetime

from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.table import Table


class CDHistory:
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
        :type dns_data: dict
        """
        self._console.print("\n")
        if dns_data:
            timeline_tree = Tree("DNS Record History")
            dates_for_timeline = list(dns_data.keys())
            dates_for_timeline.sort(key=lambda x: datetime.datetime.strptime(x, '%B %Y'))

            for timeline_date in dates_for_timeline:
                timeline_element = timeline_tree.add(Text(timeline_date,
                                                          style="bold bright_blue underline"))
                timeline_table = Table(show_header=False, )
                timeline_table.add_column("", )
                for record_data in dns_data[timeline_date]:
                    operation = record_data["operation"]
                    timeline_text = Text()
                    if operation == "Epoch":
                        timeline_text.append("First time DNS ", "bright_green")
                        timeline_text.append(f"{record_data['old server']}",
                                             f"link http://{record_data['old server']}")
                        timeline_text.append(" record was added. ", "bright_green")
                    elif operation in ("New", "Added"):
                        timeline_text.append("DNS ", "spring_green3")
                        timeline_text.append(f"{record_data['new server']}",
                                             f"link http://{record_data['new server']}")
                        timeline_text.append(f" record added on date {record_data['zone date']}",
                                             "spring_green3")
                    elif operation in ("Deleted", "Removed"):
                        timeline_text.append("DNS ", "red ")
                        timeline_text.append(f"{record_data['old server']}",
                                             f"link http://{record_data['old server']}")
                        timeline_text.append(f" record removed on date {record_data['zone date']}",
                                             "red")
                    elif operation == "Transfer":
                        timeline_text.append("DNS transferred from ", "sky_blue2")
                        timeline_text.append(f"{record_data['old server']}",
                                             f"link http://{record_data['old server']}")
                        timeline_text.append(" to ", "sky_blue2")
                        timeline_text.append(f"{record_data['new server']}",
                                             f"link http://{record_data['new server']}")
                        timeline_text.append(f" on date {record_data['zone date']}", "sky_blue2")
                    else:
                        timeline_text.append("path.name", "blue")
                    timeline_table.add_row(timeline_text)
                timeline_element.add(timeline_table)
            self._console.print(timeline_tree)
