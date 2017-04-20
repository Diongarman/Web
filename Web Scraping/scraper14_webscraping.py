__author__ = 'diongarman'
import urllib
import urlparse
from bs4 import BeautifulSoup
import mechanize

url = "http://nytimes.com"

urls = [url] #queue
visited = [url] #record
br = mechanize.Browser()

while len(urls) > 0:
    try:
        br.open(urls[0])
        #id broken link, we will go to except block and see the link. Good way to check site
        urls.pop(0) #now is open we can kick it out the pending jobs
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url, link.url)
            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                print newurl
    except:
        print 'error opening: %s' % urls[0]
        urls.pop(0)

