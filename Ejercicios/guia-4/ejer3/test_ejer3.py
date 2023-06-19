from ejer3 import is_anagram

def test_is_anagram():
    assert is_anagram("ana", "aan") == True
    assert is_anagram("ana", "ann") == False