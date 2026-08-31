import requests 
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin, urlparse, urldefrag
import sqlite3

# function to retrive page html
url = "https://en.wikipedia.org/wiki/Machine_learning"

custom_header = {
        "User-Agent": "MySearchEngineBot (mscgit@gmail.com)"
        }


def get_html(url): 
    response = requests.get(url, headers=custom_header)
    if response.status_code == 200:
        html_content = response.text
        return html_content
    else: 
        print(f"Failed to retrieve the page.\n Status code: {response.status_code}")
        return None

def get_links(html): 
    links = set() 
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        link = str(link.get('href'))

        # link normalization 
        link = urljoin(url, link)
        link, _ = urldefrag(link)
        
        parsed = urlparse(link)
        if parsed.netloc != "en.wikipedia.org":
            continue
        if not parsed.path.startswith("/wiki/"):
            continue

        links.add(link)
    return links

def main(): 
    print(get_links(get_html(url)))




if __name__ == "__main__": 
    main()
