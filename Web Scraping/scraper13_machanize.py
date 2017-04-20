__author__ = 'diongarman'
import urllib
import urlparse
from bs4 import BeautifulSoup
import mechanize

# Try other deeper urls deeper than the root e.g. http://nytimes.com/pages/todayspaper/
url = "http://nytimes.com/pages/todayspaper/"

# mechanize is a simulated browser
br = mechanize.Browser()
br.open(url)

for link in br.links():
    # print "The base url is: %s and the url is: %s" % (link.base_url, link.url)
    newurl = urlparse.urljoin(link.base_url, link.url)
    print newurl

# People aren't always going to write out full url, so mechanize is useful. Because we will be going up and down directories because people us ../ etc. for directory movement


# remember the statediagrams to understand how we can traverse a site through going up, down and looping on pages: https://www.youtube.com/watch?v=bl6whQwdLXk&index=15&list=PLgGfaPLP959bTiKYokXPkO15atkXYyYOz