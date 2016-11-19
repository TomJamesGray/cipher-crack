import argparse
import logging
from cipher_crack.ciphers import transposition

def main(args):
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description="Crack ciphers\
            based on a dictionary attack")
    parser.add_argument("cipher",action="store",type=str)
    parser.add_argument("cipher_text",action="store",type=str)
    parser.add_argument("--dict",action="store",type=str,
            default="/usr/share/dict/cracklib-small")
    results = parser.parse_args(args)

    words = get_words_from_file(results.dict)
    if results.cipher == "transposition":
        crack(results.cipher_text,transposition.decipher,words)

def get_words_from_file(location):
    return [(word.rstrip('\n')).replace("'","") for word in open(location,'r')]

def crack(cipher_txt,dec_func,dictionary):
    if not callable(dec_func):
        logging.error("Decipher function is not callable")
        raise ValueError("dec_func is not callable")
    for word in dictionary:
        print(dec_func(cipher_txt,word))

