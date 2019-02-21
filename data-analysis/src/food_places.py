import wikipedia
import json
from bs4 import BeautifulSoup
from food_synonyms import list_synonyms_from_file
from geo import list_places_from_file
from utils import *


class Place(object):
    def __init__(self, data):
        self.name = None
        self.coords = None
        self.foods = {}

        lines = data.split('\n')
        if len(lines) > 2:
            self.name = lines[0].strip().lower()
            self.coords = lines[1]
            self.foods = {}
            for food in lines[2:]:
                if len(food) > 0:
                    key, synonyms = food.lower().split('\t')
                    synonyms = json.loads(synonyms)
                    if key in self.foods:
                        self.foods[key].extend(synonyms)
                    else:
                        self.foods[key] = synonyms


    def __str__(self):
        return 'name: ' + self.name + '\n' + 'coords: ' + self.coords + '\n' + 'foods: ' + str(len(self.foods)) + '\n' + "\n".join(self.foods.keys())


def food_in_places(food_item_dict, places_list, savepath, lang='en'):
    outfile = open(savepath, 'w')
    found_words = [[], []]

    for place in places_list:
        coords = 'None'
        try:
            wikipedia.set_lang('en')
            article = wikipedia.page(place, auto_suggest=False)
            print('langlinks', article.langlinks[lang])
        except:
            try:
                wikipedia.set_lang('en')
                place_with_comma = "_".join(place.split("_")[:-1]) + ",_" + place.split("_")[-1]
                article = wikipedia.page(place_with_comma, auto_suggest=False)
                print('langlinks', article.langlinks[lang])
            except:
                continue

        try:
            coords = ", ".join([str(x) for x in article.coordinates])
        except:
            pass

        found_item_dict = find_words_in_article(food_item_dict, article)

        non_empties_en = [(k,v[0]) for k, v in found_item_dict.items() if len(v[0]) > 0]
        non_empties_es = [(k,v[1]) for k, v in found_item_dict.items() if len(v[1]) > 0]

        print(non_empties_es, non_empties_en)

        found_words[0].append(non_empties_en)
        found_words[1].append(non_empties_es)

        outfile.write(place.upper() + '\n' + coords + '\n')
        for x in non_empties_en:
            outfile.write(json.dump(x[0]) + '\t' + json.dump(x[1]) + '\n')
        for x in non_empties_es:
            outfile.write(json.dump(x[0]) + '\t' + json.dump(x[1]) + '\n')

        outfile.write('\n\n')

    return found_words


def list_places_with_food_from_files(filepaths):
    places_objs = []

    for filename in filepaths:
        with open(filename, 'r') as f:
            obj_strings = f.read().split('\n\n\n')

            for obj in obj_strings:
                new = Place(obj)
                if new.name:
                    places_objs.append(new)

    return places_objs


if __name__ == '__main__':
    # Get the list of places from a file
    places = list_places_from_file("./data/Provinces_of_Spain.txt")

    # Get a list of synonyms from a file
    food_item_dict = list_synonyms_from_file('./data/all_fruit_synonyms.txt')
    # Get the places
    food_in_places(food_item_dict, places, './data/fruits_in_us_counties.txt')

    veg_item_dict = list_synonyms_from_file('./data/all_vegetables_synonyms.txt')
    food_in_places(veg_item_dict, places, './data/veggies_in_us_counties.txt')
