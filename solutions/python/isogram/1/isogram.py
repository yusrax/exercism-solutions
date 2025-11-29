def is_isogram(string):
    letters = ''
    for char in string:
        if char.isalpha():
            letters = letters + char

    return len(set(letters.lower())) == len(letters)