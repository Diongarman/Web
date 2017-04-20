__author__ = 'diongarman'

import urllib
import re

# The inefficient way:

# html = urllib.urlopen('https://www.google.co.uk/finance?q=NFLX').read()
# regex = '<span id="ref_[^.]*_l">(.+?)</span>'
#
# #<span id="ref_[^.]*_l" class="unchanged"><span class="unchanged">(.+?)</span><span>5</span></span>
# pattern = re.compile(regex)
# results = re.findall(pattern, html)
#
# print results

# Too much network latency though, a quicker way is to investigate network tab in devtools for
# a nonpublic link that serves raw data
# The efficient way:

html = urllib.urlopen('https://www.google.co.uk/finance/getprices?q=NFLX&x=NASD&i=120&p=25m&f=0,l&df=cpct&auto=1&ts=1480613997186&ei=EF5AWJDcJYfOUfvTpLAM').read()
print html
print html.split()[-1]

