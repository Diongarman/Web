__author__ = 'diongarman'

import urllib
import urlparse
from bs4 import BeautifulSoup

#filter out parametised urls, coz browser sends info relative to session id
# or other ps to the server over the url
# we don't want to request same url multiple times

htmltext = urllib.urlopen("http://nytimes.com")
soup = BeautifulSoup(htmltext, 'lxml')

for tag in soup.findAll('a', href=True):
    raw = tag['href']
    b1 = urlparse.urlparse(tag['href']).hostname
    b2 = urlparse.urlparse(tag['href']).path
    newurl = 'http://'+str(b1)+b2
    print newurl

