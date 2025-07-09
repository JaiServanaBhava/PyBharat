def indian_inventions():
    return {
        "Zero (0)": "Invented by Aryabhata, an ancient Indian mathematician.",
        "Decimal System": "Developed in India, forming the foundation of modern mathematics.",
        "Chess": "Originated as ‘Chaturanga’ in ancient India.",
        "Ayurveda": "An ancient Indian system of medicine developed over 5000 years ago.",
        "Yoga": "Spiritual and physical discipline originated in India.",
        "Plastic Surgery": "Practiced by Sushruta in ancient India (~600 BCE).",
        "Cataract Surgery": "Performed using curved needles by Indian physicians in ancient times.",
        "Iron & Steel Smelting": "Wootz steel was a high-quality Indian invention.",
        "Buttons": "First used in the Indus Valley Civilization for ornamental purposes.",
        "Shampoo": "Originated from the Hindi word ‘chāmpo’ – a head massage.",
        "Water Harvesting System": "Ancient stepwells and tanks used across India for sustainable water collection.",
        "Binary Numbers": "Concept of binary number system was described by Pingala in the 2nd century BCE.",
        "Measurement Systems": "Indus Valley had standardized weights and measures.",
        "Zinc Extraction": "India pioneered extraction of zinc by distillation technique in Zawar mines (Rajasthan).",
        "Fiber Optics Theory": "Concept proposed by Indian physicist Narinder Singh Kapany, known as the father of fiber optics.",
        "Radio-Wave Remote Communication": "Invented by Jagadish Chandra Bose, before Marconi's patent.",
        "Crescent-Shaped Scalpels": "Used in ancient Indian surgeries.",
        "Heliocentric Theory": "Proposed by Aryabhata centuries before Copernicus.",
        "Ink & Writing Instruments": "Early form of ink and pens developed during Vedic period.",
        "Diamond Mining": "India was the only known source of diamonds until the 18th century.",
        "Algebra": "Brahmagupta made major contributions to algebra.",
        "Trigonometry": "Advanced forms used in Indian astronomy and mathematics.",
        "Sanskrit Grammar": "Panini's 'Ashtadhyayi' is the earliest known grammar of any language.",
        "Iron Pillar of Delhi": "Corrosion-resistant iron pillar from 4th century CE, still standing strong.",
        "Cotton Cultivation & Weaving": "Indus Valley Civilization was among the first to cultivate and weave cotton.",
        "Brahmastra Concept": "Mentioned in ancient Indian epics, considered a mythical divine weapon.",
        "Rocket Artillery (Mysorean Rockets)": "Used by Tipu Sultan’s army, later studied and adapted by British.",
        "Ink Manufacturing": "Carbon-based ink production from lampblack in ancient India.",
        "Magnet Use": "Used in traditional Indian medicine and navigation.",
        "Arithmetic Progression": "Explained in ancient Indian mathematical texts."
    }

def invention_detail(name):
    data = list_indian_inventions()
    key = name.strip().lower()
    for item, desc in data.items():
        if key in item.lower():
            return f"{item}: {desc}"
    return "⚠️ Invention not found in Indian records. Try another keyword."

def all_inventions():
    data = list_indian_inventions()
    for name, description in data.items():
        print(f"{name}: {description}")