import wikipedia
from bs4 import BeautifulSoup
import re
import codecs


def get_geo_articles(location_page_link, limit=100):
    article = wikipedia.page(location_page_link)
    coords = article.coordinates
    lat, lon = coords
    neighbors = wikipedia.geosearch(lat, lon, results=limit, radius=10000)
    return neighbors


def list_places_from_file(filepath):
    with codecs.open(filepath, 'r', encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def save_list_of_places(page, savepath = None, lang="en"):
    if not savepath:
        savepath = './data/' + page.replace(' ', '_') + '.txt'
    outfile = codecs.open(savepath, 'w', encoding="utf-8")
    if lang != "en":
        wikipedia.set_lang(lang)
    wpage = wikipedia.page(page, auto_suggest=False)
    soup = BeautifulSoup(wpage.html(), 'html.parser')
    table = soup.find("table", {"class": "wikitable"})
    rows = table.find_all("tr")
    city_links = []

    for row in rows:
        first_element = row.find("td")
        if first_element != None:
            # anchor = first_element.find("a") # this is for normal
            anchors = first_element.find_all("a") # this is for spain
            if len(anchors) > 1: # this is for spain
                anchor = first_element.find_all("a")[1] # this is for spain
            else: # this is for spain
                anchor = first_element.find_all("a")[0] # this is for spain
            link = anchor["href"].split("/")[-1].replace(',', '')
            city_links.append(link)
            outfile.write(link + '\n')

    return city_links


if __name__ == '__main__':
    save_list_of_places("Provincia (España)", lang="es")
    # save_list_of_places("List of counties of the united kingdom")
    # save_list_of_places("List of states of mexico")
    # save_list_of_places("List of united states counties and county equivalents")
