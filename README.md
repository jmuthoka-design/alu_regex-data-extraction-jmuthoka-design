# Regex Data Extraction

## Project overview
This Python project uses regular expressions (Regex) and Python's built-in `re` module to extract five types of information from a text file:

1. Email addresses
2. HTTP/HTTPS URLs
3. Phone numbers in three formats
4. Dollar currency amounts
5. Hashtags

## Project structure
```text
alu_regex-data-extraction-jmuthoka-design/
├── main.py
├── test_data.txt
├── README.md
└── tests/
    └── test_extractions.py
```

## Requirements
- Python 3
- No third-party packages are required.

## Run the program
Open a terminal in the project folder and run:

```bash
python3 main.py
```

The program reads `test_data.txt`, applies the five regular-expression patterns, and prints the matches by category.

## Example output

Running `python3 main.py` with the included `test_data.txt` produces:

```text
REGEX DATA EXTRACTION RESULTS


Email addresses:
  - jemimawavinya89@gmail.com
  - jemima.muthoka@company.co.uk
  - jemima+business@gmail.com

URLs:
  - https://www.jemimawavinya.com
  - https://example.com/portfolio/projects?ref=profile#about

Phone numbers:
  - (123) 456-7890
  - 123-456-7890
  - 123.456.7890

Currency amounts:
  - $19.99
  - $1,234.56
  - $5
  - $1,000,000.00

Hashtags:
  - #JemimaCodes
  - #SoftwareEngineering
  - #TechForGood
```

## Run the tests
From the project folder, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests check valid examples and confirm that several malformed examples are not extracted.

## Supported formats and limitations
- Email addresses: common email-address formats with a domain and extension.
- URLs: HTTP and HTTPS addresses with optional ports and paths. Bare domains and FTP links are not included.
- Phone numbers: `(123) 456-7890`, `123-456-7890`, and `123.456.7890` (US-style 10-digit formats).
- Currency: dollar amounts such as `$19.99`, `$1,234.56`, and `$5`.
- Hashtags: a `#` followed by a letter and then letters, digits, or underscores.

These patterns are designed for the assignment examples. They are practical extraction patterns. 


