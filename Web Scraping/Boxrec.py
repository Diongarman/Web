from __future__ import division
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://boxrec.com/boxer/257790'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

table = soup.find(class_='tBoutListTable')

# recordList =[str(row.find(class_='showMob bBottom').find('span').string.strip()) for row in table.find_all(class_='tBoutList')]
record ={int(row.find(class_='showMob').string.strip()): (1 if str(row.find(class_='showMob bBottom').find('span').string.strip()) in ['TKO', 'KO', 'RTD'] else 0) for row in table.find_all(class_='tBoutList')}
print record
ko_ratio_delta = {n:(sum(record.values()[:n])/len(record.values()[:n])*100) for n in record.keys()}
# for row in table.find_all(class_='tBoutList'):
#     result = row.find(class_='showMob bBottom').find('span')
#     bout_num = row.find(class_='showMob')
#     print bout_num.string.strip()

print ko_ratio_delta



# Resources
# http://chrisalbon.com/python/beautiful_soup_scrape_table.html
