import re
import random
import itertools

def convert_symbols_to_numbers(string):
    symbols_and_numbers = {
        '-': [4,7,8],
        '.': [3,9,0],
        ' ': [1,2,5,6]
    }
    replaced_string = string
    for symbol, numbers_list in symbols_and_numbers.items():
        random.shuffle(numbers_list)
        numbers_cycle = itertools.cycle(numbers_list)
        replaced_string = re.sub(re.escape(symbol), lambda x: str(next(numbers_cycle)), replaced_string)
    return replaced_string

# Test the function
text_with_symbols = ".-- .... . -.  --- -. .  - . .- -.-. .... . ...  - .-- ---  .-.. . .- .-. -."
text_with_symbols = ".-- .... . -.  --- -. .  - . .- -.-. .... . ...  - .-- ---  .-.. . .- .-. -."
result = convert_symbols_to_numbers(text_with_symbols)
print(result)
