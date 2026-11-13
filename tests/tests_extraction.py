

import unittest

from main import extract_data


class TestExtractions(unittest.TestCase):
    def test_emails(self):
        text = (
            "Contact jemimawavinya89@gmail.com or "
            "jemima.muthoka@company.co.uk. Invalid: user@, @example.com"
        )
        results = extract_data(text)
        self.assertEqual(
            results["Email addresses"],
            ["jemimawavinya89@gmail.com", "jemima.muthoka@company.co.uk"],
        )

    def test_urls(self):
        text = (
            "Visit https://example.com/page and "
            "http://sub.example.org/path?q=1. "
            "Invalid: www.example.com and ftp://example.com"
        )
        results = extract_data(text)
        self.assertEqual(
            results["URLs"],
            ["https://example.com/page", "http://sub.example.org/path?q=1"],
        )

    def test_phone_numbers(self):
        text = (
            "(123) 456-7890, 123-456-7890, 123.456.7890; "
            "invalid: 1234567890, 12-345-6789"
        )
        results = extract_data(text)
        self.assertEqual(
            results["Phone numbers"],
            ["(123) 456-7890", "123-456-7890", "123.456.7890"],
        )

    def test_currency(self):
        text = "$19.99, $1,234.56, $5, $1,000,000.00; invalid: 19.99, $12.345"
        results = extract_data(text)
        self.assertEqual(
            results["Currency amounts"],
            ["$19.99", "$1,234.56", "$5", "$1,000,000.00"],
        )

    def test_hashtags(self):
        text = "#JemimaCodes #SoftwareEngineering #TechForGood # #123NotAHashtag"
        results = extract_data(text)
        self.assertEqual(
            results["Hashtags"],
            ["#JemimaCodes", "#SoftwareEngineering", "#TechForGood"],
        )


if __name__ == "__main__":
    unittest.main()
