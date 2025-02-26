"""Mass conversion module"""

# Conversion factors to kilograms
TO_KG = {
    "Nanogram": 1e-12,
    "Microgram": 1e-9,
    "Milligram": 1e-6,
    "Gram": 1e-3,
    "Kilogram": 1,
    "Metric Ton": 1e3,
    "Ounce": 0.0283495,
    "Pound": 0.453592,
    "Stone": 6.35029,
    "US Ton": 907.185,
    "Imperial Ton": 1016.05
}

# Conversion from kilograms
FROM_KG = {unit: 1/factor for unit, factor in TO_KG.items()}

def convert(value, from_unit, to_unit):
    """Convert between mass units"""
    if value is None:
        return 0
    
    # Convert to kilograms first, then to target unit
    kg = value * TO_KG[from_unit]
    result = kg * FROM_KG[to_unit]
    
    return result