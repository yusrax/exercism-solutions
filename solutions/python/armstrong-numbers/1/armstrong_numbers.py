def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    sum = 0 

    for digit in digits:
        sum += digit**len(digits)

    return number == sum
