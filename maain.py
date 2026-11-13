#!/usr/bin/env python3
"""Extract emails, URLs, phone numbers, currency amounts, and hashtags from text."""

import re
from pathlib import Path

# The patterns are deliberately limited to the formats described in the assignment.
PATTERNS = {
    "Email addresses": re.compile(
        r"(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
        r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)*"
        r"\.[A-Za-z]{2,}(?![A-Za-z0-9_-])"
    ),
    "URLs": re.compile(
        r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        r"(?::\d{1,5})?(?:/[^\s<>\"']*)?",
        re.IGNORECASE,
    ),
    "Phone numbers": re.compile(
        r"(?<!\d)(?:"
        r"\(\d{3}\)\s\d{3}-\d{4}"
        r"|\d{3}-\d{3}-\d{4}"
        r"|\d{3}\.\d{3}\.\d{4}"
        r")(?!\d)"
    ),
    "Currency amounts": re.compile(
        r"(?<![A-Za-z0-9.])\$(?:\d{1,3}(?:,\d{3})+|\d+)"
        r"(?:\.\d{2})?(?![\d.])"
    ),
    "Hashtags": re.compile(r"(?<![A-Za-z0-9_])#[A-Za-z][A-Za-z0-9_]*"),
}


def extract_data(text):
    """Return all matches for each supported data type."""
    results = {}
    for category, pattern in PATTERNS.items():
        matches = pattern.findall(text)

        # URLs in prose may be followed immediately by sentence punctuation.
        if category == "URLs":
            matches = [match.rstrip(".,!?;:") for match in matches]

        results[category] = matches
    return results


def main():
    """Read the sample input file and print extracted values."""
    input_path = Path(__file__).with_name("test_data.txt")

    try:
        sample_text = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Could not find {input_path.name}. Keep it in the same folder as main.py.")
        return

    results = extract_data(sample_text)

    print("=" * 12 + " DATA EXTRACTION RESULTS " + "=" * 12)
    for category, matches in results.items():
        print(f"\n{category.upper()} ({len(matches)} found):")
        if matches:
            for match in matches:
                print(f"  - {match}")
        else:
            print("  No matches found.")
    print("\n" + "=" * 15 + " EXTRACTION COMPLETE " + "=" * 15)


if __name__ == "__main__":
    main()
