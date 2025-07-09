# agriculture.py

def major_crops():
    return ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton", "Pulses", "Millets"]

def crop_seasons():
    return {
        "Kharif": ["Rice", "Maize", "Soybean", "Cotton"],
        "Rabi": ["Wheat", "Barley", "Mustard", "Peas"],
        "Zaid": ["Cucumber", "Watermelon", "Muskmelon"]
    }

def soil_types():
    return ["Alluvial", "Black", "Red", "Laterite", "Mountain", "Desert"]

def farming_methods():
    return ["Organic Farming", "Mixed Farming", "Subsistence Farming", "Commercial Farming", "Precision Farming"]

def irrigation_methods():
    return ["Drip Irrigation", "Sprinkler", "Surface Irrigation", "Canal", "Tanks"]

def fertilizers_types():
    return {
        "Organic": ["Compost", "Vermicompost", "Green Manure"],
        "Chemical": ["Urea", "DAP", "MOP", "Super Phosphate"]
    }

def tools_and_machines():
    return ["Plough", "Harrow", "Tractor", "Cultivator", "Seeder", "Thresher"]

def indian_agri_states():
    return {
        "Punjab": "Wheat, Rice",
        "Maharashtra": "Cotton, Sugarcane",
        "Uttar Pradesh": "Wheat, Sugarcane",
        "West Bengal": "Rice, Jute",
        "Kerala": "Spices, Coconut"
    }

def top_agricultural_exports():
    return ["Basmati Rice", "Spices", "Tea", "Coffee", "Cotton", "Fruits"]

def govt_agri_schemes():
    return [
        "PM-KISAN", 
        "PM Fasal Bima Yojana", 
        "Soil Health Card Scheme",
        "e-NAM", 
        "Kisan Credit Card"
    ]

def agri_research_centres():
    return [
        "ICAR (Indian Council of Agricultural Research)",
        "IARI (Indian Agricultural Research Institute)",
        "CRIDA",
        "NBPGR"
    ]

def horticulture_crops():
    return ["Mango", "Banana", "Guava", "Citrus", "Tomato", "Onion"]

def millets_names():
    return ["Jowar", "Bajra", "Ragi", "Foxtail Millet", "Kodo"]

def farm_animals():
    return ["Cow", "Buffalo", "Goat", "Sheep", "Poultry", "Honeybee"]

def agri_weather_impact():
    return {
        "Excess Rainfall": "Crop Flooding",
        "Low Rainfall": "Drought Stress",
        "High Temperature": "Crop Drying or Wilt"
    }

def agroforestry_types():
    return ["Silvipasture", "Agrosilviculture", "Hortisilviculture"]

def pesticide_types():
    return ["Insecticides", "Fungicides", "Herbicides", "Rodenticides"]

def irrigation_needed(crop_name):
    water_needs = {
        "Wheat": "Moderate",
        "Rice": "High",
        "Sugarcane": "Very High",
        "Millets": "Low"
    }
    return water_needs.get(crop_name, "Unknown")

def recommended_crops_by_season(season):
    crops = crop_seasons()
    return crops.get(season.capitalize(), [])

def agri_languages_in_india():
    return ["Hindi", "Punjabi", "Marathi", "Telugu", "Tamil", "Bengali", "Kannada"]

def famous_agri_fairs():
    return ["Krishi Darshan", "AgriTech India", "Kisan Mela", "India Agri Progress Expo"]
# agriculture.py

def major_crops():
    return ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton", "Pulses", "Millets"]

def crop_seasons():
    return {
        "Kharif": ["Rice", "Maize", "Soybean", "Cotton"],
        "Rabi": ["Wheat", "Barley", "Mustard", "Peas"],
        "Zaid": ["Cucumber", "Watermelon", "Muskmelon"]
    }

def soil_types():
    return ["Alluvial", "Black", "Red", "Laterite", "Mountain", "Desert"]

def farming_methods():
    return ["Organic Farming", "Mixed Farming", "Subsistence Farming", "Commercial Farming", "Precision Farming"]

def irrigation_methods():
    return ["Drip Irrigation", "Sprinkler", "Surface Irrigation", "Canal", "Tanks"]

def fertilizers_types():
    return {
        "Organic": ["Compost", "Vermicompost", "Green Manure"],
        "Chemical": ["Urea", "DAP", "MOP", "Super Phosphate"]
    }

def tools_and_machines():
    return ["Plough", "Harrow", "Tractor", "Cultivator", "Seeder", "Thresher"]

def indian_agri_states():
    return {
        "Punjab": "Wheat, Rice",
        "Maharashtra": "Cotton, Sugarcane",
        "Uttar Pradesh": "Wheat, Sugarcane",
        "West Bengal": "Rice, Jute",
        "Kerala": "Spices, Coconut"
    }

def top_agricultural_exports():
    return ["Basmati Rice", "Spices", "Tea", "Coffee", "Cotton", "Fruits"]

def govt_agri_schemes():
    return [
        "PM-KISAN", 
        "PM Fasal Bima Yojana", 
        "Soil Health Card Scheme",
        "e-NAM", 
        "Kisan Credit Card"
    ]

def agri_research_centres():
    return [
        "ICAR (Indian Council of Agricultural Research)",
        "IARI (Indian Agricultural Research Institute)",
        "CRIDA",
        "NBPGR"
    ]

def horticulture_crops():
    return ["Mango", "Banana", "Guava", "Citrus", "Tomato", "Onion"]

def millets_names():
    return ["Jowar", "Bajra", "Ragi", "Foxtail Millet", "Kodo"]

def farm_animals():
    return ["Cow", "Buffalo", "Goat", "Sheep", "Poultry", "Honeybee"]

def agri_weather_impact():
    return {
        "Excess Rainfall": "Crop Flooding",
        "Low Rainfall": "Drought Stress",
        "High Temperature": "Crop Drying or Wilt"
    }

def agroforestry_types():
    return ["Silvipasture", "Agrosilviculture", "Hortisilviculture"]

def pesticide_types():
    return ["Insecticides", "Fungicides", "Herbicides", "Rodenticides"]

def irrigation_needed(crop_name):
    water_needs = {
        "Wheat": "Moderate",
        "Rice": "High",
        "Sugarcane": "Very High",
        "Millets": "Low"
    }
    return water_needs.get(crop_name, "Unknown")

def recommended_crops_by_season(season):
    crops = crop_seasons()
    return crops.get(season.capitalize(), [])

def agri_languages_in_india():
    return ["Hindi", "Punjabi", "Marathi", "Telugu", "Tamil", "Bengali", "Kannada"]

def famous_agri_fairs():
    return ["Krishi Darshan", "AgriTech India", "Kisan Mela", "India Agri Progress Expo"]