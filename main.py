import wikipedia
from bs4 import BeautifulSoup

def get_food_synonyms(page_name):
    foods = wikipedia.page(page_name)
    food_synonyms = []

    for link in foods.links:
        try:
            food = wikipedia.page(link)
            food_html = food.html()
            get_spanish_page(food_html)
            # Add the result to the foods.links
            new_synonyms = get_synonyms(food_html)
            food_synonyms.append(new_synonyms)
            print(new_synonyms)
        except:
            pass

    return food_synonyms



def get_synonyms(article):
    soup = BeautifulSoup(article, 'html.parser')
    all_p = soup.find_all('p')

    synonyms = []

    for k,p in enumerate(all_p):
        synonyms += [x.get_text() for x in p.find_all('b')]
        if len(synonyms) > 0:
            break

    return synonyms


def get_spanish_page(article):
    print('looking for spanish')
    soup = BeautifulSoup(article, 'html.parser')
    all_a = soup.find_all('a')
    if "español" in all_a.get_text():
        print('we found it')


food_synonyms_en = get_food_synonyms("List of foods")
food_synonyms_es = get_food_synonyms("Lista de comidas")
