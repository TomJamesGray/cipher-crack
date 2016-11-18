import argparse
from cipher_crack.ciphers import transposition

def main(args):
    parser = argparse.ArgumentParser(description="Crack ciphers\
            based on a dictionary attack")
    parser.add_argument("cipher",action="store",type=str)
    parser.add_argument("--dict",action="store",type=str,
            default="/usr/share/dict/cracklib-small")
    results = parser.parse_args(args)

    words = get_words_from_file(results.dict)
    if results.cipher == "transposition":
        print(words)

def get_words_from_file(location):
    return [(word.rstrip('\n')).replace("'","") for word in open(location,'r')]

def crack(dec_func,dictionary):

