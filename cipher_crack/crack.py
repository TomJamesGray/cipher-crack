import logging

logger = logging.getLogger(__name__)

def crack(cipher_txt,dec_func,dictionary,likely_words):
    likely_words = likely_words.split(" ")
    if not callable(dec_func):
        logger.error("Decipher function is not callable")
        raise ValueError("dec_func is not callable")

    for word in dictionary:
        deciphered = dec_func(cipher_txt,word)
        if deciphered != None:
            if are_words_in_cipher(likely_words,deciphered):
                logger.info("Key: {} \n{}".format(word,
                    deciphered))

def are_words_in_cipher(words,cipher):
    for word in words:
        if word in cipher:
            return True
