import concurrent.futures

from espionage.console.input import Input
from espionage.modules import UrlParser
from espionage.console import cDetailedDns


class DetailedDns:
    """
    We will collect information about all the available domain name records. Later these records
    will be sent for json and console table output. We are collecting these dns records from 
    Following is the list of dns classes which are covered as part of this dns,
    Classes
    a       -> Host Address (A records)
    cert    -> Certificate (CERT records)
    dhcid     -> DHCP Identifier (DHCID records)
    cname     -> Canonical Name (CNAME records)
    aaaa    -> Pv6 Host Address (AAAA records)
    dlv     -> DNSSEC Lookaside Validation record (DLV records)
    dname     -> Delegation name (DNAME records)
    dnskey    -> DNS Key record (DNSKEY records)
    ds      -> Delegation Signer (DS records)
    hinfo     -> Host Information (HINFO records)
    hip     -> Host Identity Protocol (HIP records)
    kx      -> Key eXchanger record (KX records)
    loc     -> Location record (LOC records)
    mx      -> Mail Exchange record (MX records)
    naptr     -> Name Authority Pointer (NAPTR records)
    ns      -> Name Servers (NS records)
    nsec     -> Next-Secure record (NSEC records)
    nsec3     -> NSEC record version 3 (NSEC3 records)
    nsec3param-> NSEC3 parameters (NSEC3PARAM records)
    opt     -> Option record (OPT records)
    talink    -> Trust Anchor LINK (TALINK records)
    tlsa    -> TLSA records
    txt     -> Text record (TXT records)
    ta      -> DNSSEC Trust Authorities (TA records)
    rrsig     -> Resource Records Signature (RRSIG records)
    soa     -> Start of Authority (SOA record)
    spf     -> Sender Policy Framework (SPF records)
    srv     -> Service Locator (SRV records)
    sshfp     -> SSH Public Key Fingerprint (SSHFP records)
    above classes are part of this service.
    """

    __GET_AUTH__ = False
    __ACCEPT_VALUE__ = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avi' \
                       'f,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    def __init__(self, domain: str = None, get_authority: bool = False):
        """
        Initiating and assigning dns object with domain information.
        :param domain: domain which will be analyzed for records collection.
        :type domain: str
        :param get_authority: want to store authority information, default disabled
        :type get_authority: bool
        """
        self.__GET_AUTH__ = get_authority
        url_parser = UrlParser(domain)
        self._domain = url_parser.for_hs()

    def __add_auth__(self, content: dict, result: list) -> list:
        """
        This function will extract authority information from json response. It will store only 
        when function is set self.__get_auth=True else it will be ignored
        :param content: dict of records downloaded from server
        :type content:  dict
        :param result: list of records shared with function, data is stored in this list
        :type result: list
        :return: list of records
        :rtype: list
        """
        if self.__GET_AUTH__:
            if "authority" in content:
                authorities = content["authority"]
                for authority in authorities:
                    record = {
                        "name": authority["name"],
                        "type": authority["type"],
                        "class": authority["class"],
                        "ttl": authority["ttl"],
                        "endpoint": self.__extract_rdata__(authority["rdata"]),
                    }
                    if record not in result:
                        result.append(record)
        return result

    def __add_answer__(self, content: dict) -> list:
        """
        This function will parse the response from server. If we are answers against the query we 
        will pass information for processing.
        :param content: dict content downloaded from server against domain
        :type content: dict
        :return: list of records
        :rtype: list
        """
        result = []
        if "answer" not in content:
            return result
        answers = content["answer"]
        if not answers:
            return result
        for answer in answers:
            r_data = self.__extract_rdata__(answer["rdata"])
            if len(r_data) == 1:
                r_data = r_data[0]
            else:
                r_data = r_data
            record = {
                "name": answer["name"],
                "type": answer["type"],
                "class": answer["class"],
                "ttl": answer["ttl"],
                "endpoint": r_data,
            }
            if record not in result:
                result.append(record)

        return result

    @staticmethod
    def __extract_rdata__(rdata: str):
        """
        This function extract data from strings and make it readable in lists for different 
        classes.
        :param rdata: class endpoint data
        :type rdata: str
        :return: list of records found in endpoint
        :rtype: list | str
        """
        contents = str(rdata).split(" ")
        if len(contents) > 1:
            if "v=spf" in contents[0].lower() or len(contents) == 2:
                return [rdata]
            elif len(contents) == 7:
                return [{
                    "primary_nameserver": contents[0],
                    "host_master_email": contents[1],
                    "serial_number": contents[2],
                    "refresh": contents[3],
                    "retry": contents[4],
                    "expire": contents[5],
                    "minimum_ttl": contents[6],
                }]

            return rdata
        else:
            contents = [contents[0].replace('"', "")]
            return contents

    def __download_record__(self, endpoint, timeout=10):
        """
        We are calling this function for downloading records from each source. This function will
        generate network requests.
        :param endpoint: API endpoint from we are collecting information
        :type endpoint: str
        :param timeout: timeout value of network request
        :type timeout: int
        :return: a dictionary of records will be return to its parent caller
        :rtype:dict
        """
        import requests

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
                      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        result = {}
        try:
            response = requests.get(f'{endpoint}', headers=headers, verify=False, timeout=timeout)
            content = response.json()
            _answered = self.__add_answer__(content)
            result = self.__add_auth__(content, _answered)
        except Exception as e:
            print(f"error {e}")

        return result

    def dns_records(self) -> list:
        """
        This function create different threads by using multiprocessing, and it performs multiple api request from
        server, response is collected and parsed according usage. This function also slices data as per requirements
        we are ignoring different classes from api response.
        :return: a result dict is returned which contains records
        :rtype: list
        """
        dns_info = []
        endpoints = [
            "http://www.dns-lg.com/us01/" + self._domain + "/a",
            "http://www.dns-lg.com/us01/" + self._domain + "/cert",
            "http://www.dns-lg.com/us01/" + self._domain + "/dhc" + "id",
            "http://www.dns-lg.com/us01/" + self._domain + "/cname",
            "http://www.dns-lg.com/us01/" + self._domain + "/aa" + "aa",
            "http://www.dns-lg.com/us01/" + self._domain + "/dlv",
            "http://www.dns-lg.com/us01/" + self._domain + "/d" + "name",
            "http://www.dns-lg.com/us01/" + self._domain + "/dns" + "key",
            "http://www.dns-lg.com/us01/" + self._domain + "/ds",
            "http://www.dns-lg.com/us01/" + self._domain + "/h" + "info",
            "http://www.dns-lg.com/us01/" + self._domain + "/hip",
            "http://www.dns-lg.com/us01/" + self._domain + "/kx",
            "http://www.dns-lg.com/us01/" + self._domain + "/loc",
            "http://www.dns-lg.com/us01/" + self._domain + "/mx",
            "http://www.dns-lg.com/us01/" + self._domain + "/na" + "ptr",
            "http://www.dns-lg.com/us01/" + self._domain + "/ns",
            "http://www.dns-lg.com/us01/" + self._domain + "/opt",
            "http://www.dns-lg.com/us01/" + self._domain + "/n" + "sec3",
            "http://www.dns-lg.com/us01/" + self._domain + "/n" + "sec3param",
            "http://www.dns-lg.com/us01/" + self._domain + "/ta" + "link",
            "http://www.dns-lg.com/us01/" + self._domain + "/t" + "lsa",
            "http://www.dns-lg.com/us01/" + self._domain + "/txt",
            "http://www.dns-lg.com/us01/" + self._domain + "/ta",
            "http://www.dns-lg.com/us01/" + self._domain + "/rr" + "sig",
            "http://www.dns-lg.com/us01/" + self._domain + "/soa",
            "http://www.dns-lg.com/us01/" + self._domain + "/spf",
            "http://www.dns-lg.com/us01/" + self._domain + "/srv",
            "http://www.dns-lg.com/us01/" + self._domain + "/ssh" + "fp",
            "http://www.dns-lg.com/us01/" + self._domain + "/n" + "sec"
        ]

        with concurrent.futures.ThreadPoolExecutor(10) as executor:
            future_to_url = {executor.submit(self.__download_record__, url): url for url in endpoints}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    if result:
                        dns_info.append(result)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))

        return dns_info


if __name__ == '__main__':
    INPUT = Input()
    DOMAIN = INPUT.domain
    if isinstance(DOMAIN, str):
        DETAILED_DNS = DetailedDns(DOMAIN)
        RESULT = DETAILED_DNS.dns_records()
        CONSOLE = cDetailedDns()
        CONSOLE.print(RESULT)

    elif isinstance(DOMAIN, list):
        for _domain in DOMAIN:
            DETAILED_DNS = DetailedDns(_domain)
            RESULT = DETAILED_DNS.dns_records()
            CONSOLE = cDetailedDns()
            CONSOLE.print(RESULT)
            print("\n")