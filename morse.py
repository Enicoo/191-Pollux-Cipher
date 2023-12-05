# Dictionary mapping characters to Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char != ' ':
            if char in morse_code_dict:
                morse_code += morse_code_dict[char] + ' '  # Separate Morse code letters by space
            else:
                morse_code += '/ '  # Use '/' for characters not in the dictionary
        else:
            morse_code += ' '  # Use '/' to represent spaces between words
    return morse_code

# Example usage:
input_text = "Hello World"
result = text_to_morse(input_text)
print(f"The Morse code for '{input_text}' is: {result}")
