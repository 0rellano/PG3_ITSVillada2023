from ejer2 import roman_to_decimal

def test_roman_to_decimal():
    assert roman_to_decimal("IV") == 4
    assert roman_to_decimal("MDCLXIV") == 1664