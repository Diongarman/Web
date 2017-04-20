__author__ = 'diongarman'
import readability
import urllib
from bs4 import BeautifulSoup
# readability library better than just getting the ptags like before
from readability.readability import Document
import mechanize


# we can be blocked from certain urls, e.g. https://www.google.co.uk/search?q=news&oq=news&aqs=chrome..69i57j69i60j69i61j69i60j69i59j69i61.599j0j7&sourceid=chrome&ie=UTF-8
# Can we hide from boxrec?
#  but we can modify the headers!
url = "https://www.google.co.uk/search?q=news&oq=news&aqs=chrome..69i57j69i60j69i61j69i60j69i59j69i61.599j0j7&sourceid=chrome&ie=UTF-8"


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent', 'Firfox')]

html = br.open(url).read()
# html = urllib.urlopen(url).read()
readable_article = Document(html).summary()
readable_title = Document(html).title()

soup = BeautifulSoup(readable_article, 'lxml')
final_article = soup.text

links = soup.findAll('img', src=True)

print html
# print links