import requests
from bs4 import BeautifulSoup
import ssl
import os
import urllib.request
import urllib3

# Disable SSL warnings for urllib3, which is used by requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# To ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://cloudofthings.net/lab-10/'

# Fetch the content from url, ignoring check of SSL certificate
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the article section by css selector
article = soup.select('article')

# Create a directory for images
if not os.path.exists('images'):
    os.makedirs('images')

md_content = ''
for section in article:
    # Append text content to markdown
    md_content += section.get_text() + '\n\n'
    
    # Find all image tags
    images = section.find_all('img')

    # Create an unverified SSL context for image downloading
    ssl_context = ssl._create_unverified_context()

    for i, img in enumerate(images):
        img_url = img['src']
        
        # Download image, ignoring SSL certificate validation
        with urllib.request.urlopen(img_url, context=ssl_context) as response, open(f'images/image_{i}.jpg', 'wb') as out_file:
            data = response.read()  # a `bytes` object
            out_file.write(data)
        
        # Append image to markdown
        md_content += f'![Image {i}](images/image_{i}.jpg)\n\n'

# Write to markdown file
with open('article.md', 'w') as f:
    f.write(md_content)
