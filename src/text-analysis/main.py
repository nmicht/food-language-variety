import wikipedia
from bs4 import BeautifulSoup
import re
from food_synonyms import list_from_file
from geo import get_list_of_places
from utils import *

food_item_dict = list_from_file('./data/all_vegetables_synonyms.txt')

places = get_list_of_places("List of counties of the united kingdom")

food_in_places(food_item_dict, places, './data/foods_in_uk_counties.txt')
# food_in_cities(synonyms_list, us_cities_links, './data/foods_in_us.txt')


# articles = get_geo_articles(city, 5000)
# print(len(articles))
# filtered = filter_by_title(articles, synonyms_list)
# print(len(filtered))
# print(filtered)
# find_in_articles("beer", articles)
