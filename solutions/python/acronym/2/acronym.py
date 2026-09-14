"""Acronym"""
def abbreviate(words):
    """Convert a phrase to its acronym"""
    words = words.replace("-", " ").replace("_", " ")
    text = words.split()
    abbreviation = ""

    for word in text:
        abbreviation += word[0]

    return abbreviation.upper()
