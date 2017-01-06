import logging
import string

logger = logging.getLogger(__name__)
def decipher(cipher_txt,key):
    """
    Deciphers a given cipher text using a key with the vigenere cipher
    """
    alphabet = string.ascii_lowercase
    cipher_txt,key = text_to_pos(cipher_txt.lower()),text_to_pos(key.lower())
    logger.info("Cipher text: {}".format(cipher_txt))
    logger.info("Key: {}".format(key))
    if cipher_txt == False or key == False:
        return False
    out = ""
    i = 0
    for c in cipher_txt:
        if i >= len(key):
            i = 0
        out += string.ascii_lowercase[(c-key[i])%26]
        i += 1
    return out

def text_to_pos(txt,alphabet=string.ascii_lowercase):
    """
    Converts a string into the positions in a string, by default the
    ascii lowercase alphabet, returning a list
    """
    out = []
    for c in txt:
        try:
            out.append(alphabet.index(c))
        except ValueError:
            logger.error("Character {} not in alphabet {}".format(c,alphabet))
            return False
    return out
