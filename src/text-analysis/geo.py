import wikipedia
from bs4 import BeautifulSoup
import re

def get_geo_articles(city, limit=100):
    city = wikipedia.page(city)
    coords = city.coordinates
    lat, lon = coords
    neighbors = wikipedia.geosearch(lat, lon, results=limit, radius=10000)
    return neighbors

def find_in_articles(word, articles):
    needle = '\\b' + word + '\\b'

    for article_link in articles:
        page = wikipedia.page(article_link, auto_suggest=False)
        found = re.search(needle, page.content.lower())
        if found:
            print('found in ' + article_link)
        else:
            print('not in ' + article_link)

articles = get_geo_articles("London")
find_in_articles("beer", articles)
