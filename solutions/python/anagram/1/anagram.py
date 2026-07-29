"""Anagram"""
def find_anagrams(word, candidates):
    """Find candidates that are anagrams of the word"""
    anagrams = []
    target = word.lower()
    
    for candidate in candidates:
        if sorted(target) == sorted(candidate.lower()) and target != candidate.lower():
            anagrams.append(candidate)

    return anagrams