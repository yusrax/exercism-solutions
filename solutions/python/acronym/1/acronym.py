def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")
    text = words.split()
    abbreviation = ""

    for word in text:
        abbreviation += word[0]

    return abbreviation.upper()
