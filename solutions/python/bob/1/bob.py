def response(hey_bob):

    if hey_bob.strip() == "":
        return "Fine. Be that way!"
        
    question = hey_bob.strip()[-1] == '?'
    yelling = hey_bob.isupper()

    if question and yelling:
        return "Calm down, I know what I'm doing!"
    
    if question:
        return 'Sure.'

    if yelling:
        return 'Whoa, chill out!'

    return 'Whatever.'
