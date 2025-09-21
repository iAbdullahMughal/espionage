import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from espionage.modules.website.detailed_dns import DetailedDns


class TestDetailedDns(unittest.TestCase):
    """Detailed DNS record fetching tests."""

    def test_a_record_endpoint_is_trimmed(self):
        domain = "example.com"
        detailed_dns = DetailedDns(domain)
        requested_urls = []

        def fake_get(url, headers=None, verify=None, timeout=None):
            requested_urls.append(url)

            class DummyResponse:
                @staticmethod
                def json():
                    return {}

            return DummyResponse()

        with patch("requests.get", side_effect=fake_get):
            detailed_dns.dns_records()

        expected_endpoint = f"http://www.dns-lg.com/us01/{detailed_dns._domain}/a"
        self.assertIn(expected_endpoint, requested_urls)
        self.assertNotIn(expected_endpoint + "%20", requested_urls)


if __name__ == "__main__":
    unittest.main()
