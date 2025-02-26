"""Temperature conversion module"""

def convert(value, from_unit, to_unit):
    """Convert between temperature units"""
    if value is None:
        return 0
    
    # First convert to Kelvin
    if from_unit == "Celsius":
        kelvin = value + 273.15
    elif from_unit == "Fahrenheit":
        kelvin = (value - 32) * 5/9 + 273.15
    else:  # Kelvin
        kelvin = value
    
    # Then convert from Kelvin to target unit
    if to_unit == "Celsius":
        return kelvin - 273.15
    elif to_unit == "Fahrenheit":
        return (kelvin - 273.15) * 9/5 + 32
    else:  # Kelvin
        return kelvin