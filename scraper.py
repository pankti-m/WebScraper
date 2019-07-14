#!/usr/env python

from bs4 import BeautifulSoup
import re
import requests

#def scrape_amazon():
url_prefix = "https://amazon.com/"
id_prefix = "/dp/"
items_on_store = {
	"TONSEE Womens Ladies Fashion Rhinestone Wristwatch Quartz Watch" : "B078GMSVJR",
	"Ceramic-Succulent-Elephant-Flowerpot-Elephants" : "B079J87J9S",
	"Compatible-iPhone-Clear-Anti-Scratch-Absorption" : "B07HRJL27Z"
	}

print "================================="
print "Items In Store With Their Ratings"
print "================================="
for k, v in items_on_store.items():
	url = url_prefix + k + id_prefix + v
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	ratings = soup.find_all("span", "a-icon-alt", string=re.compile("stars"))
	# There are multiple ratings for similar items on the webpage.
	# We are only interested in the rating of this item.
	rating = str(ratings[0]).lstrip("<span class=\"a-icon-alt\">").rstrip("</span>")
	print k, rating
