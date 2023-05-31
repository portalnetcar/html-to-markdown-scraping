import requests
from bs4 import BeautifulSoup
import mistune
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Set `verify=False` on `requests.post`.
#requests.post(url='https://example.com', data={'bar':'baz'}, verify=False)

# Step 1: Extract content from the target website
url = 'https://...'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.3"
}
response = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

article = soup.find('div')
title = article.find('header').text
content_parts = []

articles = article.find('article').text
for article in articles:
    cont_ul = article
    content_parts.append(cont_ul)
    print(cont_ul)

content = ''.join(content_parts)

# Step 2: Convert the content into a Markdown file
markdown_title = f"# {title}\n\n"
markdown_content = mistune.markdown(content)
markdown_end_link = f"\n\n# Link: {url}\n\n"

with open('article.md', 'w') as file:
    file.write(markdown_title)
    file.write(markdown_content)
    file.write(markdown_end_link)

print("Article saved as article.md")