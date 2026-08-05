"""Difference of Squares"""
def sum_up_to(number):
    if number == 1:
        return 1

    return number + sum_up_to(number - 1)
    
def square_of_sum(number):
    return sum_up_to(number) ** 2

def sum_of_squares(number):
    if number == 1:
        return 1

    return number**2 + sum_of_squares(number-1)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
