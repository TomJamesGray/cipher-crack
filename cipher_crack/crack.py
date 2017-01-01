import logging

logger = logging.getLogger(__name__)

def crack(cipher_txt,dec_func,dictionary,likely_words):
    """
    Accepts a cpiher text and decipher function and deciphers the text
    looking for likely words. The dictionary could either be a function
    that yields words or a list
    """
    likely_words = likely_words.split(" ")
    if not callable(dec_func):
        logger.error("Decipher function is not callable")
        raise ValueError("dec_func is not callable")

    results = []
    for word in dictionary():
        deciphered = dec_func(cipher_txt,word)
        if deciphered != None:
            score = count_words_in_cipher(likely_words,deciphered)
            if score != 0:
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
    cipher = cipher.upper()
    count = 0
    for word in likely_words:
        if word.upper() in cipher:
            count += 1
    return count

def calculate_ic(text):
    """
    Calculates the index of coincidence of a given text, english text
    should have a IC of ~1.73
    """
    occurences = {}
    for c in text:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    print(occurences)
    observed = sum(
            [occurences[x]*(occurences[x]-1) for x in occurences])
    random = (1/26)*len(text)*(len(text)-1)
    return observed/random

