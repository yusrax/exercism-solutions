"""
Classify numbers as perfect, abundant, or deficient.
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"
        
    factors = []
    for factor in range(1, int(number ** 0.5)+1):
        if number%factor == 0:
            factors.append(factor)
            other = number // factor
            if other not in {number, factor}:
                factors.append(other)

    aliquot_sum = sum(factors)
            
    if aliquot_sum == number:
        return "perfect"
        
    if aliquot_sum > number:
        return "abundant"

    return "deficient"
        