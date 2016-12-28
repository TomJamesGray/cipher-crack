from cipher_crack.ciphers import hill_cipher

def test_hill_decipher_key_len_4():
    to_decipher = "APADJTFTWLFJ"
    key = "HILL"
    expected_output = "shortexample"
    assert hill_cipher.decipher(to_decipher,key) == expected_output

def test_hill_decipher_key_len_9():
    to_decipher = "DPQRQEVKPQLR"
    key = "BACKUPABC"
    expected_output = "retreatnowxx"
    assert hill_cipher.decipher(to_decipher,key) == expected_output
