"""Speed conversion module"""

# Conversion factors to meters per second
TO_MPS = {
    "Meter per Second": 1,
    "Kilometer per Hour": 0.277778,
    "Mile per Hour": 0.44704,
    "Knot": 0.514444,
    "Foot per Second": 0.3048
}

# Conversion from meters per second
FROM_MPS = {unit: 1/factor for unit, factor in TO_MPS.items()}

def convert(value, from_unit, to_unit):
    """Convert between speed units"""
    if value is None:
        return 0
    
    # Convert to meters per second first, then to target unit
    mps = value * TO_MPS[from_unit]
    result = mps * FROM_MPS[to_unit]
    
    return result