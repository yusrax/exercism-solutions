def is_valid(isbn):
    """Return True if the given string is a valid ISBN-10, otherwise False."""
    number = isbn.replace("-", "")
    
    if len(number) != 10:
        return False

    if not number.isdigit():
        if not number.endswith("X"):
            return False

        if not number[:-1].isdigit():
            return False

    total = 0
    multiplier = 10
    for digit in number:
        if digit == "X":
            total += 10 * multiplier
        else:
            total += int(digit) * multiplier
    
        multiplier -= 1

    return total % 11 == 0