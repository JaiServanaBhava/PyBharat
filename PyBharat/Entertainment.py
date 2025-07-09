def list_media_houses():
    return [
        "Times Group (Bennett Coleman)", "Zee Entertainment", "Network18", 
        "India Today Group", "Sun Group", "NDTV", "ABP Group", "TV Today Network", 
        "Asianet", "ETV Network", "Republic Media", "News Nation", "TV9", "Doordarshan", "DD News"
    ]

def list_film_production_companies():
    return [
        "Yash Raj Films", "Red Chillies Entertainment", "Dharma Productions", 
        "Balaji Telefilms", "Viacom18 Motion Pictures", "T-Series", 
        "Eros International", "Bhansali Productions", "Phantom Films", "Excel Entertainment"
    ]

def list_ott_platforms():
    return [
        "Netflix India", "Amazon Prime Video", "Disney+ Hotstar", 
        "Zee5", "Sony LIV", "JioCinema", "ALT Balaji", "MX Player", "Voot", "Aha"
    ]

def describe_media_company(name):
    name = name.lower()
    descriptions = {
        "times group": "Publisher of The Times of India, and owner of Times Now, ET Now, and more.",
        "zee": "One of India's largest TV networks offering news, entertainment, and regional channels.",
        "ndtv": "A pioneering news channel known for NDTV India and NDTV 24x7.",
        "viacom18": "Media company operating Colors TV, Voot, and movie production.",
        "dd news": "Government-owned Doordarshan's news broadcast channel."
    }
    return descriptions.get(name, "Media company description not found.")

def list_regional_media_networks():
    return [
        "Sun TV Network – Tamil", "Asianet – Malayalam", "ETV Network – Telugu", 
        "Zee Marathi", "TV9 Kannada", "Raj TV – Tamil", "Colors Bangla", "ABP Ananda – Bengali"
    ]