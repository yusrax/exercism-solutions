"""Say"""
def say(number):
    """Express a given number in english words"""
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    def say_under_1000(num):
        words = []

        if num >= 100:
            hundreds = num // 100
            words.append(f"{ones[hundreds]} hundred")
            num %= 100

        if num >= 20:
            tens_digit = num // 10
            ones_digit = num % 10

            if ones_digit > 0:
                words.append(f"{tens[tens_digit]}-{ones[ones_digit]}")
            else:
                words.append(tens[tens_digit])

        elif num >= 10:
            words.append(teens[num])

        elif num > 0:
            words.append(ones[num])

        return " ".join(words)

    if number == 0:
        return "zero"

    scales = ["", "thousand", "million", "billion"]
    parts = []
    scale_index = 0

    while number > 0:
        group = number % 1000

        if group > 0:
            words = say_under_1000(group)

            if scales[scale_index]:
                words += f" {scales[scale_index]}"

            parts.append(words)

        number //= 1000
        scale_index += 1

    return " ".join(parts[::-1])

        

        

        
        
            
        
        
        

    