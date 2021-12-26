import unittest
from espionage.modules.osint.domain_available import DomainAvailable


class TestDomainAvailable(unittest.TestCase):
    def test_google_domain(self):
        domain = "www.google.com"
        domain_available = DomainAvailable(domain)
        self.assertEqual(domain_available.domain_available(), False)

    def test_iabdullahmughal_domain(self):
        domain = "www.iabdullahmughal.com"
        domain_available = DomainAvailable(domain)
        self.assertEqual(domain_available.domain_available(), True)


if __name__ == '__main__':
    unittest.main()
