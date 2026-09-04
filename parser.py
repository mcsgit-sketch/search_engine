import requests
from bs4 import BeautifulSoup


custom_header = {
        "User-Agent": "MySearchEngineBot (mscgit@gmail.com)"
        }

# could simplify things further by having get_html return a soup instead of html (change it to get_page instead)
def get_html(url): 
    try:  

        response = requests.get(url, headers=custom_header, timeout=10)
        response.raise_for_status()
        
        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type.lower():
            return None

        return response.text
    except requests.RequestException as e: 
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_title(soup): 
    title = ""
    if soup.title is not None: 
        title = soup.title.string
    return title

def get_text(soup):
    return soup.get_text(" ", strip=True)

