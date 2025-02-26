"""Currency conversion module"""

import datetime

# Exchange rates relative to USD (as of February 2025 - this is a simulation)
# These would normally be fetched from an API in a real application
EXCHANGE_RATES = {
    "USD": 1.0,        # US Dollar (base)
    "EUR": 0.92,       # Euro
    "GBP": 0.78,       # British Pound 
    "JPY": 115.2,      # Japanese Yen
    "CAD": 1.34,       # Canadian Dollar
    "AUD": 1.50,       # Australian Dollar
    "CHF": 0.88,       # Swiss Franc
    "CNY": 6.95,       # Chinese Yuan
    "INR": 82.6,       # Indian Rupee
    "RUB": 90.3,
    "PKR": 279.75,        # Russian Ruble
}

# Last update timestamp (simulated)
LAST_UPDATE = datetime.datetime.now() - datetime.timedelta(hours=4)

def convert(value, from_currency, to_currency):
    """Convert between currencies"""
    if value is None:
        return 0
    
    # Convert to USD first, then to target currency
    usd_amount = value / EXCHANGE_RATES[from_currency]
    result = usd_amount * EXCHANGE_RATES[to_currency]
    
    return result

def get_last_update():
    """Get the timestamp of the last exchange rate update"""
    return LAST_UPDATE.strftime("%Y-%m-%d %H:%M:%S UTC")