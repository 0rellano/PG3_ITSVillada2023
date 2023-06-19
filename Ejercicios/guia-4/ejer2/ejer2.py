
def roman_to_decimal(roman_number: str) -> int:
    ROMAN_VALUES = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500,
        'M': 1000
    }
    decimal = 0
    last_value = 0

    for digit in reversed(roman_number.upper()):
        value = ROMAN_VALUES[digit]

        if value >= last_value:
            decimal += value
        else:
            decimal -= value
        
        last_value = value
    
    return decimal