import urllib2
from bs4 import BeautifulSoup
import math
from English_distribution import English_distribution

ed = English_distribution()
dist = ed.get_full_english_distribution_from_wikipedia()

print dist

def shift_char(unshifted_char, shift_amt):
    return chr(((ord(unshifted_char) + shift_amt - 97) % 26) + 97)

def shift_string(str, shift_amt):

    translated = ""
    for symbol in str:
        if symbol.isalpha():
            translated += shift_char(symbol.lower(), shift_amt)
        else:
            translated += symbol

    return translated

def get_vector_distance_of_letters(eng_dist, sample_dist, shift_guess):
    sum_of_squares = 0
    for key, value in eng_dist.iteritems():
        sum_of_squares += (sample_dist[shift_char(key, shift_guess)] - value)**2
    return math.sqrt(sum_of_squares)


letter_distribution = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
wiki_link = "https://en.wikipedia.org/wiki/Derrick_Rose"
connection = urllib2.urlopen(wiki_link)
html = connection.read()
connection.close()
soup = BeautifulSoup(html, 'html5lib')
corpus = soup.text
corpus = shift_string(corpus,9)

print corpus

for symbol in corpus:
    if symbol.lower() in letter_distribution:
        letter_distribution[symbol.lower()]+=1

print ed.normalize_letter_distribution(letter_distribution)

shift_vector_distances = []
for i in range(26):
    shift_vector_distances.append(get_vector_distance_of_letters(dist, ed.normalize_letter_distribution(letter_distribution), i))

print shift_vector_distances
print shift_vector_distances.index(min(shift_vector_distances))

#print corpus
