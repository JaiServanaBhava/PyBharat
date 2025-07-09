def list_common_superstitions():
    return [
        "Black cat crossing your path is bad luck.",
        "Lemon and chilies hung outside shops ward off evil spirits.",
        "Cutting nails or hair on certain days brings misfortune.",
        "Twitching of the right eye means something good will happen (for men); left eye for women.",
        "Breaking a mirror leads to seven years of bad luck.",
        "Sneezing before starting work is a bad omen.",
        "Spilling milk is inauspicious.",
        "Jumping over someone makes them short.",
        "Hiccups mean someone is thinking of you.",
        "Wearing iron rings or black threads wards off evil eye.",
        "Shaking legs causes loss of wealth.",
        "Keeping owl feathers brings knowledge or Lakshmi's blessings.",
        "Sweeping the house after sunset drives away prosperity.",
        "Crow cawing outside the house means guests will arrive.",
        "Itching on palm means money is coming.",
        "Eclipses are inauspicious; avoid food, water, or outdoor activity.",
        "Lizard falling on body parts brings different types of luck.",
        "Left eye blinking for women means good luck, but bad for men.",
        "Number 13 is unlucky.",
        "Dogs howling at night signals bad omen."
    ]

def region_specific_superstitions():
    return {
        "Tamil Nadu": "Don’t go out after seeing a broom standing vertically.",
        "Maharashtra": "Avoid looking into mirror at night.",
        "Bengal": "Use of red chillies in rituals to cast away bad energy.",
        "Kerala": "Snakes are sacred; harming them brings misfortune.",
        "Rajasthan": "Turmeric-tied thread worn to avoid nazar (evil eye)."
    }

def good_omen_examples():
    return [
        "Seeing an elephant in the morning is lucky.",
        "Hearing a temple bell as you leave for work.",
        "First sneeze in the morning is good luck.",
        "Seeing a bride or groom on the way is auspicious.",
        "Spotting a peacock is considered lucky."
    ]

def scientific_explanations():
    return {
        "Black Cat Myth": "Imported from Western beliefs; no real danger.",
        "Lemon and Chilies": "Used in Ayurveda as a natural pest deterrent.",
        "Itching Palm": "May be due to dryness or allergy, not money.",
        "Mirror Breaking": "Superstition originated due to mirror rarity in old days.",
        "Lunar Eclipse": "Caused by Earth's shadow, not evil; safe to go out."
    }

def psychological_effects():
    return """Superstitions often arise from cultural conditioning, fear, or coincidence.
They may provide psychological comfort or ritual routine, but relying on them excessively 
can lead to anxiety and avoidable fear."""

def classify_superstition(type_):
    if type_.lower() == "bad":
        return [s for s in list_common_superstitions() if "bad" in s or "evil" in s or "misfortune" in s]
    elif type_.lower() == "good":
        return good_omen_examples()
    else:
        return "Type not recognized. Use 'good' or 'bad'."

def quiz_question():
    return {
        "question": "What is considered a bad omen in India while starting a journey?",
        "options": ["Seeing a snake", "Sneezing", "Seeing a bride", "Eating curd"],
        "answer": "Sneezing"
    }

def awareness_message():
    return """🧠 Superstitions are part of cultural folklore, but modern science helps us understand
the real reasons behind many events. It is good to preserve traditions, but also to stay aware and rational."""

def teach_kids():
    return """Start by asking them to observe which beliefs have logic and which are just followed blindly.
Use real-life examples and scientific reasoning to balance tradition with curiosity and learning."""

def is_superstition(belief):
    known = [b.lower() for b in list_common_superstitions()]
    return any(belief.lower() in b for b in known)