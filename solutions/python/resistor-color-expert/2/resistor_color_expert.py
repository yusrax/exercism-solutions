"""Resistor Color Bands"""
def resistor_label(colors):
    """Translate resistor color bands to human-readable labels"""
    color_code = { 
        "black": 0, 
        "brown": 1, 
        "red": 2, 
        "orange": 3, 
        "yellow": 4, 
        "green": 5, 
        "blue": 6, 
        "violet": 7, 
        "grey": 8, 
        "white": 9, 
    }

    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    tolerance_value = 0
    zeros = 0
    value = 0
    
    if len(colors) == 1:
        return f"{color_code[colors[0]]} ohms"
        
    if len(colors) == 4:
        value = color_code[colors[0]] * 10 + color_code[colors[1]]
        zeros = color_code[colors[2]]
        value *= 10 ** zeros
        tolerance_value = tolerance[colors[3]]
    elif len(colors) == 5:
        value = color_code[colors[0]] * 100 + color_code[colors[1]]* 10 + color_code[colors[2]]
        zeros = color_code[colors[3]]
        value *= 10 ** zeros
        tolerance_value = tolerance[colors[4]]


    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]

    unit = 0

    while value >= 1000 and unit < len(units) - 1:
        value /= 1000
        unit += 1

    return f"{value:g} {units[unit]} ±{tolerance_value}"
        
        
    