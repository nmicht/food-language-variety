import wikipedia
from bs4 import BeautifulSoup
import re
from food_synonyms import list_from_file
from geo import get_list_cities
from utils import *

synonyms_list = list_from_file('./data/synonyms.txt')

uk_cities_links = get_list_cities("List of cities in the United Kingdom")
# us_cities_links = get_list_cities("List of cities in the United States")

def food_in_cities(synonyms_list, cities_list, savepath):
    outfile = open(savepath, 'w')
    found_words = []
    for city in cities_list[50:]:
        print('---------------->' + city + '<----------------')
        d = find_words_in_article(synonyms_list, city)
        non_empties = [(k, d[k]) for k in d if len(d[k]) > 0]
        found_words.append(non_empties)
        outfile.write('\n\n' + city.upper() + '\n')
        for x in non_empties:
            outfile.write(str(x) + '\n')

    return found_words


food_in_cities(synonyms_list, uk_cities_links, './data/foods_in_uk.txt')
# food_in_cities(synonyms_list, us_cities_links, './data/foods_in_us.txt')


# articles = get_geo_articles(city, 5000)
# print(len(articles))
# filtered = filter_by_title(articles, synonyms_list)
# print(len(filtered))
# print(filtered)
# find_in_articles("beer", articles)
