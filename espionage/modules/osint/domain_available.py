import requests

from espionage.console.input import Input
from espionage.modules.parser.url_parser import UrlParser
from espionage.console import cAvailable


class DomainAvailable:

    """
    Class contains code related to domain availability test. It will check if a domain
    is available for registration or not.
    """
    __ENDPOINT__ = "https://madchecker.com/api/domain/get-information"

    def __init__(self, _domain: str):
        """
        Initialize function of domain available module
        :param _domain: user entered domain name
        :type _domain: str
        """

        self._domain = _domain

    def domain_available(self) -> bool:
        """
        This function will send a request to internet and check if a domain is available or not.
        :return: boolean type content is returned
        :rtype: bool
        """

        check_domain = UrlParser(self._domain).for_md()
        params = {
            "domain": check_domain
        }
        headers = {
            'User-Agent': str(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/96.0.4664.110 Safari/537.36'),
        }
        response = requests.get(
            url=self.__ENDPOINT__,
            params=params,
            headers=headers,
        )
        if response.status_code == 200:
            content = response.json()
            if "domain" not in content:
                return False
            domain_check = content["domain"]
            if "available" not in domain_check:
                return False
            is_available = domain_check["available"]
            return is_available
        return False


if __name__ == '__main__':
    _input = Input()
    domain = _input.domain
    if isinstance(domain, str):
        d_available = DomainAvailable(domain)
        result = d_available.domain_available()
        c_available = cAvailable()
        c_available.print(is_available=result, domain=domain)

    elif isinstance(domain, list):
        for _domain in domain:
            d_available = DomainAvailable(_domain)
            result = d_available.domain_available()
            c_available = cAvailable()
            c_available.print(is_available=result, domain=_domain)
