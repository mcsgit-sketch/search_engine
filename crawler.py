from urllib.parse import urlsplit, urljoin, urlparse, urldefrag
from parser import get_html, get_title, parse_html, get_text
from storage import create_db, store_page
from collections import deque

# url queue
urls = deque(["https://www.nytimes.com/", "https://www.bbc.com/", 
        "https://www.reddit.com/", "https://www.ycombinator.com/", 
        "https://www.usa.gov/", "https://github.com/", 
        "https://www.reuters.com/", 
        "https://en.wikipedia.org/wiki/Main_Page"])

#store seen (visited) links
# can this be done by adding a "visited?" column in the database to have the memory persist
seen = set()

def get_links(soup, base_url): 
    links = set() 

    for link in soup.find_all('a'):
        link = str(link.get('href'))

        # link normalization 
        link = urljoin(base_url, link)
        link, _ = urldefrag(link)
        
        if not should_crawl(link): 
            continue
        links.add(link)
    return links


def should_crawl(url): 
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False 

    blocked_extensions = (".jpg", ".jpeg", ".png", ".gif", 
                          ".pdf", ".zip", ".mp4", ".mp3")
    
    if parsed.path.lower().endswith(blocked_extensions): 
        return False 

    return True 

def crawl(url):
    html = get_html(url)
    if html is None: 
        return False 

    soup = parse_html(html)
    
    title = get_title(soup)
    if title == "":
        return False
    
    text = get_text(soup)
    
    for link in get_links(soup, url):
        if link not in seen: 
            urls.append(link)
    seen.add(url)
    store_page(url, title, text)

    return True

def crawling(limit): 
    crawl_count = 0
    while urls and crawl_count < limit:
        current_url = urls.popleft()
        if current_url in seen: 
            continue

        if crawl(current_url): 
            crawl_count = crawl_count + 1
    return "success"

def main(): 
    #    print(get_links(get_html(url), url))
    create_db()
    print(crawling(10))




if __name__ == "__main__": 
    main()
