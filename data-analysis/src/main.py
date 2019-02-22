import wikipedia
from bs4 import BeautifulSoup
import re
from food_synonyms import get_synonyms_keys
from food_places import list_places_with_food_from_files
from food_distribution import build_distribution_dict, write_distribution_to_json_file

print('Getting the synonyms...')
synonyms = get_synonyms_keys(['./data/all_fruit_synonyms.txt','./data/all_vegetables_synonyms.txt'])
print('---> ' + str(len(synonyms)) + ' total synonyms to process')

print('Getting the places with food...')
places_objs = list_places_with_food_from_files([
	'./data/fruits_in_us_counties.txt',
	'./data/fruits_in_es_counties.txt',
	'./data/fruits_in_mx_counties.txt',
	'./data/fruits_in_uk_counties.txt',
	'./data/veggies_in_us_counties.txt',
	'./data/veggies_in_es_counties.txt',
	'./data/veggies_in_uk_counties.txt',
	'./data/veggies_in_mx_counties.txt'
])
print('---> ' + str(len(places_objs)) + ' total of places to process')

print('Building the object distribution...')
pobjs = build_distribution_dict(synonyms, places_objs)
print('---> ' + str(len(pobjs)) + ' total of keys in the distribution')

print('Writing to json file...')
write_distribution_to_json_file(pobjs, './data/distribution.json')
