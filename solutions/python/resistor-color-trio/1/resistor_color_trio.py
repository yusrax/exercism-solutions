"""Resistor Color Trio"""
def label(colors):
    """Decode first three resistor colors"""
    code = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    numbers = [ code[color] for color in colors[:3]]
    zeros = numbers.pop()

    for zero in range(zeros):
        numbers.append(0)

    value = int("".join(str(number) for number in numbers))

    count = 0
    while (value != 0 and value % 1000 == 0):
        count += 1
        value = value // 1000

    suffix = ""
    if count >= 3:
        suffix = " gigaohms"
    elif count >= 2:
        suffix = " megaohms"
    elif count >= 1:
        suffix = " kiloohms"
    else:
        suffix = " ohms"

    return str(value) + suffix
        