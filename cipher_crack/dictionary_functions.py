import string
import logging
from itertools import combinations

logger = logging.getLogger(__name__)

def length_words(length):
    try:
        length = int(length)
    except ValueError as e:
        logger.exception(e)
        return False
    for combination in combinations(string.ascii_lowercase,length):
        #Flatten and yield the tupple
        yield ''.join(combination)

def words_starting_with(starting,length):
    try:
        length = int(length)
    except ValueError as e:
        logger.exception(e)
        return False
    print(starting)
    for combination in combinations(string.ascii_lowercase,
                                    length-len(starting)):
        yield starting + ''.join(combination)
