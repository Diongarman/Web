__author__ = 'diongarman'
import csv
import re
import urllib
from threading import Thread
import MySQLdb

with open('companylist.csv') as symbolfile:
    readCSV = csv.reader(symbolfile, delimiter=',')
    symbols = []
    for symbol in readCSV:
        symbols.append(symbol[0])

# print symbols[1:]


gmap = {}
#  reason use a func is because we need seperate memory allocation for each thread.
def th(sym):
    base = 'https://uk.finance.yahoo.com/q?s=%s&ql=1' % sym
    regex = '<span id="yfs_l84_%s">(.+?)</span>' % sym.lower()
    pattern = re.compile(regex)
    html = urllib.urlopen(base).read()
    results = re.findall(pattern, html)
    try:
        gmap[str(sym)] = results[0]
    except:
        print 'got an error'


# a data structure to store thread objects so we can join threads after we have run everything, so to correctly de-allocate memory
threadList = []

# for each symbol create a thread
for symbol in symbols[1:50]:
    t = Thread(target=th,args=(symbol,))
    t.start()
    threadList.append(t)

# after we have started all the threads we have to join them back to main memory
for i in threadList:
    i.join()

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='reductio',db='scraped_data', port=3306)


for key in gmap.keys():
    print gmap

    x = conn.cursor()
    query = 'INSERT INTO scraped_data.stocks (symbol,Price) VALUES("{}",{} )'.format(key, gmap[key])
    x.execute(query)
    row = x.fetchall()
conn.commit()

# Resources
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html

