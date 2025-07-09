def list_major_rivers():
    return ["Ganga", "Yamuna", "Brahmaputra", "Godavari", "Krishna", "Cauvery", "Narmada", "Tapti", "Mahanadi", "Sutlej"]

def river_origin(river):
    data = {
        "ganga": "Gangotri Glacier, Uttarakhand",
        "yamuna": "Yamunotri Glacier, Uttarakhand",
        "brahmaputra": "Angsi Glacier, Tibet",
        "godavari": "Trimbakeshwar, Maharashtra",
        "krishna": "Mahabaleshwar, Maharashtra",
        "cauvery": "Talakaveri, Karnataka",
        "narmada": "Amarkantak Plateau, Madhya Pradesh",
        "tapti": "Satpura Range, Madhya Pradesh",
        "mahanadi": "Sihawa, Chhattisgarh",
        "saraswati": "Lost river, believed to originate from Himalayas"
    }
    return data.get(river.lower(), "River not found.")

def states_covered_by_river(river):
    data = {
        "ganga": ["Uttarakhand", "Uttar Pradesh", "Bihar", "Jharkhand", "West Bengal"],
        "yamuna": ["Uttarakhand", "Himachal Pradesh", "Haryana", "Delhi", "Uttar Pradesh"],
        "brahmaputra": ["Arunachal Pradesh", "Assam"],
        "godavari": ["Maharashtra", "Telangana", "Andhra Pradesh", "Chhattisgarh", "Odisha"],
        "krishna": ["Maharashtra", "Karnataka", "Andhra Pradesh", "Telangana"],
        "cauvery": ["Karnataka", "Tamil Nadu"],
        "narmada": ["Madhya Pradesh", "Maharashtra", "Gujarat"],
        "tapti": ["Madhya Pradesh", "Maharashtra", "Gujarat"],
        "mahanadi": ["Chhattisgarh", "Odisha"]
    }
    return data.get(river.lower(), "River not found or incomplete data.")

def river_length_km(river):
    data = {
        "ganga": 2525,
        "yamuna": 1376,
        "brahmaputra": 2900,
        "godavari": 1465,
        "krishna": 1400,
        "cauvery": 800,
        "narmada": 1312,
        "tapti": 724,
        "mahanadi": 858
    }
    return data.get(river.lower(), "Length not available.")

def important_river_projects():
    return [
        "Tehri Dam – Ganga",
        "Sardar Sarovar Dam – Narmada",
        "Nagarjuna Sagar – Krishna",
        "Hirakud Dam – Mahanadi",
        "Bhakra Nangal – Sutlej"
    ]

def list_major_dams():
    return [
        "Tehri Dam", "Sardar Sarovar Dam", "Bhakra Nangal", "Hirakud Dam", "Nagarjuna Sagar",
        "Indira Sagar", "Tungabhadra Dam", "Koyna Dam", "Rihand Dam", "Mettur Dam"
    ]

def dam_river_relation(dam):
    data = {
        "tehri dam": "Built on Bhagirathi River (a tributary of Ganga)",
        "sardar sarovar": "Narmada River",
        "bhakra nangal": "Sutlej River",
        "hirakud": "Mahanadi River",
        "nagarjuna sagar": "Krishna River",
        "indira sagar": "Narmada River",
        "tungabhadra": "Tungabhadra River",
        "koyna": "Koyna River",
        "rihand": "Rihand River (Tributary of Son)",
        "mettur": "Cauvery River"
    }
    return data.get(dam.lower(), "Dam not found.")

def largest_river_by_volume():
    return "Brahmaputra – known for massive water flow and flooding."

def longest_river_in_india():
    return "Ganga – 2525 km"

def west_flowing_rivers():
    return ["Narmada", "Tapti", "Mahi", "Sabarmati", "Periyar"]

def east_flowing_rivers():
    return ["Ganga", "Godavari", "Krishna", "Cauvery", "Mahanadi"]

