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


def find_words_in_article(synonyms_list, article_link):
    found_words = {}
    try:
        article = wikipedia.page(article_link, auto_suggest=False)
    except:
        return found_words

    for x in synonyms_list:
        key = x[0][0]  # The first word on the synonyms_list
        found_words[key] = []
        for w in x[0]:
            word = w.strip()
            needle = '\\b' + word + '\\b'
            if re.search(needle, article.content, flags=re.IGNORECASE) and not word == '':
                found_words[key].append(word)

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
