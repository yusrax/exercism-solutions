def append(list1, list2):
    list1.extend(list2)
    return list1

def concat(lists):
    concatenated = []

    for item in lists:
        concatenated.extend(item)

    return concatenated

def filter(function, list):
    return [ item for item in list if function(item)]

def length(list):
    return len(list)

def map(function, list):
    return [ function(item) for item in list ]

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial

def reverse(list):
    return list[::-1]
