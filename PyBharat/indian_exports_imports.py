def top_exports():
    return [
        "Petroleum Products",
        "Jewelry and Precious Stones",
        "Pharmaceuticals",
        "Automobiles and Auto Parts",
        "Engineering Goods",
        "Textiles and Garments",
        "Organic Chemicals",
        "Iron and Steel",
        "Agricultural Products (Rice, Tea, Spices)",
        "IT Services and Software"
    ]

def top_imports():
    return [
        "Crude Oil and Petroleum",
        "Gold",
        "Electronic Items",
        "Machinery",
        "Coal and Natural Gas",
        "Chemicals",
        "Fertilizers",
        "Medical Equipment",
        "Plastic Raw Materials",
        "Edible Oils"
    ]

def top_export_partners():
    return [
        "United States",
        "United Arab Emirates (UAE)",
        "China",
        "Bangladesh",
        "Netherlands",
        "Singapore",
        "UK",
        "Germany",
        "Nepal",
        "Saudi Arabia"
    ]

def top_import_partners():
    return [
        "China",
        "United States",
        "UAE",
        "Saudi Arabia",
        "Russia",
        "Iraq",
        "Switzerland",
        "Singapore",
        "Germany",
        "Indonesia"
    ]

def major_export_ports():
    return [
        "Mumbai Port (Maharashtra)",
        "Jawaharlal Nehru Port (Navi Mumbai)",
        "Chennai Port (Tamil Nadu)",
        "Mundra Port (Gujarat)",
        "Kolkata Port (West Bengal)",
        "Visakhapatnam Port (Andhra Pradesh)",
        "Cochin Port (Kerala)",
        "Tuticorin Port (Tamil Nadu)"
    ]

def trade_agreements():
    return {
        "SAFTA": "South Asian Free Trade Area",
        "ASEAN-India FTA": "Free Trade with Southeast Asian Nations",
        "India-UAE CEPA": "Comprehensive Economic Partnership Agreement",
        "India-Australia ECTA": "Trade and Economic Cooperation Agreement",
        "RCEP (Not Joined)": "India opted out of Regional Comprehensive Economic Partnership"
    }

def export_boost_schemes():
    return [
        "MEIS – Merchandise Exports from India Scheme",
        "RoDTEP – Remission of Duties and Taxes on Export Products",
        "SEZ – Special Economic Zones",
        "Duty Drawback Scheme",
        "PLI – Production Linked Incentives for Exporters"
    ]

def import_duties_summary():
    return """India levies customs duty on imported goods based on HS codes. 
Essential items may have low duties, while luxury or non-essential imports like gold or electronics may attract higher rates. 
Anti-dumping duties are applied to protect domestic manufacturers."""

def banned_or_restricted_imports():
    return [
        "Endangered species (under CITES)",
        "Counterfeit currency",
        "Hazardous chemicals without clearance",
        "Certain used electronic goods",
        "Pornographic material",
        "Substandard medical equipment",
        "Fake branded products"
    ]

def major_indian_exports_by_state():
    return {
        "Gujarat": ["Diamonds", "Chemicals", "Textiles"],
        "Maharashtra": ["Automobiles", "Machinery", "Jewelry"],
        "Tamil Nadu": ["Textiles", "Electronics", "Automobile parts"],
        "Punjab": ["Agriculture", "Textiles"],
        "Andhra Pradesh": ["Seafood", "Rice"],
        "Karnataka": ["Software", "Coffee"],
        "West Bengal": ["Tea", "Jute Products"]
    }

def export_certification_bodies():
    return [
        "DGFT – Directorate General of Foreign Trade",
        "APEDA – Agricultural and Processed Food Products Export Development Authority",
        "FIEO – Federation of Indian Export Organisations",
        "Pharmexcil – Pharma Export Council",
        "GJEPC – Gem and Jewellery Export Promotion Council"
    ]

def india_trade_facts():
    return {
        "Trade Deficit": "India often imports more than it exports (negative balance).",
        "Top Export Item": "Petroleum products",
        "Top Import Item": "Crude oil",
        "India’s Forex Reserves (2024)": "Over $600 Billion",
        "Foreign Trade Policy": "Updated every 5 years by DGFT"
    }

def suggest_export_category_by_state(state):
    state = state.lower()
    data = {
        "gujarat": "Textiles, Chemicals, Gems",
        "maharashtra": "Jewelry, Machinery, IT",
        "tamil nadu": "Automobiles, Textiles",
        "andhra pradesh": "Agro & Marine products",
        "karnataka": "Coffee, Electronics, Software"
    }
    return data.get(state, "Export category data not available for this state.")

def trade_summary():
    return """India is a growing trade powerhouse, exporting software, textiles, and jewelry while importing crude oil, electronics, and gold. 
Government schemes like PLI and agreements like CEPA aim to boost exports. India is also focusing on becoming a global manufacturing hub through Atmanirbhar Bharat."""