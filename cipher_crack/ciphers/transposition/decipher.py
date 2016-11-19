import logging
import string

def decipher(cipher_txt,key):
    """
    Deciphers a given cipher text with a key
    """
    #Perform basic normalisation of the inputs
    key = key.lower()
    cipher_txt = cipher_txt.lower().replace(" ","").translate(string.punctuation)
    logging.info(cipher_txt)
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
    logging.info("Key order for {}: {}".format(key,key_order))
    
    #split the cipher text based on the length of the key into chunks
    chunks = []
    col_width = int(len(cipher_txt)//len(key_order))
    logging.info("col width: {}".format(col_width))

    for i in range(len(cipher_txt)//col_width):
        chunks.append(cipher_txt[i*col_width:(i*col_width)+col_width])

    logging.info("Chunks: {}".format(chunks))
