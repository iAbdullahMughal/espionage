import requests

from espionage import UrlParser
from bs4 import BeautifulSoup
import ipaddress


class DomainBigData:
    __EXTENDED_REPORT__ = True

    def __init__(self):
        self.__cookies = {
            'cookieconsent_dismissed': 'yes',
        }
        self.__headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://domainbigdata.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    @staticmethod
    def __extract_table_data__(div_data, record_info):
        tables = div_data.findChildren('table')
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
        website_info = {}
        website_cards = html_soup.find(id="idCardWebsite")
        website_info = self.__extract_table_data__(website_cards, website_info)

        return website_info

    @staticmethod
    def __extract_tld__(html_soup):
        extracted_tld = []
        tld_cards = html_soup.find(id="MainMaster_divOtherTLD")
        links = tld_cards.findChildren("a")
        for link in links:
            extracted_tld.append(link.string)
        return extracted_tld

    def __extract_registrant__(self, html_soup):
        card_registrant = {}
        _card_registrant = html_soup.find(id="idCardRegistrant")
        card_registrant = self.__extract_table_data__(_card_registrant, card_registrant)
        return card_registrant

    @staticmethod
    def __whois_data__(whois):
        raw_text = None
        try:
            raw_text = whois.find(attrs={"class": "col-md-12 pd5 mt10"}, )
            raw_text = raw_text.decode_contents().rstrip()
            raw_text = "\n".join(line.strip() for line in raw_text.split("<br/>"))
            raw_text = raw_text.split("\n")
        except:
            pass
        return raw_text

    def __extract_raw_text__(self, html_soup):
        raw_text = {}
        whois = html_soup.find(id="MainMaster_divWhois")
        if whois:
            data = self.__whois_data__(whois)
            if data:
                raw_text = data
        return raw_text

    @staticmethod
    def __extract_name_server__(html_soup):
        name_server = {}
        ns = html_soup.find(id="ns")
        tables = ns.findChildren('table')
        for table_card in tables:
            title = ""
            rows = table_card.findChildren(['th', 'tr'])
            ns = []
            for row in rows:
                cells = row.findChildren('td')
                _web_record = []
                for cell in cells:
                    if cell.string:
                        value = cell.string.rstrip().strip()
                        if value:
                            _web_record.append(value)
                if _web_record and _web_record not in ns:
                    title = _web_record[0]
                    ns.append(_web_record)
            if "-" in title:
                title = "History"
            name_server[title] = ns
        return name_server

    def __extract_history__(self, html_soup):
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
                try:
                    history_record["whois_data"] = self.__whois_data__(_history)
                except:
                    pass

            history.append(history_record)
        return history

    def __extract_results__(self, html_content):
        domain_details = {}

        soup = BeautifulSoup(html_content, 'html.parser')

        basic_info = self.__website_info__(soup)

        if basic_info:
            domain_details["basic_info"] = basic_info
        if self.__EXTENDED_REPORT__:
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

    def record_by_domain_address(self, domain, extended_report=False):
        domain_bigdata = {}
        self.__EXTENDED_REPORT__ = extended_report
        if not domain:
            raise "Domain address was not provided."
        url_parser = UrlParser(domain)
        domain = url_parser.for_dbd()
        with requests.get('https://domainbigdata.com/{}'.format(domain), headers=self.__headers,
                          cookies=self.__cookies) as response:
            result_status = response.status_code
            if result_status == 200:
                domain_bigdata = self.__extract_results__(response.content)

        return domain_bigdata

    def __whois_ip__(self, html_content):
        whois_ip = html_content.find(id="idIP")
        whois_record = {}
        whois_record = self.__extract_table_data__(whois_ip, whois_record)
        return whois_record

    @staticmethod
    def __website_on_ip__(html_content):
        site_on_same_ip = []
        tld_cards = html_content.find(id="MainMaster_divRptDomainsOnSameIP")
        links = tld_cards.findChildren("a")
        for link in links:
            site_on_same_ip.append(link.string)
        return site_on_same_ip

    def parse_ip_records(self, html_content=None):
        ip_details = {}
        r = open("content.html", "r")
        html_content = r.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        whois_ip = self.__whois_ip__(soup)

        if whois_ip:
            ip_details["basic_info"] = whois_ip
        sites_on_ip = self.__website_on_ip__(soup)

        if sites_on_ip:
            ip_details["sites_on_ip"] = sites_on_ip

        print(ip_details)

    def record_by_ip_address(self, ip_address):
        ip_bigdata = {}
        if not ip_address:
            raise "IP address was not provided."

        try:
            ipaddress.ip_address(ip_address)
        except ValueError:
            raise "Invalid ip address was provided"
        with requests.get('https://domainbigdata.com/{}'.format(ip_address), headers=self.__headers,
                          cookies=self.__cookies) as response:
            result_status = response.status_code
            if result_status == 200:
                print(response.content)
