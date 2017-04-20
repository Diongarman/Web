__author__ = 'diongarman'

import urllib
import re


urls = ['http://google.com', 'http://yahoo.com', 'http://nytimes.com', 'http://youtube.com', 'http://twitter.com']
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

for x in urls:
    html = urllib.urlopen(x).read()
    titles = re.findall(pattern, html)
    print titles


