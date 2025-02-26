"""Data storage conversion module"""

# Conversion factors to bits
TO_BIT = {
    "Bit": 1,
    "Byte": 8,
    "Kilobit": 1e3,
    "Kilobyte": 8e3,
    "Megabit": 1e6,
    "Megabyte": 8e6,
    "Gigabit": 1e9,
    "Gigabyte": 8e9,
    "Terabit": 1e12,
    "Terabyte": 8e12,
    "Petabit": 1e15,
    "Petabyte": 8e15
}

# Conversion from bits
FROM_BIT = {unit: 1/factor for unit, factor in TO_BIT.items()}

def convert(value, from_unit, to_unit):
    """Convert between data storage units"""
    if value is None:
        return 0
    
    # Convert to bits first, then to target unit
    bits = value * TO_BIT[from_unit]
    result = bits * FROM_BIT[to_unit]
    
    return result