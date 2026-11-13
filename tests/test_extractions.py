"""Unit tests for the Regex extraction project."""

import sys
import unittest
from pathlib import Path

# Allow importing main.py when tests are run from the project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import extract_data


class TestDataExtraction(unittest.TestCase):
    def test_extracts_valid_emails_and_ignores_broken_addresses(self):
        text = (
            "jemimawavinya89@gmail.com "
            "firstname.lastname@company.co.uk "
            "jemima+business@gmail.com "
            "user@ @example.com user@com"
        )
        self.assertEqual(
            extract_data(text)["Email addresses"],
            [
                "jemimawavinya89@gmail.com",
                "firstname.lastname@company.co.uk",
                "jemima+business@gmail.com",
            ],
        )

    def test_extracts_http_and_https_urls(self):
        text = (
            "https://www.example.com "
            "https://subdomain.example.org/page "
            "https://example.com/guide?ref=nav#intro. "
            "www.example.com ftp://files.example.com"
        )
        self.assertEqual(
            extract_data(text)["URLs"],
            [
                "https://www.example.com",
                "https://subdomain.example.org/page",
                "https://example.com/guide?ref=nav#intro",
            ],
        )

    def test_extracts_supported_phone_formats_only(self):
        text = (
            "(123) 456-7890 123-456-7890 123.456.7890 "
            "1234567890 12-345-6789"
        )
        self.assertEqual(
            extract_data(text)["Phone numbers"],
            ["(123) 456-7890", "123-456-7890", "123.456.7890"],
        )

    def test_extracts_currency_formats_and_ignores_invalid_examples(self):
        text = "$19.99 $1,234.56 $5 $1,000,000.00 19.99 USD 5 $12.345"
        self.assertEqual(
            extract_data(text)["Currency amounts"],
            ["$19.99", "$1,234.56", "$5", "$1,000,000.00"],
        )

    def test_extracts_hashtags(self):
        text = "#JemimaCodes #SoftwareEngineering #TechForGood # #123NotAHashtag"
        self.assertEqual(
            extract_data(text)["Hashtags"],
            ["#JemimaCodes", "#SoftwareEngineering", "#TechForGood"],
        )


if __name__ == "__main__":
    unittest.main()
