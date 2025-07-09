def currency_unit():
    return "The currency of India is the Indian Rupee (INR), symbol ₹."

def temperature_unit():
    return "India uses Celsius (°C) for measuring temperature."

def weight_units():
    return {
        "1 kilogram": "1000 grams",
        "1 quintal": "100 kilograms",
        "1 metric tonne": "1000 kilograms",
        "1 tola": "11.66 grams (traditional gold weight)",
        "1 mann": "37.32 kilograms (traditional unit, still used in villages)"
    }

def length_units():
    return {
        "1 meter": "100 centimeters",
        "1 kilometer": "1000 meters",
        "1 foot": "30.48 cm (used in construction)",
        "1 inch": "2.54 cm",
        "1 yard": "0.9144 meters",
        "1 guz": "≈ 0.91 meters (used in fabric measurement)"
    }

def area_units():
    return {
        "1 square meter": "10.76 square feet",
        "1 hectare": "10,000 square meters",
        "1 acre": "4046.86 square meters",
        "1 bigha (North India)": "≈ 2500 to 2700 sq. meters (varies by state)",
        "1 guntha": "≈ 101.17 square meters (common in Maharashtra/Karnataka)"
    }

def volume_units():
    return {
        "1 liter": "1000 milliliters",
        "1 milliliter": "0.001 liter",
        "1 cubic meter": "1000 liters",
        "1 gallon (Indian usage)": "4.546 liters"
    }

def energy_units():
    return {
        "Electricity": "Kilowatt-hour (kWh)",
        "Fuel": "Litre (for petrol, diesel)",
        "Heat": "Joules / Calories (dietary and physics)"
    }

def time_units():
    return {
        "1 minute": "60 seconds",
        "1 hour": "60 minutes",
        "1 day": "24 hours",
        "1 week": "7 days",
        "1 month": "30/31 days",
        "1 year": "12 months"
    }

def speed_units():
    return "India uses Kilometers per hour (km/h) for vehicle speeds."

def agricultural_units():
    return {
        "Land measurement": "Bigha, Acre, Hectare, Guntha (state dependent)",
        "Yield": "Quintals per hectare (Q/ha)",
        "Irrigation": "Cusec (cubic foot/sec), Hectare-meter"
    }

def rainfall_unit():
    return "Rainfall in India is measured in millimeters (mm)."

def pressure_unit():
    return "Barometric pressure is measured in millibar or hectopascal (hPa)."

def humidity_unit():
    return "Measured in percentage (% relative humidity)."

def gold_weight_units():
    return {
        "1 tola": "11.66 grams",
        "1 gram": "Standard unit in modern trading",
        "1 sovereign (8 grams)": "Used in South India for ornaments"
    }

def cooking_units():
    return {
        "1 cup": "≈ 240 ml",
        "1 tablespoon": "≈ 15 ml",
        "1 teaspoon": "≈ 5 ml",
        "Pinch": "Very small amount, varies by context"
    }

def cloth_measurement_units():
    return {
        "1 meter": "Standard fabric measurement unit",
        "1 guz": "≈ 0.91 meter",
        "1 yard": "0.9144 meters"
    }

def list_all_units():
    return [
        "Currency - Rupee (₹)",
        "Temperature - Celsius (°C)",
        "Weight - Kilogram, Quintal, Tola",
        "Length - Meter, Kilometer, Guz",
        "Area - Acre, Bigha, Hectare, Guntha",
        "Volume - Liter, Gallon",
        "Energy - Kilowatt-hour, Joules",
        "Speed - Kilometer per hour",
        "Rainfall - Millimeter",
        "Gold - Gram, Tola, Sovereign",
        "Cloth - Meter, Guz, Yard",
        "Cooking - Cup, Tablespoon, Teaspoon",
        "Pressure - Millibar, hPa",
        "Humidity - Percent (%)"
    ]