def interlinking_project():
    return "Ken-Betwa River Linking Project is India's first river interlinking project."

def dam_height(dam):
    data = {
        "tehri": "260.5 m (tallest dam in India)",
        "sardar sarovar": "163 m",
        "bhakra nangal": "226 m",
        "hirakud": "61 m (longest dam)",
        "indira sagar": "92 m"
    }
    return data.get(dam.lower(), "Height data not available.")

def list_tributaries(river):
    data = {
        "ganga": ["Yamuna", "Ghaghara", "Gandak", "Kosi", "Son"],
        "yamuna": ["Tons", "Hindon", "Chambal", "Betwa", "Ken"],
        "godavari": ["Purna", "Pranhita", "Indravati", "Manjira"],
        "krishna": ["Bhima", "Tungabhadra", "Musi"],
        "narmada": ["Tawa", "Hiran", "Shakkar"]
    }
    return data.get(river.lower(), "No tributary data found.")

def dams_by_state(state):
    data = {
        "uttarakhand": ["Tehri Dam"],
        "gujarat": ["Sardar Sarovar"],
        "odisha": ["Hirakud"],
        "punjab": ["Bhakra Nangal"],
        "karnataka": ["Tungabhadra", "Almatti", "Krishna Raja Sagara"],
        "tamil nadu": ["Mettur Dam", "Vaigai Dam"],
        "maharashtra": ["Koyna Dam", "Jayakwadi", "Ujjani"]
    }
    return data.get(state.lower(), "No data found for this state.")

def largest_reservoir():
    return "Indira Sagar Reservoir on Narmada River"

def dams_used_for_flood_control():
    return ["Hirakud", "Tehri", "Bhakra Nangal", "Tungabhadra"]

def rivers_with_delta():
    return ["Ganga", "Godavari", "Krishna", "Cauvery", "Mahanadi"]

def rivers_without_delta():
    return ["Narmada", "Tapti", "Sabarmati"]

def river_facts():
    return [
        "Ganga is considered sacred and personified as Goddess Ganga.",
        "Narmada flows westward and does not form a delta.",
        "Brahmaputra floods Assam annually.",
        "Yamuna is a major tributary of Ganga but highly polluted."
    ]

def lost_rivers():
    return ["Saraswati", "Drishadvati", "Kumudvati"]

def river_pollution_issues():
    return {
        "Ganga": "Industrial waste, religious dumping",
        "Yamuna": "Sewage and chemical waste from Delhi",
        "Sabarmati": "Industrial discharge in Gujarat"
    }

def ganga_cleaning_program():
    return "Namami Gange – Flagship program to clean and rejuvenate the Ganga River."

def international_rivers():
    return {
        "Brahmaputra": "India, China, Bangladesh",
        "Sutlej": "China, India, Pakistan",
        "Indus": "China, India, Pakistan"
    }

def water_disputes():
    return {
        "Cauvery": "Between Karnataka and Tamil Nadu",
        "Krishna": "Maharashtra, Karnataka, Andhra Pradesh",
        "Ravi-Beas": "Punjab and Haryana"
    }

def navigation_rivers():
    return ["Ganga", "Brahmaputra", "Godavari", "Hooghly"]

def holy_rivers_india():
    return ["Ganga", "Yamuna", "Saraswati", "Godavari", "Narmada", "Kshipra"]

def rivers_in_indus_system():
    return ["Indus", "Jhelum", "Chenab", "Ravi", "Beas", "Sutlej"]

def describe_river(name):
    river = name.lower()
    if river == "ganga":
        return "Ganga is the most sacred and longest river of India flowing from Gangotri to Bay of Bengal."
    elif river == "narmada":
        return "Narmada flows westward and is considered holy; it doesn't form a delta."
    elif river == "brahmaputra":
        return "Brahmaputra originates in Tibet and causes annual floods in Assam."
    elif river == "krishna":
        return "Krishna flows across South India and supports major irrigation in Maharashtra and Andhra."
    else:
        return "River data not available."