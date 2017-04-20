__author__ = 'diongarman'
import mechanize


def getHtmlText(url):
    br = mechanize.Browser()
    htmlText = br.open(url).read()
    return htmlText

def getHtmlFile(url):
    br = mechanize.Browser()
    htmlFile = br.open(url)
    return htmlFile
