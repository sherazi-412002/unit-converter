"""Volume conversion module"""

# Conversion factors to liters
TO_LITER = {
    "Milliliter": 1e-3,
    "Cubic Centimeter": 1e-3,
    "Liter": 1,
    "Cubic Meter": 1e3,
    "Teaspoon": 0.00492892,
    "Tablespoon": 0.0147868,
    "Fluid Ounce": 0.0295735,
    "Cup": 0.24,
    "Pint": 0.473176,
    "Quart": 0.946353,
    "Gallon": 3.78541,
    "Cubic Inch": 0.0163871,
    "Cubic Foot": 28.3168,
    "Cubic Yard": 764.555
}

# Conversion from liters
FROM_LITER = {unit: 1/factor for unit, factor in TO_LITER.items()}

def convert(value, from_unit, to_unit):
    """Convert between volume units"""
    if value is None:
        return 0
    
    # Convert to liters first, then to target unit
    liters = value * TO_LITER[from_unit]
    result = liters * FROM_LITER[to_unit]
    
    return result