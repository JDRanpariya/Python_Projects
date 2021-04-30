import requests
from bs4 import BeautifulSoup as bs4
import re
import collections
import nltk
from nltk.corpus import stopwords
# from nltk import stopwords


def scrapeArticle(url):

    raw_res = requests.get(url)
    soup = bs4(raw_res.content, 'html.parser')
    raw_text = soup.text.replace("\n", "").replace("\t", "")
    word_count = int(len(soup.text.replace("\n", "").replace("\t", ""))/5)

    return raw_text


def text_clean_up(raw_text):
    words = [word.lower() for word in raw_text.split(" ") if word.strip()]
    return words


if __name__ == "__main__":
    raw_text = scrapeArticle("https://en.wikipedia.org/wiki/Article_(grammar)")
    words = text_clean_up(raw_text)
    stop_words = list(set(stopwords.words('english')))[:100]
    final_words = []
    for word in words:
        if word not in stop_words:
            final_words.append(word)
    count_words = collections.Counter(words)
    print(count_words.most_common(20))

