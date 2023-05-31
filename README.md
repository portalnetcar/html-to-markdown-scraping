## html-to-markdown-scraping

This Python script converts an HTML page into a Markdown file. It can be used for web scraping or archiving web pages in a mardown format that's easy to read and write.

The script is designed to be run from the command line and accepts two arguments: the URL of the web page to convert, and a selector that specifies which part of the page to convert.

## Dependencies
The script depends on the following Python packages:
```
requests for making HTTP requests
bs4 (BeautifulSoup4) for parsing HTML
html2text for converting HTML to Markdown
```
Run this command to checkand install dependencies on your system:
```
# Fetch and run the setup script
curl -fsSL https://raw.githubusercontent.com/portalnetcar/html-to-markdown-scraping/main/setup.sh | bash
```
## Scrapping
To run the code use this command for local dowloaded script:
```
python3 markdowner.py "https://pageurl" "section"
```
or to run without download:
```
#!/bin/bash

# Fetch and run the Python script
curl -sSL https://raw.githubusercontent.com/portalnetcar/html-to-markdown-scraping/main/markdowner.py | python3 - "https://pageurl" "section"

```
Enjoy 

Feel free to customize this README to fit your needs.

## Important

Please note that web scraping should be done responsibly and ethically. It's crucial to respect the copyright of the websites you are scraping. Just because data is publicly available doesn't mean it is legally available for all uses. Websites often have a "terms of service" or "robots.txt" file that may limit or prohibit web scraping. Additionally, laws about web scraping vary by country, so always ensure that you are scraping data in a way that is legal and respectful. If in doubt, it's a good practice to ask for permission before scraping data. This script is provided for educational purposes and should not be used to infringe on copyrights or violate any terms of service.

## Links

- https://www.baeldung.com/cs/web-crawling-vs-web-scraping