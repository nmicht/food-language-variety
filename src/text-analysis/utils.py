import wikipedia
from bs4 import BeautifulSoup
import re


def filter_by_title(articles, synonyms_list):
    return [a for a in articles if any_word_in(synonyms_list, a)]


def any_word_in(synonyms_list, article):
    for x in synonyms_list:
        for w in x[0]:
            needle = '\\b' + w.strip() + '\\b'
            if re.search(needle, article, flags=re.IGNORECASE) and not w.strip() == '':
                return True

    return False


def find_words_in_article(food_item_dict, article):
    found_words = {}

    for key in food_item_dict:
        found_words[key] = [[], []]
        wordlist_en = food_item_dict[key][0]
        wordlist_es = food_item_dict[key][1]

        for w in wordlist_en:
            word = w.strip()
            needle = '\\b' + word + '\\b'
            if re.search(needle, article.content, flags=re.IGNORECASE) and not word == '':
                found_words[key][0].append(word)

        for w in wordlist_es:
            word = w.strip()
            needle = '\\b' + word + '\\b'
            if re.search(needle, article.content, flags=re.IGNORECASE) and not word == '':
                found_words[key][1].append(word)

    return found_words


def find_word_in_articles(word, article_links):
    needle = '\\b' + word + '\\b'

    for article_link in article_links:
        page = wikipedia.page(article_link, auto_suggest=False)
        found = re.search(needle, page.content.lower())
        if found:
            print('found in ' + article_link)
        else:
            print('not in ' + article_link)


def food_in_places(food_item_dict, places_list, savepath):
    outfile = open(savepath, 'w')
    found_words = [[], []]

    for place in places_list:
        coords = 'None'
        print('---------------->' + place + '<----------------')
        try:
            article = wikipedia.page(place, auto_suggest=False)
        except:
            continue

        try:
            coords = " ".join([str(x) for x in article.coordinates])
        except:
            pass

        found_item_dict = find_words_in_article(food_item_dict, article)

        # for key in found_item_dict:
        #     found_words_en = found_item_dict[key][0]
        #     found_words_es = found_item_dict[key][1]
        #
        non_empties_en = [v[0] for k, v in found_item_dict.items() if len(v[0]) > 0]
        non_empties_es = [v[1] for k, v in found_item_dict.items() if len(v[1]) > 0]

        #non_empties_es = [x for x in found_words_es if len(x) > 0]

        print(non_empties_es, non_empties_en)

        found_words[0].append(non_empties_en)
        found_words[1].append(non_empties_es)

        outfile.write('\n\n' + place.upper() + '\n' + coords + '\n')
        for x in non_empties_en:
            outfile.write(str(x) + '\n')
        for x in non_empties_es:
            outfile.write(str(x) + '\n')

    return found_words
