def equilateral(sides):
    a, b, c = sides
    return isTriangle(sides) and (a == b == c)
    
def isosceles(sides):
    a, b, c = sides
    return isTriangle(sides) and ( a == b or b == c or c == a)

def scalene(sides):
    return isTriangle(sides) and not equilateral(sides) and not isosceles(sides)

def isTriangle(sides):
    a, b, c = sides
    if a == 0 and b == 0 and c == 0:
        return False
    return a + b >= c and b + c >= a and a + c >= b