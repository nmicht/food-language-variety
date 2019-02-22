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
