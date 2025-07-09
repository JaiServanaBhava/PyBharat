# education_exams.py

def list_national_level_exams():
    """Return a list of top national-level competitive exams in India."""
    return [
        "JEE Main",
        "JEE Advanced",
        "NEET",
        "UPSC Civil Services",
        "NDA",
        "CLAT",
        "CAT",
        "CUET",
        "GATE",
        "UGC NET"
    ]

def jee_main_info():
    """Details about JEE Main exam."""
    return (
        "JEE Main is the national-level entrance exam for engineering aspirants conducted by NTA. "
        "It provides admission into NITs, IIITs, and acts as the eligibility test for JEE Advanced."
    )

def jee_advanced_info():
    """Details about JEE Advanced."""
    return (
        "JEE Advanced is for admission into the Indian Institutes of Technology (IITs). "
        "Only top 2.5 lakh rankers of JEE Main are eligible to appear."
    )

def neet_exam_info():
    """Details about NEET exam."""
    return (
        "NEET (National Eligibility cum Entrance Test) is the single entrance exam for MBBS, BDS, and AYUSH courses across India. "
        "Conducted by NTA, it covers Physics, Chemistry, and Biology."
    )

def upsc_info():
    """Overview of the UPSC Civil Services Exam."""
    return (
        "UPSC CSE is the toughest exam in India to recruit IAS, IPS, IFS, and IRS officers. "
        "It has 3 stages: Preliminary, Mains, and Personality Test (Interview)."
    )

def board_exam_classes():
    """Return classes where board exams are conducted in India."""
    return ["Class 10 (Secondary)", "Class 12 (Senior Secondary)"]

def state_education_boards():
    """List top state boards in India."""
    return [
        "Maharashtra State Board (MSBSHSE)",
        "UP Board (UPMSP)",
        "Bihar Board (BSEB)",
        "Tamil Nadu Board (TNBSE)",
        "West Bengal Board (WBBSE)"
    ]

def cbse_board_info():
    """Information about CBSE board."""
    return (
        "CBSE (Central Board of Secondary Education) is a national board under the Indian government. "
        "It follows NCERT curriculum and conducts Class 10 & 12 exams."
    )

def icse_board_info():
    """Information about ICSE board."""
    return (
        "ICSE (Indian Certificate of Secondary Education) is a private national-level board focusing on strong English and conceptual clarity."
    )

def cuet_exam_info():
    """About CUET exam for central universities."""
    return (
        "CUET (Common University Entrance Test) is a centralised exam for admissions into central universities. "
        "Covers sections like language, domain subjects, and general knowledge."
    )

def list_open_schools():
    """List major open schooling systems in India."""
    return [
        "NIOS (National Institute of Open Schooling)",
        "BOSSE (Board of Open Schooling and Skill Education)",
        "State Open Schools"
    ]

def scholarship_exams():
    """List top national-level scholarship exams."""
    return [
        "NTSE (National Talent Search Examination)",
        "KVPY (Kishore Vaigyanik Protsahan Yojana)",
        "INSPIRE Scholarship",
        "PMSSS (for J&K students)",
        "SOF Olympiads"
    ]

def olympiad_exams_india():
    """Return Olympiad exams conducted for school students."""
    return [
        "Science Olympiad Foundation (SOF)",
        "NSTSE",
        "SilverZone",
        "Unified Council Olympiads"
    ]

def kvs_admission_criteria():
    """Criteria for admission to Kendriya Vidyalayas."""
    return {
        "Age": "Minimum 5 years for Class 1",
        "Priority": "Government employees’ children get first preference",
        "Reservation": "SC/ST/OBC/EWS quotas applicable"
    }

def ncert_books_list(class_number):
    """Return a list of subjects taught in NCERT books for a given class."""
    subjects = {
        6: ["Maths", "Science", "English", "Sanskrit", "History", "Geography", "Civics"],
        10: ["Maths", "Science", "English", "Social Science", "Hindi"],
        12: ["Physics", "Chemistry", "Biology", "Accountancy", "Political Science", "Economics"]
    }
    return subjects.get(class_number, [])

