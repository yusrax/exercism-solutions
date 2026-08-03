"""Line Up"""
def line_up(name, number):
    """Given a name and a number, produce a sentence"""
    last_digit = number % 10
    last_two_digits = number % 100

    if 11 <= last_two_digits <= 13:
        position = f"{number}th"
    elif last_digit == 1:
        position = f"{number}st"
    elif last_digit == 2:
        position = f"{number}nd"
    elif last_digit == 3:
        position = f"{number}rd"
    else:
        position = f"{number}th"
    
    return f"{name}, you are the {position} customer we serve today. Thank you!"