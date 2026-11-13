"""Extract emails, URLs, phone numbers, currency amounts, and hashtags."""

import re
from pathlib import Path

PATTERNS = {
    "Emails": re.compile(
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
        r"(?<!\d)(?:\(\d{3}\)\s\d{3}-\d{4}|"
        r"\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})(?!\d)"
    ),
    "Currency amounts": re.compile(
        r"(?<![A-Za-z0-9.])\$(?:\d{1,3}(?:,\d{3})+|\d+)"
        r"(?:\.\d{2})?(?![\d.])"
    ),
    "Hashtags": re.compile(r"(?<![A-Za-z0-9_])#[A-Za-z][A-Za-z0-9_]*"),
}


def extract_data(text):
    """Return all supported data matches found in the supplied text."""
    results = {}

    for category, pattern in PATTERNS.items():
        matches = pattern.findall(text)

        # Remove common punctuation that may follow a URL in a sentence.
        if category == "URLs":
            matches = [match.rstrip(".,!?;:") for match in matches]

        results[category] = matches

    return results


def main():
    """Read the sample text file and print extracted information."""
    input_file = Path(__file__).with_name("test_data.txt")

    if not input_file.exists():
        print("Error: test_data.txt was not found.")
        return

    text = input_file.read_text(encoding="utf-8")
    results = extract_data(text)

    print("REGEX DATA EXTRACTION RESULTS")
    print("=" * 32)

    for category, matches in results.items():
        print(f"\n{category}:")
        if matches:
            for match in matches:
                print(f"  - {match}")
        else:
            print("  No matches found.")


if __name__ == "__main__":
    main()