def check_exam_eligibility(exam_name, age):
    """Check eligibility for a given exam based on age."""
    exam_name = exam_name.lower()
    if exam_name == "jee" and 16 <= age <= 25:
        return "Eligible for JEE Main."
    elif exam_name == "neet" and 17 <= age <= 25:
        return "Eligible for NEET."
    elif exam_name == "upsc" and 21 <= age <= 32:
        return "Eligible for UPSC."
    else:
        return "Eligibility unclear or not met."

def ugc_net_info():
    """Overview of UGC NET exam."""
    return (
        "UGC NET is a national exam for determining eligibility for Assistant Professors and JRF in Indian universities. "
        "Conducted by NTA in subjects like English, Commerce, Sociology, etc."
    )

def education_ministry_schemes():
    """Government schemes related to education in India."""
    return [
        "Samagra Shiksha Abhiyan",
        "Mid Day Meal Scheme",
        "Beti Bachao Beti Padhao",
        "Digital India e-Learning",
        "PM eVIDYA"
    ]

def skill_india_programs():
    """List of Indian vocational and skill education programs."""
    return [
        "PMKVY – Pradhan Mantri Kaushal Vikas Yojana",
        "Skill India Digital",
        "eSkill India",
        "DDU-GKY (for rural youth)"
    ]

def navodaya_exam_info():
    """About JNVST (Navodaya) entrance exam for Class 6 & 9."""
    return (
        "Jawahar Navodaya Vidyalaya Selection Test (JNVST) is for rural students to gain free admission to Navodaya schools. "
        "Covers reasoning, maths, and language skills."
    )

def nta_role_in_exams():
    """Role of NTA (National Testing Agency)."""
    return (
        "NTA is responsible for conducting major exams like JEE, NEET, CUET, UGC NET, etc. "
        "It ensures transparency, fairness, and standardisation."
    )

def best_online_learning_platforms():
    """List top Indian online learning platforms."""
    return ["BYJU’S", "Unacademy", "Vedantu", "Toppr", "PW (Physics Wallah)", "SWAYAM"]

def iit_institutes_list():
    """Return list of top IITs in India."""
    return [
        "IIT Bombay",
        "IIT Delhi",
        "IIT Kanpur",
        "IIT Madras",
        "IIT Kharagpur",
        "IIT Roorkee"
    ]

def list_iims():
    """List top IIMs for management studies."""
    return ["IIM Ahmedabad", "IIM Bangalore", "IIM Calcutta", "IIM Lucknow", "IIM Kozhikode"]

def ssc_exam_categories():
    """Various exams under SSC (Staff Selection Commission)."""
    return [
        "SSC CGL",
        "SSC CHSL",
        "SSC MTS",
        "SSC GD Constable",
        "SSC JE"
    ]

def railway_exams_info():
    """Return list of railway recruitment exams."""
    return [
        "RRB NTPC",
        "RRB ALP",
        "RRB Group D",
        "RRB JE"
    ]

def defence_exams():
    """List Indian defence-related exams."""
    return ["NDA", "CDS", "AFCAT", "SSB Interview", "Territorial Army Exam"]

def itis_and_polytechnics():
    """Vocational and technical training after class 10/12."""
    return {
        "ITI": "Industrial Training Institutes for trades like Electrician, Welder, Mechanic",
        "Polytechnic": "3-year diploma in engineering or applied sciences"
    }

def adult_education_missions():
    """Govt. initiatives for adult literacy and continuing education."""
    return [
        "Saakshar Bharat Mission",
        "New India Literacy Program (2022 onwards)",
        "ePathshala App"
    ]

def describe_module():
    """Full description of the education_exams module."""
    return (
        "This module focuses on Indian school boards, competitive exams, scholarships, national learning platforms, "
        "government schemes, career entrance tests, and online education. It helps learners explore India’s diverse academic ecosystem."
    )