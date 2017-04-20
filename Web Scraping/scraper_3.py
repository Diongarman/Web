__author__ = 'diongarman'

import urllib
import re
import csv

# symbolfile = open("companylist.csv").read()

with open('companylist.csv') as symbolfile:
    readCSV = csv.reader(symbolfile, delimiter=',')
    names = []
    for row in readCSV:
        name = row[0]


        names.append(name)

print(names[1:])

#this code is a linear implementation, i.e one request at a time

for x in names[1:]:
    html = urllib.urlopen('https://uk.finance.yahoo.com/q?s=%s&ql=1' % x).read()
    #either of the below regex variabes work in this program
    #regex = '<span id="yfs_l84_%s">(.+?)</span>' % x.lower()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, html)
    if len(price):
        print 'The price of',x ,'is:', price[0]
    else:
        print 'The price of',x ,'does not exist'
