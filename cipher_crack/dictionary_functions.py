import string
from itertools import combinations

def length_words(length):
    for combination in combinations(string.ascii_lowercase,length):
        #Flatten and yield the tupple
        yield ''.join(combination)
