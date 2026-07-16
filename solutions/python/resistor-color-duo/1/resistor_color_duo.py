"""Retrieve Resistor Color Value"""
def value(colors):
    """Return two digit number using first twon color names"""
    code = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }
    
    return int("".join(code[color] for color in colors[:2]))