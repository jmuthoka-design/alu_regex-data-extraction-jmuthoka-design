

A Python project that uses regular expressions (Regex) to extract five types of information from a text file:

1. Email addresses
2. URLs (HTTP and HTTPS)
3. Phone numbers
4. Currency amounts
5. Hashtags

The project uses Python's built-in "re" module. It reads text from "test_data.txt", searches for matches, and prints the results in the terminal.

## Project structure
alu_regex-data-extraction-jmuthoka-design/
├── main.py
├── test_data.txt
├── README.md
└── tests/
    └── test_extraction.py



 How to run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   
   python3 main.py
   

The program reads "test_data.txt" from the same folder as "main.py" and prints the extracted values.

How to run the tests

Run:
python3 -m unittest discover -s tests -v


 Regex patterns and supported formats

| Data type | Examples supported |
|---|---|
| Email addresses | `jemimawavinya89@gmail.com`, `firstname.lastname@company.co.uk`, `jemima+business@gmail.com` |
| URLs | `https://www.example.com`, URLs with paths, query strings and fragments |
| Phone numbers | `(123) 456-7890`, `123-456-7890`, `123.456.7890` |
| Currency amounts | `$19.99`, `$1,234.56`, `$5`, `$1,000,000.00` |
| Hashtags | `#JemimaCodes`, `#SoftwareEngineering` |

The sample input also contains malformed examples, such as "user@", "@example.com", "1234567890", and "$12.345", to check that the patterns do not accept those examples.

 Notes and limitations

- These patterns are designed for the formats listed in the assignment. They are not intended to validate every possible email address, URL, telephone numbering plan, or currency format in the world.
- The phone number examples use a 3-digit area code and 7-digit local number, as shown in the assignment.
- The URL pattern extracts HTTP and HTTPS links. It intentionally does not extract bare domains such as `www.example.com` or FTP addresses.
- Currency examples use the dollar sign and either whole amounts or amounts with exactly two decimal places.
- The email addresses, URLs, and phone numbers in "test_data.txt" are sample test data. 



