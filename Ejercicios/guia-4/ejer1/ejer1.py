
def validate_password(password: str):

    # check lenght password
    if len(password) < 8:
        return False
    
    # check special chars
    SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|\\;:'\",.<>/?`~"
    
    for char in SPECIAL_CHARS:
        if char in password:
            return False

    # check uppercase, lowercase and number   
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    
    if not (has_uppercase and has_lowercase and has_number):
        return False

    return True