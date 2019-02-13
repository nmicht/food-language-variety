import wikipedia
from bs4 import BeautifulSoup
import re
from food_synonyms import list_from_file
from geo import *
from utils import *


places = get_places_from_file("./data/List_of_United_States_counties_and_county_equivalents.txt")

food_item_dict = list_from_file('./data/all_fruit_synonyms.txt')
food_in_places(food_item_dict, places, './data/fruits_in_us_counties.txt')

veg_item_dict = list_from_file('./data/all_vegetables_synonyms.txt')
food_in_places(veg_item_dict, places, './data/veggies_in_us_counties.txt')
