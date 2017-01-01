import argparse
import logging
import logging.config
import cipher_crack.dictionary_functions as dict_funcs
from cipher_crack.ciphers import transposition,hill_cipher
from cipher_crack import crack

logging_config = {
    "version":1,
    "formatters":{
        "main":{"format":"%(name)s-%(lineno)d: %(message)s"},
        "simple":{"format":"%(message)s"}
    },
    "handlers":{
        "ciphers":{"class":"logging.StreamHandler",
            "formatter":"main",
            "level":"DEBUG"},
        "user":{"class":"logging.StreamHandler",
            "formatter":"main",
            "level":"INFO"},
        "clean":{"class":"logging.StreamHandler",
            "formatter":"simple",
            "level":"INFO"}
    },
    "loggers":{
        "cipher_crack.ciphers":{
            "handlers":["ciphers"],
            "level":"ERROR"},
        "cipher_crack.crack":{
            "handlers":["clean"],
            "level":"INFO"},
        "cipher_crack.main":{
            "handlers":["user"],
            "level":"INFO"},
        "cipher_crack.dictionary_functions":{
            "handlers":["user"],
            "level":"INFO"}
    }
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main(args):
    dictionary_functions = {
        "word_length": lambda x: dict_funcs.length_words(x),
        "words_starting": lambda start,l:
            dict_funcs.words_starting_with(start,l)
    }

    parser = argparse.ArgumentParser(description="Crack ciphers\
            based on a dictionary attack")
    parser.add_argument("cipher",action="store",type=str)
    parser.add_argument("cipher_text",action="store",type=str)
    parser.add_argument("likely_words",action="store",type=str)
    #Use either a dictionary of a pre-defined functions
    parser.add_argument("--dict",action="store",type=str)
    #Include index of coincidence in the ratings of outputs
    parser.add_argument("--include-ic",action="store_true",default=False)
    #Have dict_func as a group, one arg for the function name, and
    #one for the comma seperated args
    dict_func_group = parser.add_argument_group("dict_func")
    dict_func_group.add_argument("--dict_func",action="store",type=str)
    dict_func_group.add_argument("--args",action="store",type=str)

    results = parser.parse_args(args)

    if results.dict == None and results.dict_func == None:
        logger.error("No dictionary or dictionary function specified")
        return False
    elif results.dict != None:
        words = lambda: get_words_from_file(results.dict)
    else:
        words = lambda: dictionary_functions.get(results.dict_func)(
                *results.args.split(","))

    if results.cipher == "transposition":
        crack.crack(results.cipher_text,transposition.decipher,words,
                results.likely_words,results.include_ic)
    elif results.cipher == "hill_cipher":
        crack.crack(results.cipher_text,hill_cipher.decipher,words,
                results.likely_words,results.include_ic)
    else:
        logger.error("No cipher found matching {}".format(results.cipher))

def get_words_from_file(location):
    for word in open(location,'r'):
        yield (word.rstrip('\n')).replace("'","")
