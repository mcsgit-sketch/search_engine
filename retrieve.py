import requests 
from bs4 import BeautifulSoup



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
        return ""

def get_links(html): 
    links = [] 
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def main(): 
    print(get_links(get_html(url)))




if __name__ == "__main__": 
    main()
