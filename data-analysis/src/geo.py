import wikipedia
from bs4 import BeautifulSoup
import re


def get_geo_articles(location_page_link, limit=100):
    article = wikipedia.page(location_page_link)
    coords = article.coordinates
    lat, lon = coords
    neighbors = wikipedia.geosearch(lat, lon, results=limit, radius=10000)
    return neighbors


def get_places_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def get_list_of_places(page, savepath = None):
    if not savepath:
        savepath = './data/' + page.replace(' ', '_') + '.txt'
    outfile = open(savepath, 'w')
    wpage = wikipedia.page(page)
    soup = BeautifulSoup(wpage.html(), 'html.parser')
    table = soup.find("table", {"class": "wikitable"})
    rows = table.find_all("tr")
    city_links = []

    for row in rows:
        first_element = row.find("td")
        if first_element != None:
            # anchor = first_element.find("a") # this is for normal
            anchor = first_element.find_all("a")[1] # this is for spain
            link = anchor["href"].split("/")[-1].replace(',', '')
            city_links.append(link)
            outfile.write(link + '\n')

    return city_links


if __name__ == '__main__':
    print(get_list_of_places("Provinces of Spain"))
