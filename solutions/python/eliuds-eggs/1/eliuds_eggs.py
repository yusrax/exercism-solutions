def egg_count(display_value):

    binary = []
    while display_value > 0:
        binary.append(display_value % 2)
        display_value //= 2

    count = 0
    for number in binary:
        if number:
            count += 1

    return count
        
