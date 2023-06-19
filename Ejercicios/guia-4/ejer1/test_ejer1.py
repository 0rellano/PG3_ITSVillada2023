from ejer1 import validate_password

def test_validate_password():
    assert validate_password("Aaaaaaaaaa1") == True
    assert validate_password("Aaaaaaaaaa*1") == False
    assert validate_password("A1") == False
    assert validate_password("aaaaaaaaaa") == False
    


test_validate_password()