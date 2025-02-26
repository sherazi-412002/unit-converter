"""Time conversion module"""

# Conversion factors to seconds
TO_SECOND = {
    "Nanosecond": 1e-9,
    "Microsecond": 1e-6,
    "Millisecond": 1e-3,
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400,
    "Week": 604800,
    "Month": 2.628e6,  # Average month (30.44 days)
    "Year": 3.154e7,   # Average year (365.25 days)
    "Decade": 3.154e8,
    "Century": 3.154e9
}

# Conversion from seconds
FROM_SECOND = {unit: 1/factor for unit, factor in TO_SECOND.items()}

def convert(value, from_unit, to_unit):
    """Convert between time units"""
    if value is None:
        return 0
    
    # Convert to seconds first, then to target unit
    seconds = value * TO_SECOND[from_unit]
    result = seconds * FROM_SECOND[to_unit]
    
    return result