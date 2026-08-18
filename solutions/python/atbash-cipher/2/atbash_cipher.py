encoding = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a",
}

decoding = { value:key for key, value in encoding.items() }


def encode(plain_text):
    """Encode plaintext to ciphertext"""
    cipher = ''
    count = 0
    
    for char in plain_text:
        if char.isalpha():
            encoded = encoding[char.lower()]
        elif char.isnumeric():
            encoded = char
        else:
            continue

        if count != 0 and count % 5 == 0:
            cipher += ' '
    
        cipher += encoded
        count += 1

    return cipher

def decode(ciphered_text):
    """Decode ciphertext to plaintext"""
    plain_text = ''

    for char in ciphered_text:
        if char.isalpha():
            plain_text += decoding[char.lower()]

        if char.isnumeric():
            plain_text += char

    return plain_text