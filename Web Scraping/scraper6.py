__author__ = 'diongarman'
import urllib
import json
import csv

with open('companylist.csv') as symbolfile:
    readCSV = csv.reader(symbolfile, delimiter=',')
    names = []
    for row in readCSV:
        name = row[0]
        names.append(name)

print(names[1:])

for symbol in names[1:]:
    myWriteFile = open("daily_prices/%s.txt" % symbol, "w+")
    myWriteFile.close()
# had issues finding this link using the network>xhr in chrome devtools
    html = urllib.urlopen('https://www.bloomberg.com/markets/api/bulk-time-series/price/{}%3AUS?timeFrame=1_DAY'.format(symbol), proxies={'http':'Http://ninjacloak.Com'})
    data = json.load(html)

    myWriteFile = open("daily_prices/%s.txt" % symbol, "a")
    if len(data[0]['price']):
        for x in data[0]['price']:
            print symbol, 'value:', x['value'], 'time:', x['dateTime']
            myWriteFile.write(str(symbol)+","+str(x['value'])+","+str(x['dateTime']+"\n"))
    else:
        continue
    myWriteFile.close()


    print len(data[0]['price'])
