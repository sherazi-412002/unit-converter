"""Unit conversion package"""

from . import length
from . import mass
from . import temperature
from . import volume
from . import area
from . import time
from . import speed
from . import data
from . import pressure
from . import energy
from . import currency

# Map category names to their respective modules
CONVERTERS = {
    "Length": length,
    "Mass": mass,
    "Temperature": temperature,
    "Volume": volume,
    "Area": area,
    "Time": time,
    "Speed": speed,
    "Data": data,
    "Pressure": pressure,
    "Energy": energy,
    "Currency": currency
}

def get_converter(category):
    """Return the appropriate converter module for the category"""
    return CONVERTERS.get(category)