def decode(string):
    count = ""
    decoded = ""

    for char in string:
        if char.isdigit():
            count += char
        else:
            if count and int(count) > 0:
                decoded += char * int(count)
            else:
                decoded += char
            count = ""
    return decoded

def encode(string):
    if not string:
        return ""
    
    groups = []
    current = ""

    for char in string:
        if not current or char == current[-1]:
            current += char
        else:
            groups.append(current)
            current = char
    
    groups.append(current)

    encoded = [
        f"{len(group)}{group[0]}" if len(group) > 1 else group[0]
        for group in groups
    ]

    return "".join(encoded)
