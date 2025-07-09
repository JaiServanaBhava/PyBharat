# __init__.py

__version__ = "0.0.1"
__author__ = "Jai Servana Bhava"
__license__ = "MIT"
__description__ = "🇮🇳 PyBharat: A culturally rich Python library representing India’s heritage, governance, science, and modern identity."

# PyBharat/__init__.py

# Auto-import all modules
from . import (
    award, Cinema, law, Entertainment, river, exam, healthcare, finance,
    festival, historicalplace, temple, sport, company, unit, name, space,
    state, climate, ayurveda, culture, geography, traffic_transport,
    ecommerce, indian_exports_imports, invention, superstition,
    emergency_contact, agriculture, rare_facts, National, NationalSymbol
)

# Optional: Import commonly used modules/functions here (wildcard exposure)
# This will expose selected functions directly when doing: from PyBharat import *
from .award import AwardDetails
from .law import describe_module as law_description
from .temple import get_temple_info
from .exam import describe_module as exam_description
from .finance import describe_module as finance_description
from .sport import describe_sport
from .space import get_rocket_info
from .emergency_contact import all_emergency_contacts
from .agriculture import major_crops
from .name import random_name

# Utility welcome functions
def welcome():
    print("🇮🇳 Welcome to PyBharat – Code with Culture, Script with Spirit!")
