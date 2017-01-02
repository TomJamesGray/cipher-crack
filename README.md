# cipher-crack [![Build Status](https://travis-ci.org/TomJamesGray/cipher-crack.svg?branch=master)](https://travis-ci.org/TomJamesGray/cipher-crack)
Crack traditional ciphers through dictionary attacks

```
usage: cipher-crack [-h] [--dict DICT] [--include-ic]
                    [--min-rating MIN_RATING] [--dict_func DICT_FUNC]
                    [--args ARGS]
                    cipher cipher_text likely_words

Crack ciphers based on a dictionary attack

positional arguments:
  cipher                The type of cipher used e.g transposition
  cipher_text
  likely_words          Space seperated words that are likely to appear to
                        appear in the correct output

optional arguments:
  -h, --help            show this help message and exit
  --dict DICT           A file containing the possible keys
  --include-ic          Include the index of coincidence in the rating of the
                        output, this is reccomended for longer cipher texts
                        however for shorter ciphers the index of coincidence
                        could skew the output too much
  --min-rating MIN_RATING
                        The minimum rating for a given output to be printed
                        out

dict_func:
  --dict_func DICT_FUNC
                        A function that yields words based on a criteria
  --args ARGS           Arguments to be used with a dictionary function
```
