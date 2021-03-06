import requests
import re
import newspaper
from lxml import html
from bs4 import BeautifulSoup
from scrapyr_app.models import Article
'''import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapyr'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapyr.settings")
from django.conf import settings'''

companies = ["Google, Yahoo, Facebook", "Microsoft"]

companies_to_ticker = { "Google": "GOOG", "Yahoo": "YHOO", "Facebook": "FB", "Microsoft": "MSFT"}

article_websites = ["engadget", "techcrunch"]
#tc_article_url_re = re.compile('.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*')
#eg_article_url_re = re.compile('\.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*')

#article_comment_re = re.compile('http://techcrunch\.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*/#comments')

articles = []

def scraper(article_websites):
	articles = []
	for site in article_websites:
		r = requests.get("http://www." + site + ".com")
		# print site
		data = r.text

		soup = BeautifulSoup(data)
		for link in soup.find_all('a'):
			article_link = link.get('href')
			try:
				if re.match("http://w?w?w?\.?" + site + "\.com/20[0-9][0-9]/[0-1][0-9]/[0-3][0-9]/.*", article_link):
					if article_link not in articles and not article_link.endswith('#comments'):
						articles.append(article_link)
						#print article_link
			except AttributeError as ae:
				print str(ae)
			except TypeError as te:
				print str(te)
	return articles

#articles = scraper(article_websites)
'''
for article in articles:
	a = newspaper.Article(article)
	a.download()
	a.parse()
	# print a.title
	a.nlp()

	article_keywords = []
	for word in a.keywords:
	    if word.capitalize() in companies:
		    article_keywords.append(word.capitalize())

    article_authors = []
    for author in a.authors:
        article_authors.append(author.encode('ascii', 'ignore'))
    author_db = ", ".join(article_authors)
    db_article = Article(title=a.title, author=author_db, pub_date=a.publish_date, content=a.text, url=article)
    db_article.save()
    '''