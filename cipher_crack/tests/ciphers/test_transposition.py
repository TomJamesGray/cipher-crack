from cipher_crack.ciphers import transposition

def test_transposition_decipher():
    to_decipher = "EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE"
    key = "ZEBRAS"
    expected_output = "WEAREDISCOVEREDFLEEATONCEQKJEU"
    assert transposition.decipher(to_decipher,key) == expected_output
