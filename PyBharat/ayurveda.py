# ayurveda_yoga.py

def get_dosha_types():
    """Return the three fundamental doshas in Ayurveda."""
    return ["Vata", "Pitta", "Kapha"]

def get_classical_ayurveda_texts():
    """Return key ancient Ayurveda texts from India."""
    return ["Charaka Samhita", "Sushruta Samhita", "Ashtanga Hridaya"]

def describe_body_types():
    """Describe the three Ayurvedic body types."""
    return {
        "Vata": "Energetic, thin, creative",
        "Pitta": "Intelligent, driven, medium build",
        "Kapha": "Calm, strong, emotionally grounded"
    }

def guess_dosha_from_symptom(symptom):
    """Suggest a likely dosha imbalance based on a symptom."""
    s = symptom.lower()
    if "dry" in s:
        return "Possibly Vata imbalance"
    elif "acid" in s:
        return "Possibly Pitta imbalance"
    elif "lazy" in s or "heavy" in s:
        return "Possibly Kapha imbalance"
    else:
        return "Cannot determine"

def get_daily_ayurvedic_routine():
    """Return daily routine practices according to Ayurveda."""
    return ["Wake up at Brahma Muhurta", "Oil pulling", "Yoga", "Herbal tea", "Mindful meals", "Meditation"]

def list_common_herbs():
    """List some widely used Ayurvedic herbs."""
    return ["Ashwagandha", "Tulsi", "Giloy", "Brahmi", "Amla", "Haritaki"]

def get_herb_usage(herb):
    """Return traditional Indian use of a specific herb."""
    herb = herb.lower()
    benefits = {
        "ashwagandha": "Used to reduce stress and boost strength.",
        "tulsi": "Used for boosting immunity and lung health.",
        "brahmi": "Improves memory and brain function.",
        "amla": "Rich in Vitamin C, boosts immunity and digestion.",
        "giloy": "Effective against fever and infections.",
        "shatavari": "Supports women’s reproductive health."
    }
    return benefits.get(herb, "Herb not found.")

def get_basic_asanas():
    """List basic yoga poses with Sanskrit names."""
    return ["Tadasana", "Vrikshasana", "Bhujangasana", "Dhanurasana", "Shavasana"]

def get_surya_namaskar_steps():
    """Return number of poses in one round of Surya Namaskar."""
    return 12

def breathing_for_focus():
    """List pranayama (breathing) techniques to improve focus."""
    return ["Anulom Vilom", "Bhramari", "Nadi Shodhana"]

def food_suggestions_by_dosha(dosha):
    """Suggest Indian foods based on a person's dosha."""
    dosha = dosha.lower()
    foods = {
        "vata": ["Warm soups", "Cooked grains", "Milk", "Ghee"],
        "pitta": ["Coconut", "Mint", "Cucumber", "Buttermilk"],
        "kapha": ["Spices", "Green tea", "Millets", "Light meals"]
    }
    return foods.get(dosha, [])

def list_immunity_boosters():
    """Return Ayurvedic remedies to build immunity."""
    return ["Chyawanprash", "Turmeric milk", "Tulsi decoction", "Giloy juice"]

def get_panchakarma_methods():
    """Return the 5 main therapies of Panchakarma treatment."""
    return ["Vamana", "Virechana", "Basti", "Nasya", "Raktamokshana"]

def list_indian_meditation_styles():
    """List ancient meditation methods from India."""
    return ["Vipassana", "Yoga Nidra", "Nada Yoga", "Transcendental Meditation"]

def get_chakras_with_names():
    """Return all 7 chakras by their Sanskrit names."""
    return ["Muladhara", "Swadhisthana", "Manipura", "Anahata", "Vishuddha", "Ajna", "Sahasrara"]

def ayurvedic_sleep_tips():
    """Return bedtime practices based on Ayurveda."""
    return ["Warm oil massage", "Avoid screens", "Drink milk", "Sleep by 10 PM"]

def yoga_for_digestion():
    """List yoga poses that help digestion."""
    return ["Pavanamuktasana", "Vajrasana", "Trikonasana"]

def yoga_for_children():
    """Child-safe and easy yoga poses for school kids."""
    return ["Butterfly pose", "Tree pose", "Cat-Cow stretch"]

def detox_practices_during_festivals():
    """Traditional Indian festive season detox rituals."""
    return ["Fasting on Ekadashi", "Tulsi water", "Oil bath"]

def ayurvedic_skin_care():
    """Natural Indian ways to care for skin."""
    return ["Neem paste", "Sandalwood", "Multani mitti", "Turmeric milk"]

def ayurveda_courses_in_india():
    """Popular Ayurveda courses for medical studies in India."""
    return ["BAMS", "MD in Ayurveda", "PhD in Ayurveda"]

def list_classical_ayurvedic_oils():
    """Return names of ancient therapeutic massage oils."""
    return ["Dhanwantharam Taila", "Ksheerabala Oil", "Brahmi Oil", "Mahanarayana Taila"]

def yoga_for_diabetes():
    """Effective yoga poses for diabetes management."""
    return ["Naukasana", "Dhanurasana", "Matsyendrasana"]

def compare_ayurveda_homeopathy():
    """Basic difference between Ayurveda and Homeopathy systems."""
    return {
        "Ayurveda": "Based on doshas and natural herbs.",
        "Homeopathy": "Based on ‘like cures like’ theory and dilutions."
    }

def yoga_suits_indian_climate():
    """Daily yoga advice for India’s weather conditions."""
    return ["Early morning yoga", "Evening cooling pranayama", "Avoid yoga in peak sun"]

def famous_ayurvedic_drinks():
    """Indian herbal beverages used in traditional medicine."""
    return ["Jeera water", "Tulsi tea", "Amla juice", "Herbal kadha"]

def best_time_for_yoga():
    """Return best time for yoga as per Indian scriptures."""
    return "Brahma Muhurta (4:00 AM – 6:00 AM)"

def list_yogic_hand_mudras():
    """Important hand gestures (mudras) used in yoga & meditation."""
    return ["Gyan Mudra", "Prana Mudra", "Apana Mudra", "Dhyana Mudra"]

def ancient_indian_remedies():
    """Ayurvedic medicine mixes used for generations."""
    return ["Chyawanprash", "Triphala", "Dashamoola", "Sitopaladi churna"]

def yogic_principles_for_life():
    """Spiritual codes of conduct from Patanjali's Yoga Sutras."""
    return ["Ahimsa", "Satya", "Asteya", "Brahmacharya", "Aparigraha"]

def eye_care_with_ayurveda():
    """Natural Indian remedies for eye health."""
    return ["Cold water rinse", "Triphala eyewash", "Netra tarpana"]

def yoga_for_women():
    """Safe and beneficial yoga poses for women in India."""
    return ["Baddha Konasana", "Bhujangasana", "Viparita Karani"]

def monsoon_wellness_tips():
    """Ayurvedic health precautions during India's monsoon."""
    return ["Avoid curd", "Eat light, dry food", "Use neem oil", "Herbal fumigation"]

def ayurveda_in_education_policy():
    """Ayurveda’s importance in Indian education policy."""
    return "Yoga and Ayurveda included in NEP 2020 for holistic well-being."

def top_ayurveda_hospitals():
    """Reputed Ayurvedic hospitals and institutions in India."""
    return ["Kottakkal Arya Vaidya Sala", "Patanjali Yogpeeth", "AVP Coimbatore", "SDM College Udupi"]