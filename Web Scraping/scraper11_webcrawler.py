__author__ = 'diongarman'

# spider alog: queue of urls appended to stack
# creates a data structure that creates new pages and keeps a history of visited pages
import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://nytimes.com"

# stack: running total of pages we need to scrape
urls = [url]
# Queue: Historical record of urls
visited = [url]

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print urls[0]
    soup = BeautifulSoup(htmltext, "lxml")

    urls.pop(0)
    print len(urls)

    for tag in soup.findAll('a', href=True):
        # urljoin checks if there is a top level domain name, if not it appends one.
        tag['href'] = urlparse.urljoin(url, tag['href'])
        print tag['href']
        #below keeps us on same site
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href']) #temp list of jobs that need to be processed
            visited.append(tag['href']) #historica record
print visited



