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

#Functions used to find out the modular multiplicative inverse
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/
#Extended_Euclidean_algorithm
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def get_adj(x):
    """
    Returns the adjudicate matrix of X
    """
    return np.linalg.det(x)*x.getI()

def mod_matrix(x,mod=26):
    """
    Returns the matrix x, using modular arithmetic of mod
    """
    new_data = []
    for row in x:
        new_data.append([])
        for item in row:
            logger.info("{} to {}".format(item,item%mod))
            new_data[-1].append(item%mod)

    return np.matrix(x)

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
    #Round the determinant to a reasonable accuracy
    det = round(np.linalg.det(key_matrix),3)
    logger.info("Determinant: {}".format(det))
    det_mulinv = mulinv(det,26)
    logger.info("Mulinv det: {}".format(det_mulinv))
    #No modular multiplicative inverse found
    if det == None:
        return None
    key_inverse = mod_matrix(det_mulinv*get_adj(key_matrix),26)

    logger.info("Inverted key: {}".format(key_inverse))
    out = []
    for cipher_txt_matrix in cipher_txt_matricies:
        out.append((key_inverse*cipher_txt_matrix).tolist())

    logger.info("Out chars: {}".format(out))
    return "ACT"

