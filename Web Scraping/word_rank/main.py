__author__ = 'diongarman'
import articleText



url = "http://www.wral.com/bill-would-give-more-power-to-new-nc-superintendent-reduce-role-of-school-board/16341626/"
article = articleText.getArticle(url)
print articleText.getKeywords(article)