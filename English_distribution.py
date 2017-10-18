import urllib2
from bs4 import BeautifulSoup

class English_distribution:

    def __init__(self):
        self.letter_distribution = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.wiki_link = "https://en.wikipedia.org/wiki/Donald_Glover"


    def normalize_letter_distribution(self, full_distribution):
        max = 0

        for key, value in full_distribution.iteritems():
            if value > max:
                max = value

        for key, value in full_distribution.iteritems():
            full_distribution[key] = float(full_distribution[key]) / max

        return full_distribution

    def get_full_english_distribution_from_corpus(self, corpus):
        for symbol in corpus:
            if symbol.lower() in self.letter_distribution:
                self.letter_distribution[symbol.lower()]+=1


        return self.normalize_letter_distribution(self.letter_distribution)

    def get_full_english_distribution_from_wikipedia(self):
        connection = urllib2.urlopen(self.wiki_link)
        html = connection.read()
        connection.close()
        soup = BeautifulSoup(html, 'html5lib')

        corpus = soup.text
        return self.get_full_english_distribution_from_corpus(corpus = soup.text)
