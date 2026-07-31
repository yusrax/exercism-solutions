"""Secret Handshake"""
def commands(binary_str):
    """Convert a number to a sequence of actions"""
    actions = ["wink", "double blink", "close your eyes", "jump"]
    handshake = []

    for index, char in enumerate(reversed(binary_str)):
        if char == "1" and index < 4:
            handshake.append(actions[index])

    if binary_str[0] == "1":
        handshake.reverse()

    return handshake
    
