"""Matching Brackets"""
def is_paired(input_string):
    """Verify that any and all bracket pairs are matched and nested correctly"""
    brackets = "".join(char for char in input_string if char in "()[]{}")
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    opening_brackets = []

    for bracket in brackets:
        if bracket in "([{":
            opening_brackets.append(bracket)
        elif len(opening_brackets) >= 1 and pairs[bracket] == opening_brackets[-1]:
            opening_brackets.pop()
        else:
            return False
        
    return len(opening_brackets) == 0
                  