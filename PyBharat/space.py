# astro_space.py

def ancient_astronomers():
    return ["Aryabhata", "Varahamihira", "Bhaskara I", "Bhaskara II", "Lagadha"]

def famous_isro_missions():
    return ["Chandrayaan-1", "Chandrayaan-2", "Chandrayaan-3", "Mangalyaan", "Aditya-L1", "Gaganyaan"]

def indian_satellites():
    return ["INSAT", "IRS", "GSAT", "RISAT", "Cartosat", "NavIC"]

def vedic_constellations():
    return ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira"]

def navagraha_names():
    return ["Surya", "Chandra", "Mangala", "Budha", "Guru", "Shukra", "Shani", "Rahu", "Ketu"]

def indian_space_centres():
    return ["ISRO HQ", "VSSC", "SHAR", "URSC", "SDSC", "ISTRAC"]

def planetary_positions_today():
    return {"Sun": "Cancer", "Moon": "Pisces", "Mars": "Leo"}  # Dummy sample

def zodiac_signs_sanskrit():
    return ["Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya", "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Meena"]

def lunar_phases():
    return ["Amavasya", "Shukla Paksha", "Purnima", "Krishna Paksha"]

def indian_astronomy_books():
    return ["Aryabhatiya", "Surya Siddhanta", "Pancha Siddhantika", "Brahmasphutasiddhanta"]

def rashi_names():
    return zodiac_signs_sanskrit()

def nakshatra_list():
    return vedic_constellations()

def calculate_birth_rashi(name):
    return "Simha"  # Dummy logic

def calculate_nakshatra(dob):
    return "Rohini"  # Dummy logic

def vedic_cosmos_layers():
    return ["Bhuloka", "Bhuvarloka", "Svarloka", "Maharloka", "Janarloka", "Tapoloka", "Satyaloka"]

def sacred_planets_in_puranas():
    return ["Surya", "Chandra", "Shukra", "Budha", "Mangal", "Guru", "Shani"]

def isro_founding_year():
    return 1969

def founder_of_isro():
    return "Dr. Vikram Sarabhai"

def moon_missions_india():
    return ["Chandrayaan-1", "Chandrayaan-2", "Chandrayaan-3"]

def mars_mission_india():
    return ["Mangalyaan"]

def future_space_missions():
    return ["Shukrayaan", "Gaganyaan", "LUPEX", "Aditya-L2"]

def solar_system_in_sanskrit():
    return ["Surya", "Budha", "Shukra", "Prithvi", "Mangala", "Guru", "Shani", "Uranus", "Neptune"]

def indian_calendar_systems():
    return ["Saka Calendar", "Vikram Samvat", "Tamil Calendar", "Malayalam Calendar"]

def arya_sidereal_year():
    return 365.25636  # Sidereal year in Aryabhata’s calculation

def navagraha_temples():
    return ["Suryanar Kovil", "Thingalur", "Vaitheeswaran Koil", "Kanjanoor", "Keezhperumpallam"]

def daily_panchang():
    return {"Tithi": "Dwitiya", "Nakshatra": "Rohini", "Yoga": "Siddhi", "Karana": "Bava"}

def vedanga_jyotisha_subjects():
    return ["Kalpa", "Ganit", "Hora", "Samhita", "Siddhanta"]

def space_related_ministries():
    return ["Department of Space", "DOS", "Antrix Corporation", "IN-SPACe"]

def famous_space_scientists_india():
    return ["Vikram Sarabhai", "Satish Dhawan", "A.P.J Abdul Kalam", "K. Sivan", "S. Somanath"]

def astrosat_mission_details():
    return {
        "Launch Year": 2015,
        "Purpose": "Multi-wavelength Space Observatory",
        "Orbit": "Low Earth Orbit",
        "Status": "Active"
    }

def astrology_vs_astronomy():
    return {
        "Astronomy": "Scientific study of celestial bodies",
        "Astrology": "Belief in celestial influence on human life"
    }
def get_rocket_info(rocket_name):
    rockets = {
        "sounding_rocket": "India's first rocket, launched in 1963 from Thumba. Used for atmospheric studies.",
        "slv": "Satellite Launch Vehicle (SLV) – India’s first experimental satellite launcher, successfully launched Rohini satellite in 1980.",
        "aslv": "Augmented Satellite Launch Vehicle – Used in the 1980s and early 90s, mainly for technology development.",
        "pslv": "Polar Satellite Launch Vehicle – India’s workhorse rocket, used to launch satellites into polar and sun-synchronous orbits.",
        "gslv": "Geosynchronous Satellite Launch Vehicle – Used to place heavier payloads into geostationary orbit.",
        "gslv_mk2": "An improved GSLV with an indigenously developed cryogenic upper stage.",
        "gslv_mk3": "Also called LVM3 – ISRO’s most powerful rocket, used for Chandrayaan-2 and 3 missions. Will be used in Gaganyaan.",
        "sslv": "Small Satellite Launch Vehicle – A mini launcher designed for quick, cost-effective deployment of small satellites.",
        "rslv": "Reusable Satellite Launch Vehicle – Experimental spaceplane under development for low-cost access to space.",
        "agni": "India’s strategic missile, not a space launch vehicle, but often confused due to its rocket shape.",
        "prithvi": "Short-range ballistic missile, part of India’s missile development program, not for satellite launch.",
        "vikas_engine": "A powerful liquid-fueled rocket engine developed by ISRO, used in PSLV and GSLV stages.",
        "lvm3": "Launch Vehicle Mark-3 – New official name for GSLV Mk III. Carries heavy payloads and future crewed missions.",
        "sron": "Sounding rockets of Rohini series for upper atmospheric studies. Still used today by ISRO."
    }

    key = rocket_name.strip().lower().replace(" ", "_")
    return rockets.get(key, "Rocket not found. Please check the name or try a known ISRO rocket.")