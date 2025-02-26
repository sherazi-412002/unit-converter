"""Energy conversion module"""

# Conversion factors to joules
TO_JOULE = {
    "Joule": 1,
    "Kilojoule": 1e3,
    "Calorie": 4.184,
    "Kilocalorie": 4184,
    "Watt Hour": 3600,
    "Kilowatt Hour": 3.6e6,
    "Electronvolt": 1.602e-19,
    "British Thermal Unit": 1055.06,
    "US Therm": 1.055e8
}

# Conversion from joules
FROM_JOULE = {unit: 1/factor for unit, factor in TO_JOULE.items()}

def convert(value, from_unit, to_unit):
    """Convert between energy units"""
    if value is None:
        return 0
    
    # Convert to joules first, then to target unit
    joules = value * TO_JOULE[from_unit]
    result = joules * FROM_JOULE[to_unit]
    
    return result