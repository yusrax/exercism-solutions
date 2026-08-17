"""Translate words into Pig Latin."""
def translate(text):

    vowels = ['a', 'e', 'i', 'o', 'u']

    words = text.split()
    pig_latin = []

    for word in words:
        
        sw_vowels = word[0] in vowels or word[:2] in ['xr', 'yt']
        sw_consonants = not sw_vowels
    
        consonants = ''
        start = 0
        
        if sw_consonants:
    
            for index, char in enumerate(word):
                if char in vowels:
                    break 
    
                if index != 0 and char == 'y':
                    break
                    
                consonants = consonants + char
                start = index + 1
                
    
            if consonants.endswith('q') and word[word.index('q') + 1] == 'u':
                consonants = consonants + 'u'
                start += 1

        pig_latin.append(word[start:] + consonants + 'ay')

    return " ".join(pig_latin)