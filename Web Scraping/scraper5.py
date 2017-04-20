__author__ = 'diongarman'

import urllib
import json


# had issues finding this link using the network>xhr in chrome devtools
html = urllib.urlopen('http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US')
data = json.load(html)

print data
print "last price was: ", data["last_price"]
