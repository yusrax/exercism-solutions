"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    """Determine the relationship between two list"""
    
    if list_one == list_two:
        return EQUAL

    if not list_one:
        return SUBLIST

    if not list_two:
        return SUPERLIST
    
    if len(list_one) < len(list_two):
        return SUBLIST if check_list(list_one, list_two) else UNEQUAL
    else:
        return SUPERLIST if check_list(list_two, list_one) else UNEQUAL

    return result
        
def check_list(sublist, superlist):
    """Check whether is a list is a sublus given a superlist"""
    start = 0
    end = len(sublist)

    while end <= len(superlist):
        if sublist == superlist[start:end]:
            return True

        start += 1
        end += 1

    return False
    
