import re
import random
import itertools

def decode_numbers_to_symbols(encoded_string):
    symbols_and_numbers = {
        '-': [4,7,8],
        '.': [3,9,0],
        ' ': [1,2,5,6]
    }
    
    numbers_to_symbols = {}
    for symbol, numbers_list in symbols_and_numbers.items():
        for number in numbers_list:
            numbers_to_symbols[number] = symbol
    
    decoded_string = encoded_string
    decoded_string = re.sub(r'\d', lambda x: numbers_to_symbols[int(x.group(0))], decoded_string)
    
    return decoded_string

# Test the decoding function
encoded_text = "3481093029573614872405961823507649831093029530961723485748610793205946380179"
decoded_result = decode_numbers_to_symbols(encoded_text)
print(decoded_result)
