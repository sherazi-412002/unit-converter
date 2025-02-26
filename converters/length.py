"""Length conversion module"""

# Conversion factors to meters
TO_METER = {
    "Nanometer": 1e-9,
    "Micrometer": 1e-6,
    "Millimeter": 1e-3,
    "Centimeter": 1e-2,
    "Decimeter": 1e-1,
    "Meter": 1,
    "Kilometer": 1e3,
    "Inch": 0.0254,
    "Foot": 0.3048,
    "Yard": 0.9144,
    "Mile": 1609.344,
    "Nautical Mile": 1852,
    "Light Year": 9.461e15
}

# Conversion from meters
FROM_METER = {unit: 1/factor for unit, factor in TO_METER.items()}

def convert(value, from_unit, to_unit):
    """Convert between length units"""
    if value is None:
        return 0
    
    # Convert to meters first, then to target unit
    meters = value * TO_METER[from_unit]
    result = meters * FROM_METER[to_unit]
    
    return result