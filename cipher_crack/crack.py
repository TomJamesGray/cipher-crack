import logging
import string
import math

logger = logging.getLogger(__name__)

def crack(cipher_txt,dec_func,dictionary,likely_words,ic=False,min_rating=1):
    """
    Accepts a cipher text and decipher function and deciphers the text
    looking for likely words. The dictionary should be a lazy function
    """
    likely_words = likely_words.split(" ")
    if not callable(dec_func):
        logger.error("Decipher function is not callable")
        raise ValueError("dec_func is not callable")

    results = []
    for word in dictionary():
        deciphered = dec_func(cipher_txt,word)
        if isinstance(deciphered,str):
            score = rate_output(likely_words,deciphered,ic)
            if score >= min_rating:
                results.append((word,deciphered,score))

    #Sort results by the score
    results = sorted(results,key=lambda x:x[2])
    for result in results:
        print("Score: {},Key: {}\n{}".format(result[2],result[0],result[1]))

def rate_output(likely_words,cipher,ic=False):
    """
    Rates a output based on the occurences of the likely words and if
    enabled the index of coincidence
    """
    target_ic = 1.73
    sd = 0.25
    cipher = cipher.upper()
    rating = 0
    for word in likely_words:
        if word.upper() in cipher:
            rating += 1
    if ic:
        rating *= apply_normal_dist(calculate_ic(cipher),target_ic,sd)
    return rating

def calculate_ic(text):
    """
    Calculates the index of coincidence of a given text, english text
    should have a IC of ~1.73
    """
    alphabet = string.ascii_lowercase
    text = text.lower()
    new_text = ""
    occurences = {}
    for c in text:
        if c in alphabet:
            new_text += c
            if c in occurences:
                occurences[c] += 1
            else:
                occurences[c] = 1
    observed = sum(
            [occurences[x]*(occurences[x]-1) for x in occurences])
    random = (1/len(alphabet))*len(new_text)*(len(new_text)-1)
    return observed/random

def apply_normal_dist(x,mean,sd):
    """
    Get the y value for a given x value using the normal distribution
    with a given mean and standard deviation
    """
    return (1/(sd*(2*math.pi)**0.5))*math.e**((-(x-mean)**2)/(2*(sd**2)))
