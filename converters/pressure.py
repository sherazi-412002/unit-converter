"""Pressure conversion module"""

# Conversion factors to pascals
TO_PASCAL = {
    "Pascal": 1,
    "Kilopascal": 1e3,
    "Bar": 1e5,
    "PSI": 6894.76,
    "Atmosphere": 101325,
    "Torr": 133.322,
    "Millimeter of Mercury": 133.322
}

# Conversion from pascals
FROM_PASCAL = {unit: 1/factor for unit, factor in TO_PASCAL.items()}

def convert(value, from_unit, to_unit):
    """Convert between pressure units"""
    if value is None:
        return 0
    
    # Convert to pascals first, then to target unit
    pascals = value * TO_PASCAL[from_unit]
    result = pascals * FROM_PASCAL[to_unit]
    
    return result