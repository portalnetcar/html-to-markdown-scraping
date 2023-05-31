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

class MarkdownGenerator:
    def __init__(self):
        self.md_content = ''
        self.image_counter = 0  # To keep track of image numbers
        self.ssl_context = ssl._create_unverified_context()

    def handle_node(self, node):
        if node.name == 'img':
            # Handle image node
            img_url = node['src']
            
            # Download image, ignoring SSL certificate validation
            with urllib.request.urlopen(img_url, context=self.ssl_context) as response, open(f'images/image_{self.image_counter}.jpg', 'wb') as out_file:
                data = response.read()  # a `bytes` object
                out_file.write(data)
            
            # Append image to markdown
            self.md_content += f'![Image {self.image_counter}](images/image_{self.image_counter}.jpg)\n\n'
            self.image_counter += 1
        elif node.name is None:
            # Append text node to markdown
            self.md_content += node + '\n\n'
        elif node.name == 'code':
            # Handle code block
            self.md_content += '```\n' + node.get_text() + '\n```\n\n'
        elif node.name == 'a':
            # Handle link
            self.md_content += f'[{node.get_text()}]({node["href"]})\n\n'
        else:
            # Recursively handle children of other nodes
            for child in node.children:
                self.handle_node(child)



    def generate_markdown(self, url, css_selector):
        # Fetch the content from url, ignoring check of SSL certificate
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the article section by css selector
        article = soup.select(css_selector)

        # Create a directory for images
        if not os.path.exists('images'):
            os.makedirs('images')

        for section in article:
            self.handle_node(section)

        # Write to markdown file
        with open('article.md', 'w') as f:
            f.write(self.md_content)

url = 'https://...'
css_selector = 'article'  # replace this with your actual CSS selector
generator = MarkdownGenerator()
generator.generate_markdown(url, css_selector)
