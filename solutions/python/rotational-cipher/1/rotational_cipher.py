"""Implement Caeser Cipher"""
def rotate(text, key):
    """Rotate English letters in text by the given key."""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    cipher = []
    for char in text:
        if char.isalpha():
            uppercase = char.isupper()
            index = alphabet.index(char.lower()) + key
            
            if uppercase:
                cipher.append(alphabet[index % 26].upper())
            else:
                cipher.append(alphabet[index % 26])
        else:
            cipher.append(char)

    return "".join(cipher)