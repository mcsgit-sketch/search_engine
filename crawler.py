from urllib.parse import urlsplit, urljoin, urlparse, urldefrag
import sqlite3
from parser import get_html, get_title, parse_html
from storage import create_db, store_page


# global variables 
urls = set() 


# function to retrive page html
url = "https://en.wikipedia.org/wiki/Machine_learning"

def get_links(soup, base_url): 
    links = set() 

    for link in soup.find_all('a'):
        link = str(link.get('href'))

        # link normalization 
        link = urljoin(base_url, link)
        link, _ = urldefrag(link)
        
        parsed = urlparse(link)
        if parsed.scheme not in ("http", "https"):
            continue

        links.add(link)
    return links

def main(): 
    print(get_links(get_html(url), url))




if __name__ == "__main__": 
    main()
