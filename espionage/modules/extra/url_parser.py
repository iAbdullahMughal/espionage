class UrlParser:

    def __init__(self, domain):
        if ":" in domain:
            content = str(domain).split(":")
            if len(content) > 1:
                domain = content[0]
            else:
                domain = content
        self.domain = domain

    @staticmethod
    def __remove_http__(domain):
        domain = str(domain).lower()
        if domain.startswith('http:\\\\'):
            domain = domain.replace('http:\\\\', '')
        elif domain.startswith('https:\\\\'):
            domain = domain.replace('https:\\\\', '')

        return domain

    @staticmethod
    def __remove_www__(domain):
        domain = str(domain).lower()
        if domain.startswith("www."):
            domain = domain.replace('www.', '')

        return domain

    @staticmethod
    def __extract_root__(domain):
        if "/" not in domain:
            return domain
        domain = domain.split("/")
        if len(domain) > 1:
            return domain[0]
        return domain[0]

    def for_dbd(self):
        domain = self.domain
        domain = self.__remove_http__(domain)
        domain = self.__remove_www__(domain)
        domain = self.__extract_root__(domain)

        return domain
