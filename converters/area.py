"""Area conversion module"""

# Conversion factors to square meters
TO_SQ_METER = {
    "Square Millimeter": 1e-6,
    "Square Centimeter": 1e-4,
    "Square Meter": 1,
    "Hectare": 1e4,
    "Square Kilometer": 1e6,
    "Square Inch": 0.00064516,
    "Square Foot": 0.092903,
    "Square Yard": 0.836127,
    "Acre": 4046.86,
    "Square Mile": 2.59e6
}

# Conversion from square meters
FROM_SQ_METER = {unit: 1/factor for unit, factor in TO_SQ_METER.items()}

def convert(value, from_unit, to_unit):
    """Convert between area units"""
    if value is None:
        return 0
    
    # Convert to square meters first, then to target unit
    sq_meters = value * TO_SQ_METER[from_unit]
    result = sq_meters * FROM_SQ_METER[to_unit]
    
    return result