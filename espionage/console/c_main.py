import secrets

from rich.text import Text
from espionage.constants import Constants


class CMain:
    """
    Console display class for entry function. This class mainly holds banner rotation and version
    information.
    """
    _console = None

    _banner_list = [
        """oooooooooooo                      o8o
`888'     `8                      `"'
 888          .oooo.o oo.ooooo.  oooo   .ooooo.  ooo. .oo.    .oooo.    .oooooooo  .ooooo.
 888oooo8    d88(  "8  888' `88b `888  d88' `88b `888P"Y88b  `P  )88b  888' `88b  d88' `88b
 888    "    `"Y88b.   888   888  888  888   888  888   888   .oP"888  888   888  888ooo888
 888       o o.  )88b  888   888  888  888   888  888   888  d8(  888  `88bod8P'  888    .o
o888ooooood8 8""888P'  888bod8P' o888o `Y8bod8P' o888o o888o `Y888""8o `8oooooo.  `Y8bod8P'
                       888                                             d"     YD
                      o888o                                            "Y88888P'""",
        """███████╗███████╗██████╗ ██╗ ██████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██║██╔═══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝
█████╗  ███████╗██████╔╝██║██║   ██║██╔██╗ ██║███████║██║  ███╗█████╗
██╔══╝  ╚════██║██╔═══╝ ██║██║   ██║██║╚██╗██║██╔══██║██║   ██║██╔══╝
███████╗███████║██║     ██║╚██████╔╝██║ ╚████║██║  ██║╚██████╔╝███████╗
╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝""",
        """ _______  _______  _______  ___   _______  __    _  _______  _______  _______
|       ||       ||       ||   | |       ||  |  | ||   _   ||       ||       |
|    ___||  _____||    _  ||   | |   _   ||   |_| ||  |_|  ||    ___||    ___|
|   |___ | |_____ |   |_| ||   | |  | |  ||       ||       ||   | __ |   |___
|    ___||_____  ||    ___||   | |  |_|  ||  _    ||       ||   ||  ||    ___|
|   |___  _____| ||   |    |   | |       || | |   ||   _   ||   |_| ||   |___
|_______||_______||___|    |___| |_______||_|  |__||__| |__||_______||_______|"""
    ]

    def __init__(self, console):
        """
        Init function of console main class
        :param console: terminal console
        :type console: Console
        """

        self._console = console

    def banner(self):
        """
        This function prints a banner on terminal screen.
        """

        constants = Constants()
        banner_text = secrets.choice(self._banner_list)
        project_title = f"\n\nEspionage v {constants.version} - Domain reconnaissance tool\n"
        # project_author = "\nBy {}".format(Constants.author)
        # author_email = "\033[4m{}\033[0m".format(Constants.email)

        text = Text()
        text.append(banner_text)
        text.append(project_title)
        # text.append(project_author, style="bold magenta")
        # text.append(" (", style="")
        # text.append(author_email, style="italic blue")
        # text.append(")", style="")

        self._console.print(text)
