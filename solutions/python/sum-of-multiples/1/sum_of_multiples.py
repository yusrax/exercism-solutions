def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    
    for value in multiples:
        k = 1;
        n = value
        
        while n != 0 and k*n < limit:
            unique_multiples.add(k*n)
            k += 1

    return sum(unique_multiples)
            