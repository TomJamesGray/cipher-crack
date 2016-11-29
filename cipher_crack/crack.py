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

    for word in dictionary():
        deciphered = dec_func(cipher_txt,word)
        if deciphered != None:
            if are_words_in_cipher(likely_words,deciphered):
                logger.info("Key: {} \n{}".format(word,
                    deciphered))

def are_words_in_cipher(words,cipher):
    cipher = cipher.upper()
    for word in words:
        if word.upper() in cipher:
            return True
