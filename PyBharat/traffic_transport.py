def types_of_transport_in_india():
    return [
        "Road Transport",
        "Rail Transport",
        "Air Transport",
        "Water Transport",
        "Metro Rail",
        "Electric Rickshaws & Autos",
        "Public Bus Services",
        "Cycle and Pedestrian Transport"
    ]

def major_indian_highways():
    return [
        "NH 44 – Longest highway (Kashmir to Kanyakumari)",
        "Golden Quadrilateral – Connects 4 metro cities",
        "Delhi–Mumbai Expressway",
        "Eastern Peripheral Expressway",
        "Mumbai–Pune Expressway"
    ]

def public_transport_systems():
    return {
        "Delhi": "Delhi Metro, DTC Buses",
        "Mumbai": "Suburban Local Trains, BEST Buses",
        "Bengaluru": "Namma Metro, BMTC",
        "Chennai": "Chennai Metro, MRTS, MTC Buses",
        "Hyderabad": "Hyderabad Metro, TSRTC",
        "Kolkata": "Kolkata Metro, Trams, Buses"
    }

def vehicle_categories_india():
    return {
        "LMV": "Light Motor Vehicle (Car, Jeep)",
        "HMV": "Heavy Motor Vehicle (Trucks, Buses)",
        "MCWG": "Motorcycle with Gear",
        "MCWOG": "Motorcycle without Gear (Scooter)",
        "EV": "Electric Vehicle (E-Rickshaw, Electric Car)",
        "Passenger Vehicle": "Taxis, Autos, Buses",
        "Commercial Vehicle": "Goods Carriers, Dumpers"
    }

def traffic_rules_summary():
    return [
        "Always wear helmet and seatbelt.",
        "Follow traffic signals and road signs.",
        "Speed limit differs by vehicle and area.",
        "No honking near schools/hospitals.",
        "Drunken driving is punishable.",
        "Mobile phone usage is banned while driving.",
        "Overloading and triple riding is illegal.",
        "Use indicators while turning or overtaking."
    ]

def penalty_for_violations():
    return {
        "Driving without License": "₹5000",
        "Not wearing helmet": "₹1000",
        "Drunken driving": "₹10,000 or 6 months jail",
        "Overspeeding": "₹1000–₹2000",
        "Signal Jumping": "₹1000",
        "Using phone while driving": "₹5000",
        "Pollution certificate missing": "₹10000"
    }

def vehicle_identification_by_number_plate():
    return {
        "White Plate": "Private vehicle",
        "Yellow Plate": "Commercial vehicle",
        "Black Plate with Yellow Letters": "Rental self-drive",
        "Green Plate": "Electric vehicles",
        "Red Plate": "Temporary Registration",
        "Blue Plate": "Foreign Embassy/Consulate"
    }

def traffic_emergency_contacts():
    return {
        "National Highway Helpline": "1033",
        "Traffic Police": "100 / Local control room",
        "Ambulance": "102 / 108",
        "Vehicle Breakdown": "Local RTO or Tow services",
        "Road Accidents": "112 (All-in-one emergency)"
    }

def smart_transport_initiatives():
    return [
        "FASTag for toll collection",
        "Smart traffic lights with AI",
        "Integrated Transport Apps (e.g., Chalo, MoBus)",
        "Electric Buses and Charging Stations",
        "Highway EV corridors",
        "Bharat NCAP – Crash safety rating system"
    ]

def important_transport_documents():
    return [
        "Driving License",
        "RC (Registration Certificate)",
        "PUC Certificate",
        "Vehicle Insurance",
        "Road Tax Receipt",
        "Permit (for commercial vehicles)",
        "Fitness Certificate"
    ]

def famous_indian_rail_routes():
    return [
        "Darjeeling Himalayan Railway",
        "Palace on Wheels (Rajasthan)",
        "Konkan Railway (coastal scenic route)",
        "Nilgiri Mountain Railway",
        "Vande Bharat Express",
        "Tejas Express",
        "Rajdhani & Shatabdi Express"
    ]

def road_safety_tips_for_children():
    return [
        "Use zebra crossing to cross the road.",
        "Never run across the road suddenly.",
        "Wear helmet when cycling.",
        "Use footpaths and signals.",
        "Never lean out of school bus."
    ]

def vehicle_emission_categories():
    return {
        "BS-IV": "Older standard",
        "BS-VI": "Latest emission standard (cleaner fuel)",
        "EV": "Zero emission vehicles",
        "CNG Vehicles": "Low pollution alternative"
    }

def describe_transport_mode(mode):
    mode = mode.lower()
    descriptions = {
        "road": "Includes buses, cars, taxis, trucks, autos — largest network.",
        "rail": "Indian Railways is the 4th largest rail network globally.",
        "air": "Air India, IndiGo, SpiceJet, Vistara operate across domestic and international routes.",
        "water": "Used for inland and coastal shipping; Ganga Waterway is a priority.",
        "metro": "Urban mass transport in major cities – clean and fast."
    }
    return descriptions.get(mode, "Mode not recognized.")

def india_transport_facts():
    return {
        "Length of Roads": "6.3 million km (2024) – 2nd largest in the world",
        "Railway Network": "Over 68,000 km",
        "Major Airports": "Delhi, Mumbai, Bengaluru, Hyderabad, Chennai",
        "Ports": "13 major and 200+ minor ports",
        "EV Push": "Targeting 30% EV by 2030"
    }

def awareness_message():
    return """🚦 Respecting traffic rules saves lives. India's road safety 
mission is 'Sadak Suraksha – Jeevan Raksha'. Citizens must be aware of laws, 
carry valid documents, and report accidents responsibly."""