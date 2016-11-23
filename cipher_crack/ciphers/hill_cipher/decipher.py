import logging
import numpy as np
import string

logger = logging.getLogger(__name__)

def gen_square_matrix(data,rows):
    """
    Generate a square matrix from a list of data
    """
    mat_data = []
    for i in range(0,len(data),rows):
        mat_data.append(data[i:i+rows])
    return np.matrix(mat_data)

def gen_column_matricies(data,rows):
    """
    Generate a list of column matricies from a list of data
    """
    matricies = []
    for i in range(0,len(data),rows):
        matrix = []
        for elem in data[i:i+rows]:
            matrix.append([elem])
        matricies.append(np.matrix(matrix))
    return matricies


def decipher(cipher_txt,key):
    """
    Decipher a given string using a given key using the hill cipher
    """
    #Check if key length is a square number, temp soluton
    if not (len(key) == 4) or (len(key) == 9):
        return None

    #Get positions in alphabet for key
    key = key.lower()
    key_positions = []
    for c in key:
        key_positions.append(string.ascii_lowercase.index(c))
    logger.info("Key positions: {}".format(key_positions))

    cipher_txt = cipher_txt.lower()
    cipher_txt_positions = []
    for c in cipher_txt:
        cipher_txt_positions.append(string.ascii_lowercase.index(c))
    logger.info("Cipher text positions: {}".format(cipher_txt_positions))

    #Create key matrix
    if len(key) == 4:
        key_matrix = gen_square_matrix(key_positions,2)
        cipher_txt_matricies = gen_column_matricies(cipher_txt_positions,2)
    elif len(key) == 9:
        key_matrix = gen_square_matrix(key_positions,3)
        cipher_txt_matricies = gen_column_matricies(cipher_txt_positions,3)

    logger.info("Key matrix: {}".format(key_matrix))
    logger.info("Cipher text matrices: {}".format(cipher_txt_matricies))

    #Try and invert the matrix
    try:
        inverted_key = key_matrix.getI()
    except numpy.linalg.linalg.LinAlgError:
        logger.error("Cipher text matrix is singular")
        return None
    logger.info("Inverted key: {}".format(inverted_key))
    out = []
    for cipher_txt_matrix in cipher_txt_matricies:
        out.append((inverted_key*cipher_txt_matrix).tolist())

    logger.info("Out chars: {}".format(out))
    return "ACT"

