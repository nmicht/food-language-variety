import wikipedia
from bs4 import BeautifulSoup


def get_food_synonyms(page_name, savepath):

    f = open(savepath, 'w')

    foods = wikipedia.page(page_name)
    foods_links = foods.links
    food_synonyms = {}  # each item of the form key: ([list of synonyms en], [list of synonyms es], img)

    for link in foods_links:
        try:
            print('PAGE: ' + link)
            en_synonyms = []
            es_synonyms = []

            wikipedia.set_lang("en")
            page_en = wikipedia.page(link, auto_suggest=False)
            food_html_en = page_en.html()
            img_link = get_image(food_html_en)
            en_synonyms = get_synonyms(food_html_en)

            wikipedia.set_lang("es")
            try:
                page_es = wikipedia.page(link, auto_suggest=False)
                food_html_es = page_es.html()
                es_synonyms = get_synonyms(food_html_es)
            except:
                pass

            food_synonyms[link] = (en_synonyms, es_synonyms, img_link)
            print(food_synonyms[link])

            f.write(link + '\n' + ', '.join(en_synonyms) + '\n' + ', '.join(es_synonyms) + '\n' + img_link + '\n\n')
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


def list_from_file_old(filepath):
    to_return = []

    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        elems = line.split('\t')
        foods = elems[0].strip()
        img = 'None'

        if len(elems) == 2:
            img = elems[1]

        synonyms = foods.split(', ')
        to_return.append((synonyms, img))

    return to_return


def list_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    entries = {}
    i = 0
    while i < len(lines):
        key = lines[i].strip()
        synonyms_en = lines[i+1].strip().split(', ')
        synonyms_es = lines[i+2].strip().split(', ')
        img_link = lines[i+3]
        i += 5
        entries[key] = (synonyms_en, synonyms_es, img_link)

    return entries


if __name__ == '__main__':
    food_synonyms_en = get_food_synonyms("List of vegetables", "./data/all_vegetables_synonyms.txt")
    # food_synonyms_es = get_food_synonyms("Lista de comidas")
