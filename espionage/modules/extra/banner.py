from espionage.modules.extra.colors import Colors


class Banner:

    def __init__(self, version=""):
        self.version = version

    @staticmethod
    def _block(count):
        block = ""
        i = 0
        while i < count:
            block += "█"
            i += 1
        return Colors.FAIL + block + Colors.ENDC

    @staticmethod
    def _shadow(shape):
        return Colors.WARNING + shape + Colors.ENDC

    @staticmethod
    def _separator(user_len):
        shape = ""
        i = 0
        while i < user_len:
            shape += "-"
            i += 1
        return shape

    @staticmethod
    def _script_info(user_len, user_text="1.0.0"):
        user_len = user_len - (len(user_text))
        shape = ""
        i = 0
        while i < user_len:
            shape += " "
            i += 1
        return shape + user_text

    def banner(self):
        banner_text = " " + str(self._block(7)) + self._shadow("╗") + str(self._block(7)) + self._shadow("╗") + str(
            self._block(6)) + self._shadow(
            "╗") + " " + str(self._block(2)) + self._shadow("╗") + " " + str(self._block(6)) + self._shadow(
            "╗") + " " + str(
            self._block(3)) + self._shadow("╗") + "   " + str(self._block(2)) + self._shadow("╗") + " " + str(
            self._block(5)) + self._shadow(
            "╗") + "  " + str(self._block(6)) + self._shadow("╗") + " " + str(self._block(7)) + self._shadow(
            "╗") + "\n " + \
                      str(self._block(2)) + self._shadow("╔════╝") + str(self._block(2)) + self._shadow("╔════╝") + str(
            self._block(2)) + self._shadow(
            "╔══") + str(self._block(2)) + self._shadow("╗") + str(self._block(2)) + self._shadow("║") + str(
            self._block(2)) + self._shadow(
            "╔═══") + str(
            self._block(2)) + self._shadow("╗") + str(self._block(4)) + self._shadow("╗") + "  " + str(
            self._block(2)) + self._shadow("║") + str(
            self._block(2)) + self._shadow("╔══") + str(self._block(2)) + self._shadow("╗") + str(
            self._block(2)) + self._shadow("╔════╝ ") + str(
            self._block(2)) + self._shadow("╔════╝") + "\n " + \
                      str(self._block(5)) + self._shadow("╗  ") + str(self._block(7)) + self._shadow("╗") + str(
            self._block(6)) + self._shadow(
            "╔╝") + str(self._block(2)) + self._shadow("║") + str(self._block(2)) + self._shadow("║") + self._shadow(
            "   ") + str(
            self._block(2)) + self._shadow("║") + str(self._block(2)) + self._shadow("╔") + str(
            self._block(2)) + self._shadow("╗ ") + str(
            self._block(2)) + self._shadow("║") + str(self._block(7)) + self._shadow("║") + str(
            self._block(2)) + self._shadow("║  ") + str(
            self._block(3)) + self._shadow("╗") + str(self._block(5)) + self._shadow("╗") + "\n " + \
                      str(self._block(2)) + self._shadow("╔══╝  ╚════") + str(self._block(2)) + self._shadow("║") + str(
            self._block(2)) + self._shadow(
            "╔═══╝ ") + str(self._block(2)) + self._shadow("║") + str(self._block(2)) + self._shadow(
            "║") + self._shadow("   ") + str(
            self._block(2)) + self._shadow("║") + str(self._block(2)) + self._shadow("║╚") + str(
            self._block(2)) + self._shadow("╗") + str(
            self._block(2)) + self._shadow("║") + str(self._block(2)) + self._shadow("╔══") + str(
            self._block(2)) + self._shadow("║") + str(
            self._block(2)) + self._shadow("║   ") + str(self._block(2)) + self._shadow("║") + str(
            self._block(2)) + self._shadow(
            "╔══╝") + "\n " + str(
            self._block(7)) + self._shadow("╗") + str(self._block(7)) + self._shadow("║") + str(
            self._block(2)) + self._shadow("║     ") + str(
            self._block(2)) + self._shadow("║╚") + str(self._block(6)) + self._shadow("╔╝") + str(
            self._block(2)) + self._shadow("║ ╚") + str(
            self._block(4)) + self._shadow("║") + str(self._block(2)) + self._shadow("║  ") + str(
            self._block(2)) + self._shadow("║╚") + str(
            self._block(6)) + self._shadow("╔╝") + str(self._block(7)) + self._shadow("╗") + "\n " + self._shadow(
            "╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝")

        print(banner_text)
        user_len = 73
        print(self._separator(user_len))
        title = "Espionage " + self.version
        print(self._script_info(user_len, title))
        tag_line = "Domain Information Gathering, Reconnaissance & Osint"
        print(self._script_info(user_len, tag_line))
