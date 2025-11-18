def square_root(number):
    n = number 
    while n*n > number:
        n -= 1
    return n
    