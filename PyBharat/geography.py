def india_location():
    return "India lies in the Northern Hemisphere, between 8°4′ and 37°6′ North latitude, and 68°7′ and 97°25′ East longitude."

def india_neighbors():
    return ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar", "Afghanistan (via PoK)", "Sri Lanka (via sea)"]

def india_highest_mountain():
    return "Kangchenjunga – 8,586 m (3rd highest in the world), located in Sikkim."

def india_longest_river():
    return "Ganga (2,525 km) – Flows through Uttarakhand, UP, Bihar, Jharkhand, and West Bengal."

def major_rivers():
    return ["Ganga", "Yamuna", "Brahmaputra", "Godavari", "Krishna", "Narmada", "Tapi", "Mahanadi", "Kaveri", "Sutlej"]

def indian_deserts():
    return "The Thar Desert – Located in Rajasthan, extends to parts of Gujarat, Punjab, and Haryana."

def coastal_states():
    return ["Gujarat", "Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu", "Andhra Pradesh", "Odisha", "West Bengal"]

def island_territories():
    return {
        "Andaman and Nicobar Islands": "Bay of Bengal",
        "Lakshadweep Islands": "Arabian Sea"
    }

def indian_plateaus():
    return ["Deccan Plateau", "Chotanagpur Plateau", "Malwa Plateau", "Karnataka Plateau", "Meghalaya Plateau"]

def major_mountain_ranges():
    return ["Himalayas", "Aravallis", "Vindhyas", "Satpura", "Western Ghats", "Eastern Ghats"]

def forest_types():
    return ["Tropical Evergreen", "Tropical Deciduous", "Thorn", "Montane", "Mangrove"]

def biosphere_reserves():
    return [
        "Nilgiri", "Nanda Devi", "Sundarbans", "Gulf of Mannar",
        "Great Nicobar", "Simlipal", "Pachmarhi", "Achanakmar-Amarkantak"
    ]

def national_boundaries():
    return {
        "Pakistan": "3323 km",
        "China":" 3488 km",
        "Bangladesh": "4096 km (Longest)",
        "Nepal": "1751 km",
        "Myanmar": "1643 km",
        "Bhutan":" 699 km",
        "Afghanistan": "106 km"
    }

def climate_zones():
    return {
        "Tropical Wet": "Western Ghats, North-East",
        "Tropical Dry": "Central India",
        "Subtropical Humid": "North India",
        "Mountain": "Himalayan Region",
        "Arid": "Rajasthan"
    }

def states_with_highest_rainfall():
    return {
        "Meghalaya": "Mawsynram (highest rainfall in the world)",
        "Kerala": "Heavy monsoon rains",
        "Goa": "High coastal rainfall"
    }

def largest_states_by_area():
    return [
        "Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh", "Gujarat"
    ]

def longest_border_with_country():
    return "Bangladesh – 4,096 km"

def total_land_area():
    return "India has a land area of ~3.28 million square kilometers (7th largest in the world)."

def get_river_info(name):
    name = name.lower()
    info = {
        "ganga": "Longest river, originates from Gangotri Glacier.",
        "yamuna": "Tributary of Ganga, joins it at Allahabad (Prayagraj).",
        "brahmaputra": "Flows from Tibet (Tsangpo) into Assam and Bangladesh.",
        "godavari": "Longest river in peninsular India.",
        "krishna": "Flows through Maharashtra, Karnataka, and Andhra Pradesh.",
        "narmada": "Flows westward into Arabian Sea, important for hydro projects.",
    }
    return info.get(name, "River information not found.")

def print_major_geography():
    print(india_location())
    print("Neighbors:", ", ".join(india_neighbors()))
    print("Highest Mountain:", india_highest_mountain())
    print("Longest River:", india_longest_river())
    print("Desert:", indian_deserts())
    print("Coastal States:", coastal_states())
    
print_major_geography()