class UrlParser:
    """
    Class addresses cosmetic settings for an url. Different online services requires
    different shape of url so this class generally contains different function which
     beautify url/domain according to its requirement.
    """

    def __init__(self, domain):
        """
        Setting domain address within class. Performing some operations to remove port number
        from string
        :param domain: user provided domain address
        :type domain: str
        """
        if ":" in domain:
            content = str(domain).split(":")
            if len(content) > 1:
                domain = content[0]
            else:
                domain = content
        self.domain = domain

    @staticmethod
    def __remove_http__(domain):
        """
        Removing http identifiers from domain address
        :param domain: user input domain e.g. http://www.google.com
        :type domain: str
        :return: domain without http e.g. www.google.com
        :rtype: str
        """
        domain = str(domain).lower()
        if domain.startswith('http:\\\\'):
            domain = domain.replace('http:\\\\', '')
        elif domain.startswith('https:\\\\'):
            domain = domain.replace('https:\\\\', '')

        return domain

    @staticmethod
    def __remove_www__(domain):
        """
        This function will remove www from any given domain
        :param domain: domain address e.g. www.google.com
        :type domain: str
        :return: return domain without www e.g. google.com
        :rtype: str
        """
        domain = str(domain).lower()
        if domain.startswith("www."):
            domain = domain.replace('www.', '')

        return domain

    @staticmethod
    def __extract_root__(domain):
        """
        This property function extracts root domain from given url
        :param domain: user input domain address
        :type domain: str
        :return: domain e.g. www.google.com
        :rtype: str
        """

        if "/" not in domain:
            return domain
        domain = domain.split("/")
        if len(domain) > 1:
            return domain[0]
        return domain[0]

    def for_dbd(self):
        """
        This function prepares domain for domain history checking service.
        :return: simplified  domain e.g. example.com
        :rtype: str
        """
        domain = self.domain
        domain = self.__remove_http__(domain)
        domain = self.__remove_www__(domain)
        domain = self.__extract_root__(domain)

        return domain

    def for_md(self):
        """
        This function prepares domain for domain availability checking service.
        :return: root of domain e.g. www.example.com
        :rtype: str
        """
        domain = self.domain
        domain = self.__remove_http__(domain)
        domain = self.__extract_root__(domain)
        return domain
