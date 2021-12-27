import requests

from bs4 import BeautifulSoup

from espionage.modules.parser.url_parser import UrlParser
from espionage.console.input import Input
from espionage.console.c_dbdata import CDBData


class DomainBigData:
    """
    This class provides function which downloads whois records from domainbigdata and then parses
    this downloaded html content and extracts useful information from content, following is
    example of domain cnn.cn
    """
    extended_report = True

    def __init__(self):
        """
        Data initialization for domain big data request
        """
        str_cookie = "cookie"
        self.__cookies = {
            f'{str_cookie}consent_dismissed': 'yes',
        }
        self.__headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Referer': 'https://domainbigdata.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    @staticmethod
    def __extract_table_data__(div_data, record_info):
        """
        This function extracts table data from given html div into list and dictionary
        :param div_data: html div data extracted from html content
        :type div_data: soup
        :param record_info: dictionary for record
        :type record_info: dict
        :return: a dictionary type record is returned
        :rtype: dict
        """
        if not div_data.find('table'):
            return {}

        tables = div_data.findChildren('table')
        if not tables or len(tables) < 1:
            return {}

        table_card = tables[0]
        rows = table_card.findChildren(['th', 'tr'])
        for row in rows:
            cells = row.findChildren('td')
            _web_record = []
            for cell in cells:
                if cell.text:
                    value = cell.text.rstrip().strip()
                    if value and "Check abuses from" not in value:
                        _web_record.append(value)
            if len(_web_record) > 1:
                _extracted_value = _web_record[1]
                record_info[_web_record[0]] = _extracted_value

        return record_info

    def __website_info__(self, html_soup):
        """
        This function extracts website basic whois information from given div based on class
        :param html_soup: html content
        :type html_soup: soup
        :return: dictionary is returned
        :rtype: dict
        """
        website_info = {}
        website_cards = html_soup.find(id="idCardWebsite")
        website_info = self.__extract_table_data__(website_cards, website_info)

        return website_info

    @staticmethod
    def __extract_tld__(html_soup) -> list:
        """
        This function extracts links from whois data. These links are tld of searched domain.
        :param html_soup: html soup object from bs4 library
        :type html_soup: soup
        :return: A list is returned with data added in it
        :rtype: list
        """
        extracted_tld = []
        tld_cards = html_soup.find(id="MainMaster_divOtherTLD")
        links = tld_cards.findChildren("a")
        for link in links:
            extracted_tld.append(link.string)
        return extracted_tld

    def __extract_registrant__(self, html_soup):
        """
        Extract registrant information from whois dataset
        :param html_soup: html soup object from bs4 library
        :type html_soup: soup
        :return: A list is returned with data added in it
        :rtype: list
        """
        card_registrant = {}
        _card_registrant = html_soup.find(id="idCardRegistrant")
        card_registrant = self.__extract_table_data__(_card_registrant, card_registrant)
        return card_registrant

    @staticmethod
    def __whois_data__(whois):
        """
        This function extracts raw whois data from whois html content.
        :param whois: html soup object
        :type whois: soup
        :return: a list of raw text split based on new line
        :rtype: list
        """
        raw_text = whois.find(attrs={"class": "col-md-12 pd5 mt10"}, )
        raw_text = raw_text.decode_contents().rstrip()
        raw_text = "\n".join(line.strip() for line in raw_text.split("<br/>"))
        raw_text = raw_text.split("\n")
        return raw_text

    def __extract_raw_text__(self, html_soup):
        """
         This function extracts raw whois data from whois html content.
        :param html_soup:  html soup object
        :type html_soup: soup
        :return:  a list of raw text split based on new line
        :rtype: list
        """
        raw_text = []
        whois = html_soup.find(id="MainMaster_divWhois")
        if whois:
            data = self.__whois_data__(whois)
            if data:
                raw_text = data
        return raw_text

    @staticmethod
    def __extract_name_server__(html_soup):
        """
        This function loops through html soup object and extracts nameservers. These nameservers
        are appended into list and then added into dictionary.
        :param html_soup: html input
        :type html_soup: soup
        :return: name servers records in dictionary
        :rtype: dict
        """
        name_server = {}
        name_servers = html_soup.find(id="ns")
        tables = name_servers.findChildren('table')
        for table_card in tables:
            title = ""
            rows = table_card.findChildren(['th', 'tr'])
            name_servers = []
            for row in rows:
                cells = row.findChildren('td')
                _web_record = []
                for cell in cells:
                    if cell.string:
                        value = cell.string.rstrip().strip()
                        if value:
                            _web_record.append(value)
                if _web_record and _web_record not in name_servers:
                    title = _web_record[0]
                    name_servers.append(_web_record)
            if "-" in title:
                title = "History"
            name_server[title] = name_servers
        return name_server

    def __extract_history__(self, html_soup):
        """
        This function loops through html soup and extract history from whois record.
        :param html_soup: html soup object as  input
        :type html_soup: soup
        :return: previous whois history
        :rtype: list
        """
        history = []
        _domain_histories = html_soup.find_all(id="divRptHistoryMain")
        for _history in _domain_histories:
            history_record = {}
            recorded_at = _history.find("h2").string
            if recorded_at:
                card_registrant = {}
                recorded_at = str(recorded_at).replace("Recorded : ", "")
                history_record["recorded_date"] = recorded_at
                card_registrant = self.__extract_table_data__(_history, card_registrant)
                history_record["registrant"] = card_registrant
                history_record["whois_data"] = self.__whois_data__(_history)

            history.append(history_record)
        return history

    def __extract_results__(self, html_content):
        """
        This function call different submodules used to extract data from html content.
        :param html_content: html content downloaded from website or read from file
        :type html_content: str | bytes
        :return: dictionary is returned with whois data information
        :rtype: dict | None
        """
        domain_details = {}
        soup = BeautifulSoup(html_content, 'html.parser')

        basic_info = self.__website_info__(soup)

        if basic_info:
            domain_details["basic_info"] = basic_info
        if self.extended_report:
            more_tld = self.__extract_tld__(soup)
            if more_tld:
                domain_details["other_tld"] = more_tld
            whois_data = self.__extract_raw_text__(soup)
            if whois_data:
                domain_details["whois_data"] = whois_data
            historic_data = self.__extract_history__(soup)
            if historic_data:
                domain_details["historic_data"] = historic_data
        registrant_info = self.__extract_registrant__(soup)
        if registrant_info:
            domain_details["registrant_info"] = registrant_info
        name_server = self.__extract_name_server__(soup)
        if name_server:
            domain_details["name_server"] = name_server

        return domain_details

    def with_domain_name(self, user_domain, extended_report=False):
        """
        Function which receives domain name as input and search it's record on domain big data
        website. Later we parse this data with bs4 library. All data is converted into lists
        and dictionaries.
        :param user_domain: input from user
        :type user_domain: str
        :param extended_report: User want extended output like tlds, whois histories,
        :type extended_report: bool
        :return: a dictionary is crafted with whois data
        :rtype: dict | None
        """
        domain_bigdata = {}
        self.extended_report = extended_report
        if not user_domain:
            return domain_bigdata
        url_parser = UrlParser(user_domain)
        user_domain = url_parser.for_dbd()
        with requests.get(f'https://domainbigdata.com/{user_domain}', headers=self.__headers,
                          cookies=self.__cookies) as response:
            result_status = response.status_code
            if result_status == 200:
                domain_bigdata = self.__extract_results__(response.content)

        return domain_bigdata


if __name__ == '__main__':
    _input = Input()
    domain = _input.domain
    _domain_big_data = DomainBigData()
    if isinstance(domain, str):
        result = _domain_big_data.with_domain_name(domain, _input.extended)

        if result:
            c_data = CDBData()
            c_data.print(whois=result)

    elif isinstance(domain, list):
        for _domain in domain:
            result = _domain_big_data.with_domain_name(_domain, _input.extended)
            if result:
                c_data = CDBData()
                c_data.print(whois=result)
