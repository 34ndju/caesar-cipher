import urllib2
from bs4 import BeautifulSoup

class English_distribution:

    def __init__(self):
        self.letter_distribution = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }

    def get_distribution_from_wikipedia(self, wiki_link):
        connection = urllib2.urlopen(wiki_link)
        html = connection.read()
        connection.close()
        soup = BeautifulSoup(html, 'html5lib')

        corpus = soup.text

        for i in range(0, len(corpus)):
            if corpus[i].lower() in self.letter_distribution:
                self.letter_distribution[corpus[i].lower()]+=1


        return self.letter_distribution


    def dist_sample(self):
        max = 0
        full_distribution = self.get_distribution_from_wikipedia('https://en.wikipedia.org/wiki/Donald_Glover')

        for key, value in full_distribution.iteritems():
            if value > max:
                max = value

        for key, value in full_distribution.iteritems():
            full_distribution[key] = float(full_distribution[key]) / max

        return full_distribution
