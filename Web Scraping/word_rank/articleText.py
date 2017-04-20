__author__ = 'diongarman'
from bs4 import BeautifulSoup
import re
import gethtml

def getArticleText(webtext):
    # nytimes specific regex below
    # regex = 'paragraph paragraph-(d*)'
    soup = BeautifulSoup(webtext, 'lxml')
    text = ''
    for tag in soup.findAll('p'):
        try:
            text += str(tag.contents[0]) + "\n"
        except:
            continue
    return text

def getArticle(url):
    html_text = gethtml.getHtmlText(url)
    return getArticleText(html_text)

def getKeywords(articletext):
    common = open('commonWords').read().split('\n')
    word_dict = {}
    word_list = articletext.lower().split()

    for word in word_list:
        if word not in common and word.isalnum():
            if word not in word_dict:
                word_dict[word] = 1
            if word in word_dict:
                word_dict[word] += 1
    return sorted(word_dict.items(), key=lambda(k,v):(v,k), reverse=True)[0:10]


