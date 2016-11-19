import logging
import string


logger = logging.getLogger(__name__)

def decipher(cipher_txt,key):
    """
    Deciphers a given cipher text with a key
    """
    #Perform basic normalisation of the inputs
    key = key.lower()
    cipher_txt = cipher_txt.upper().replace(" ","").translate(string.punctuation)
    logger.debug("Cipher text: {}".format(cipher_txt))
    #remove duplicate characters
    __key = ""
    for c in key:
        if c not in __key:
            __key += c
    #Find the order of the key, based on the position of the chars
    #in the alphabet
    __key_sorted = sorted(__key)
    key_order = []
    for c in __key:
        key_order.append(__key_sorted.index(c))
    logger.debug("Key order for {}: {}".format(key,key_order))
    
    #split the cipher text based on the length of the key into chunks
    chunks = []
    col_width = int(len(cipher_txt)//len(key_order))
    logger.debug("col width: {}".format(col_width))
    for i in range(len(key_order)):
        chunks.append(cipher_txt[i*col_width:(i*col_width)+col_width])
    logger.debug("Chunks: {}".format(chunks))
    
    #Order the chunks in the order of the key
    ordered_chunks = []
    for pos in key_order:
        ordered_chunks.append(chunks[pos])

    out = ""
    for c in range(col_width):
        for chunk in range(len(ordered_chunks)):
            out += ordered_chunks[chunk][c]
    logger.debug("Output: {}".format(out))

    return out
