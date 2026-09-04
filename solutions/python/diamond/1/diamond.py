import string

"""Diamond"""
def rows(letter):
    """Given a letter, print a diamond"""

    letters = string.ascii_uppercase
    diamond_letters = letters[:letters.index(letter)+1]
    inner_space = 0
    outer_space = len(diamond_letters) - 1
    diamond = []

    for char in diamond_letters:
        if char == "A":
            diamond.append(f'{" " * outer_space}{char}{" " * outer_space}')
            inner_space += 1

        else:
            diamond.append(f'{" " * outer_space}{char}{" " * inner_space}{char}{" " * outer_space}')
            inner_space +=  2

        outer_space -= 1

    diamond += diamond[:-1][::-1]
            
    return diamond
        