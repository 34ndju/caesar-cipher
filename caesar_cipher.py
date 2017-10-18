import urllib2
from bs4 import BeautifulSoup
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

str = "The specific contributions of this paper are as follows: we trained one of the largest convolutional neural networks to date on the subsets of ImageNet used in the ILSVRC-2010 and ILSVRC-2012 competitions [2] and achieved by far the best results ever reported on these datasets. We wrote a highly-optimized GPU implementation of 2D convolution and all the other operations inherent in training convolutional neural networks, which we make available publicly1 . Our network contains a number of new and unusual features which improve its performance and reduce its training time, which are detailed in Section 3. The size of our network made overfitting a significant problem, even with 1.2 million labeled training examples, so we used several effective techniques for preventing overfitting, which are described in Section 4. Our final network contains five convolutional and three fully-connected layers, and this depth seems to be important: we found that removing any convolutional layer"

letter_distribution = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
wiki_link = "https://en.wikipedia.org/wiki/LeBron_James"
connection = urllib2.urlopen(wiki_link)
html = connection.read()
connection.close()
soup = BeautifulSoup(html, 'html5lib')
corpus = soup.text
corpus = shift_string(corpus,3)

for symbol in corpus:
    if symbol.lower() in letter_distribution:
        letter_distribution[symbol.lower()]+=1

print ed.normalize_letter_distribution(letter_distribution)

print corpus
