"""Binary Search"""
def find(search_list, value):
    """find a value in the given list"""
    first = 0
    last = len(search_list)-1

    while first <= last:
        mid = (first + last) // 2
        if search_list[mid] == value:
            return mid
            
        if search_list[mid] > value:
            last = mid - 1
        else:
            first = mid + 1

    raise ValueError("value not in array")