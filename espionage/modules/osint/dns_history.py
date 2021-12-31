import secrets
import time
import uuid
import requests

from bs4 import BeautifulSoup
from espionage.modules.parser.url_parser import UrlParser
from espionage.console.input import Input
from espionage.console import cDomainHistory


class DnsHistory:
    """
    DNS History class contains function which performs requests to download records from hoster
    stats website. Downloaded html is parsed and converted into dictionary record. This class will
    provide historical records for given domain address.
    """

    _domain = None
    _endpoint = 'http://www.hosterstats.com/historicaldns.php'

    def __init__(self, user_domain):
        """
        Init function with user given domain address
        :param user_domain: domain address
        :type user_domain: str
        """
        url_parser = UrlParser(user_domain)
        self._domain = url_parser.for_hs()

    def __download_record__(self):
        """
        We download report from internet against user domain. This function generates random
        cookie data and send request over the domain for data collection.
        :return: dict is returned to caller function
        :rtype: str
        """
        user_uuid = str(uuid.uuid4())
        user_b = int(time.time())
        user_l = user_b + 5280971
        device_uuid = str(uuid.uuid4())
        device_e = user_b + 500005280971
        session_uuid = str(uuid.uuid4())

        user_g = secrets.randbelow(2000000)
        cookies = {
            f'ab.storage.userId.{user_uuid}': f'%7B%22g%22%3A%22{user_g}%22%2C%22c%22%3A{user_b}'
                                              f'%2C%22l%22%3A{user_l}%7D',
            f'ab.storage.deviceId.{user_uuid}': f'%7B%22g%22%3A%22{device_uuid}%22%2C%22c%22%3A'
                                                f'{user_b}%2C%22l%22%3A{1638132006324}%7D',
            f'ab.storage.sessionId.{user_uuid}': f'%7B%22g%22%3A%22{session_uuid}%22%2C%22e%22%3A'
                                                 f'{device_e}%2C%22c%22%3A{user_b}%2C%22l%22%3A'
                                                 f'{user_l}%7D',
        }

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                          ' like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
                      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.hosterstats.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        params = (
            ('domain', f'{self._domain}'),
        )
        try:
            response = requests.get('http://www.hosterstats.com/historicaldns.php', headers=headers,
                                    params=params,
                                    cookies=cookies, timeout=8)
        except requests.exceptions.ConnectionError:
            return None
        except requests.exceptions.Timeout:
            return None

        if response.status_code == 200:
            html_report = response.content.decode("utf-8")
            return html_report
        return None

    @staticmethod
    def __convert_into_dict__(html_tables):
        """
        We convert html tables data into dictionary data. Html table contains dns history of
        given url.
        :param html_tables: soup object of html report downloaded against domain
        :type html_tables: soup
        :return: dns history returned as dictionary
        :rtype: dict
        """
        dns_history = {

        }
        for table in html_tables:
            if not table.has_attr("summary"):
                continue
            if "Domain Hosting History" not in str(table):
                continue
            rows = table.findChildren(['th', 'tr'])

            for row in rows:
                columns = row.findChildren('td')
                if len(columns) != 5:
                    continue
                columns = row.findChildren('td')
                old_server = str(columns[0].text).strip().rstrip().replace('\xa0', ' ')
                new_server = str(columns[1].text).strip().rstrip().replace('\xa0', ' ')
                month_year = str(columns[2].text).strip().rstrip().replace('\xa0', ' ')
                zone_date = str(columns[3].text).strip().rstrip().replace('\xa0', ' ')
                operation = str(columns[4].text).strip().rstrip().replace('\xa0', ' ')

                if month_year not in dns_history:
                    dns_history[month_year] = []

                data = {
                    "old server": old_server,
                    "new server": new_server,
                    "zone date": zone_date,
                    "operation": operation,
                }
                if data not in dns_history[month_year]:
                    dns_history[month_year].append(
                        data
                    )
        return dns_history

    def historical_data(self):
        """
        Function is used download dns history report from internet and then extract data from
        downloaded report.
        :return: a dictionary of records is returned to caller
        :rtype: dict
        """
        _historical_data = {}
        html_data = self.__download_record__()
        if not html_data:
            return _historical_data
        soup = BeautifulSoup(html_data, 'lxml')
        data_tables = soup.findAll("table")
        if not data_tables:
            return _historical_data
        _historical_data = self.__convert_into_dict__(data_tables)

        return _historical_data


if __name__ == '__main__':
    INPUT = Input()
    DOMAIN = INPUT.domain
    DOMAIN_HISTORY = DnsHistory(DOMAIN)
    if isinstance(DOMAIN, str):
        RESULTS = DOMAIN_HISTORY.historical_data()
        if RESULTS:
            CONSOLE = cDomainHistory()
            CONSOLE.print(DOMAIN_HISTORY.historical_data())

    elif isinstance(DOMAIN, list):
        for _domain in DOMAIN:
            RESULTS = DOMAIN_HISTORY.historical_data()
            if RESULTS:
                CONSOLE = cDomainHistory()
                CONSOLE.print(DOMAIN_HISTORY.historical_data())
