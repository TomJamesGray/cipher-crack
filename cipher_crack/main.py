import argparse
import logging
import logging.config
from cipher_crack.ciphers import transposition

logging_config = {
    "version":1,
    "formatters":{
        "main":{"format":"%(name)s-%(lineno)d: %(message)s"}
    },
    "handlers":{
        "ciphers":{"class":"logging.StreamHandler",
            "formatter":"main",
            "level":"DEBUG"},
        "user":{"class":"logging.StreamHandler",
            "formatter":"main",
            "level":"INFO"}
    },
    "loggers":{
        "cipher_crack.ciphers":{
            "handlers":["ciphers"],
            "level":"ERROR"},
        "cipher_crack.main":{
            "handlers":["user"],
            "level":"INFO"}
    }
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main(args):
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
        logger.error("Decipher function is not callable")
        raise ValueError("dec_func is not callable")
    for word in dictionary:
        print(dec_func(cipher_txt,word))

