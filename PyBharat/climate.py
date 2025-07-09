def india_seasons():
    return ["Winter (Dec-Feb)", "Summer (Mar-May)", "Monsoon (Jun-Sep)", "Post-Monsoon/Autumn (Oct-Nov)"]

def current_season(month):
    month = month.lower()
    if month in ["dec", "jan", "feb"]:
        return "Winter in India 🌨️"
    elif month in ["mar", "apr", "may"]:
        return "Summer in India ☀️"
    elif month in ["jun", "jul", "aug", "sep"]:
        return "Monsoon Season 🌧️"
    elif month in ["oct", "nov"]:
        return "Post-Monsoon / Autumn 🍂"
    else:
        return "Invalid month input."

def indian_climate_zones():
    return {
        "Tropical Wet": ["Kerala", "Goa", "Andaman & Nicobar"],
        "Tropical Dry": ["Madhya Pradesh", "Rajasthan"],
        "Mountain Climate": ["Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand"],
        "Arid (Desert)": ["Rajasthan", "Gujarat"],
        "Coastal": ["Tamil Nadu", "Odisha", "West Bengal"]
    }

def famous_weather_events():
    return [
        "Amphan Cyclone (2020)", "Kerala Floods (2018)", "Odisha Super Cyclone (1999)", 
        "Chennai Floods (2015)", "Dust Storms in Rajasthan"
    ]

def hottest_places_india():
    return ["Phalodi (Rajasthan)", "Nagpur (Maharashtra)", "Banda (Uttar Pradesh)"]

def coldest_places_india():
    return ["Dras (Ladakh)", "Leh", "Spiti Valley", "Siachen Glacier"]

def wettest_places_india():
    return ["Mawsynram", "Cherrapunji", "Agumbe", "Pasighat"]

def dryest_places_india():
    return ["Jaisalmer", "Bikaner", "Barmer"]

def monsoon_facts():
    return {
        "Southwest Monsoon": "Starts from Kerala around June 1st.",
        "Northeast Monsoon": "Affects Tamil Nadu and Andhra in Oct-Dec.",
        "IMD Role": "Monsoon is tracked and forecasted by the Indian Meteorological Department (IMD)."
    }

def imd_alert_types():
    return {
        "Yellow": "Be Aware",
        "Orange": "Be Prepared",
        "Red": "Take Action (Severe Weather)"
    }

def air_quality_index_levels():
    return {
        "0-50": "Good",
        "51-100": "Satisfactory",
        "101-200": "Moderate",
        "201-300": "Poor",
        "301-400": "Very Poor",
        "401-500": "Severe"
    }

def common_cyclone_names_india():
    return ["Hudhud", "Phailin", "Fani", "Amphan", "Yaas", "Nisarga"]

def cyclone_prone_states():
    return ["Odisha", "Andhra Pradesh", "West Bengal", "Tamil Nadu", "Gujarat"]

def fog_prone_regions():
    return ["Delhi", "Punjab", "Uttar Pradesh", "Bihar"]

def flood_prone_regions():
    return ["Assam", "Kerala", "Bihar", "Odisha", "Uttarakhand"]

def dust_storm_regions():
    return ["Rajasthan", "Haryana", "Delhi", "Western UP"]

def temperature_extremes():
    return {
        "Highest Ever Recorded": "51°C in Phalodi, Rajasthan (2016)",
        "Lowest Recorded": "-60°C in Dras, Ladakh"
    }

def himalayan_climate():
    return "Alpine and tundra-like climate with snowfall from Oct-March and sub-zero temps year-round in higher altitudes."

def western_ghats_climate():
    return "Tropical monsoon climate with heavy rains from June to September."

def thar_desert_climate():
    return "Hot and dry with temperature crossing 48°C in summers, extremely cold winters at night."

def coastal_climate_characteristics():
    return "Moderate temperatures, high humidity, and heavy monsoon rains."

def summer_heatwaves_info():
    return "Northern plains, especially Rajasthan and UP, experience deadly heatwaves during May-June."

def el_nino_impact():
    return "El Niño causes weaker monsoon in India; affects agriculture and economy."

def cloudburst_regions():
    return ["Uttarakhand", "Jammu & Kashmir", "Himachal Pradesh", "North East India"]

def wind_patterns_india():
    return {
        "Summer": "Southwest Monsoon winds from sea to land",
        "Winter": "Northeast winds from land to sea"
    }

def sunniest_cities():
    return ["Jodhpur", "Bikaner", "Ahmedabad", "Jaipur"]

def snow_cities():
    return ["Shimla", "Manali", "Auli", "Leh", "Gulmarg"]

def cyclone_seasons():
    return {
        "Pre-Monsoon": "April to June",
        "Post-Monsoon": "October to December"
    }

def humidity_zones():
    return {
        "Very High": ["Mumbai", "Kolkata", "Chennai"],
        "Low": ["Rajasthan", "Ladakh", "Punjab (Winter)"]
    }

def sunrise_sunset_difference():
    return "In India, the eastern states like Arunachal experience sunrise much earlier than western states like Gujarat (up to 2-hour difference)."

def climate_change_effects():
    return [
        "Melting glaciers in Himalayas", 
        "Erratic monsoons",
        "Rising sea level in coastal cities",
        "More cyclones in Bay of Bengal & Arabian Sea"
    ]

def major_weather_institutions():
    return {
        "IMD": "Indian Meteorological Department",
        "IITM Pune": "Research on monsoon",
        "SAFAR": "Air Quality Index system for major cities"
    }

def desertification_regions():
    return ["Western Rajasthan", "Kutch in Gujarat", "South Punjab", "South Haryana"]

def rain_shadow_areas():
    return ["Leeward side of Western Ghats – Solapur, Rayalaseema, Tamil Nadu Plateau"]

def rainfall_trend():
    return "India receives around 75% of its total annual rainfall during the monsoon season (June–September)."

def seasonal_crop_dependence():
    return {
        "Kharif Crops": "Need monsoon rains (June–Oct) - Rice, Maize, Bajra",
        "Rabi Crops": "Grown in winter - Wheat, Mustard, Barley"
    }

def describe_weather_in(city):
    city = city.lower()
    data = {
        "delhi": "Extremely hot in summer (up to 45°C), foggy in winter, moderate monsoon.",
        "mumbai": "Hot and humid with heavy monsoon rains. Moderate winters.",
        "kolkata": "Humid subtropical climate with hot summers and very rainy monsoons.",
        "chennai": "Tropical climate, less summer rainfall but heavy Northeast monsoon in Oct-Dec.",
        "leh": "Cold desert climate, dry and cold year-round. Heavy snow in winters."
    }
    return data.get(city, "City not found or data unavailable.")