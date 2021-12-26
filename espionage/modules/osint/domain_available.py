import json
from urllib.error import HTTPError

from espionage.console.input import Input
from espionage.modules.parser.url_parser import UrlParser
from espionage.console import cAvailable
from urllib.request import urlopen, Request
from urllib.parse import urlencode


class DomainAvailable:
    __ENDPOINT__ = "https://madchecker.com/api/domain/get-information"

    def __init__(self, domain):
        self._domain = domain

    def domain_available(self) -> bool:

        domain = UrlParser(self._domain).for_md()
        params = {
            "domain": domain
        }
        query_string = urlencode(params)
        endpoint_url = self.__ENDPOINT__ + "?" + query_string
        try:
            endpoint_request = Request(
                endpoint_url,
                None,
                headers={
                    'User-Agent': str(
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'),
                }
            )
            with urlopen(endpoint_request) as response:
                response_text = response.read()
                content = json.loads(response_text)
                if "domain" in content:
                    domain_details = content["domain"]
                    available = domain_details["available"]
                    if available:
                        return True
                    else:
                        return False
                return False
        except HTTPError as e:
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
