from cipher_crack.ciphers import vigenere

def test_vigenere_decipher():
    to_decipher = "LXFOPVEFRNHR"
    key = "LEMON"
    expected_output = "attackatdawn"
    assert expected_output == vigenere.decipher(to_decipher,key)
