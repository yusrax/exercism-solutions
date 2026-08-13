"""Sum of Multiples"""
def sum_of_multiples(limit, multiples):
    """Calculate sum of multiples under a given limit"""
    unique_multiples = set()
    
    for value in multiples:
        multiplier = 1
        number = value
        
        while value != 0 and multiplier * value < limit:
            unique_multiples.add(multiplier*number)
            multiplier += 1

    return sum(unique_multiples)
            