import wikipedia
from bs4 import BeautifulSoup


def get_food_synonyms(page_name, savepath):

    f = open(savepath, 'w')

    foods = wikipedia.page(page_name)
    food_synonyms = []  # each row of the form ([list of synonyms], img)

    for link in foods.links[44:]:
        try:
            print('PAGE: ' + link)
            page = wikipedia.page(link, auto_suggest=False)
            food_html = page.html()
            # get_spanish_page(food_html)
            # Add the result to the foods.links
            img_link = get_image(food_html)
            new_synonyms = get_synonyms(food_html)
            entry = (new_synonyms, img_link)
            food_synonyms.append(entry)
            f.write(', '.join(new_synonyms) + '\t' + img_link + '\n')
            print(entry)
        except:
            pass

    return food_synonyms


def get_image(article):
    soup = BeautifulSoup(article, 'html.parser')
    table = soup.find("table", {"class": "infobox"})

    if table == None:
        table = soup.find("table", {"class": "vertical-navbox"})

    try:
        img = table.find('img')
        img_link = "http:" + img["src"]
    except:
        img_link = ""

    return img_link


def get_synonyms(article):

    soup = BeautifulSoup(article, 'html.parser')
    all_p = soup.find_all('p')

    synonyms = []

    for k, p in enumerate(all_p):
        synonyms += [x.get_text() for x in p.find_all('b')]
        if len(synonyms) > 0:
            break

    return synonyms


def get_spanish_page(article):
    print('looking for spanish')
    soup = BeautifulSoup(article, 'html.parser')
    all_a = soup.find_all('a')
    # if "espanol" in all_a.get_text():
        # print('we found it')


food_synonyms_en = get_food_synonyms("List of foods", "./data/synonyms.txt")
# food_synonyms_es = get_food_synonyms("Lista de comidas")
