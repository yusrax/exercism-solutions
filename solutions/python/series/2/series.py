"""Series"""
def slices(series, length):
    """Given a string of digits, output all the contiguous substrings of a given length"""
    if len(series) == 0:
        raise ValueError("series cannot be empty")
        
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    substrings = [
        series[index:index + length]
        for index in range(len(series))
        if len(series[index:index + length]) == length
    ]

    return substrings
