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
    for x in range(1, int(number ** 0.5)+1):
        if(number%x == 0):
            factors.append(x)
            other = number // x
            if other != number and other != x:
                factors.append(other)

    aliquotSum = sum(factors)
            
    if aliquotSum == number:
        return 'perfect'
    elif aliquotSum > number:
        return 'abundant'
    else:
        return 'deficient'
        