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

def count_words_in_cipher(words,cipher):
    cipher = cipher.upper()
    count = 0
    for word in words:
        if word.upper() in cipher:
            count += 1
    return count
