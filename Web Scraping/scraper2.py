__author__ = 'diongarman'

import urllib
import re


symbols= ['AAPL', 'SPY', 'GOOG', 'NFLX']


for x in symbols:
    html = urllib.urlopen('https://uk.finance.yahoo.com/q?s=%s&ql=1' % x).read()
    regex = '<span id="yfs_l84_%s">(.+?)</span>' % x.lower()
    pattern = re.compile(regex)
    price = re.findall(pattern, html)
    print 'The price of',x ,'is:', price[0]
