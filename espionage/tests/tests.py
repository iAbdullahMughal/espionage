import unittest
from espionage.modules.osint.domain_available import DomainAvailable
from espionage.modules.osint.domain_big_data import DomainBigData


class TestDomainAvailable(unittest.TestCase):
    """Domain available unittest cases."""

    def test_google_domain(self):
        domain = "www.google.com"
        domain_available = DomainAvailable(domain)
        self.assertEqual(domain_available.domain_available(), False)

    def test_iabdullahmughal_domain(self):
        domain = "www.iabdullahmughal.com"
        domain_available = DomainAvailable(domain)
        self.assertEqual(domain_available.domain_available(), True)


class TestDomainBigData(unittest.TestCase):
    """ DomainBigData test cases."""

    def test_google_domain(self):
        domain = "www.google.com"
        domain_available = DomainBigData()
        stored_record = {'basic_info': {'Date creation': '1997-09-15',
                                        'Domain': 'google.com',
                                        'IP Address': '172.217.13.206',
                                        'IP Geolocation': 'United States, California, '
                                                          'Mountain View',
                                        'Title': 'Google',
                                        'Web age': '24 years and 3 months',
                                        'Words in': 'go ogle'},
                         'name_server': {'A': [['A', 'google.com', '142.250.65.206', '300', 'IN']],
                                         'AAAA': [['AAAA',
                                                   'google.com',
                                                   '2607:f8b0:4006:80f::200e',
                                                   '300',
                                                   'IN']]}}
        record_keys = len(stored_record)  # There are two keys basic_info and name_server

        self.assertEqual(len(domain_available.with_domain_name(user_domain=domain)), record_keys)


if __name__ == '__main__':
    unittest.main()
