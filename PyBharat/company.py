def list_top_indian_companies():
    return ["Tata Group", "Reliance Industries", "Infosys", "Wipro", "Adani Group", "Mahindra", "HCL", "ITC", "L&T", "Bajaj", "HDFC", "LIC", "BSNL"]

def list_fmcg_companies():
    return ["Hindustan Unilever", "Dabur", "ITC", "Patanjali", "Godrej Consumer", "Britannia", "Parle", "Amul"]

def list_tech_it_companies():
    return ["TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra", "Mindtree", "L&T Infotech", "Zoho"]

def list_banking_finance_companies():
    return ["SBI", "ICICI", "HDFC Bank", "Kotak Mahindra", "Axis Bank", "Yes Bank", "Bajaj Finserv", "LIC", "PNB", "IDFC First"]

def list_automobile_companies():
    return ["Tata Motors", "Mahindra & Mahindra", "Ashok Leyland", "TVS Motors", "Bajaj Auto", "Hero MotoCorp", "Eicher Motors", "Force Motors"]

def list_airlines_india():
    return ["Air India", "IndiGo", "SpiceJet", "Vistara", "Akasa Air", "Go First", "Alliance Air"]

def describe_company(name):
    name = name.lower()
    data = {
        "tata": "Tata Group is one of India's oldest and largest conglomerates with companies in steel, IT, automotive, and more.",
        "reliance": "Reliance Industries is a major conglomerate with interests in energy, petrochemicals, retail, and telecom (Jio).",
        "infosys": "Infosys is a global leader in IT consulting and software services based in Bengaluru.",
        "wipro": "Wipro provides IT, consulting, and business process services globally.",
        "mahindra": "Mahindra is a major Indian automobile manufacturer and leader in tractors and utility vehicles.",
        "hdfc": "HDFC is a financial giant involved in banking, loans, and housing finance.",
        "itc": "ITC is a diversified company in FMCG, hotels, paper, packaging, and agri-business.",
        "amul": "Amul is India's largest dairy brand known for milk, butter, and cheese products.",
    }
    return data.get(name, "Description not found.")

def list_indian_startups():
    return ["Byju's", "Ola", "Zomato", "Swiggy", "Razorpay", "Paytm", "CRED", "Nykaa", "PhonePe", "Dream11", "Meesho", "Groww"]

def unicorn_startups():
    return ["Razorpay", "CRED", "PhysicsWallah", "Zerodha", "Ola", "Swiggy", "Meesho", "ShareChat", "Delhivery"]

def list_defense_manufacturers():
    return ["HAL", "Bharat Dynamics Ltd", "BEL", "DRDO", "Mazagon Dock", "Bharat Electronics"]

def telecom_companies():
    return ["Jio", "Airtel", "BSNL", "Vodafone-Idea"]

def oil_energy_companies():
    return ["ONGC", "IOCL", "BPCL", "HPCL", "Reliance", "Adani Green", "NTPC", "GAIL"]

def pharma_companies():
    return ["Sun Pharma", "Dr. Reddy’s", "Cipla", "Lupin", "Biocon", "Zydus Cadila", "Glenmark"]

def ecommerce_companies():
    return ["Flipkart", "Myntra", "Snapdeal", "Nykaa", "BigBasket", "Meesho", "IndiaMART"]

def edtech_companies():
    return ["Byju’s", "Vedantu", "Unacademy", "PhysicsWallah", "Toppr", "Adda247", "Testbook"]

def indian_govt_psus():
    return ["BSNL", "ONGC", "NTPC", "SAIL", "BHEL", "GAIL", "HAL", "BEL", "Coal India", "IOCL"]

def food_and_beverages_brands():
    return ["Amul", "Parle", "Britannia", "Dabur", "Patanjali", "MDH", "Mother Dairy", "Nestlé India"]

def aviation_manufacturers():
    return ["HAL", "Tata Aerospace", "DRDO", "Mahindra Aerospace"]

def most_trusted_indian_brands():
    return ["Tata", "LIC", "Amul", "HDFC", "BSNL", "Bajaj", "Infosys"]

def textile_companies():
    return ["Raymond", "Arvind Ltd", "Vardhman", "Trident", "Bombay Dyeing", "Grasim", "Welspun"]

def steel_manufacturers():
    return ["Tata Steel", "JSW Steel", "SAIL", "Essar Steel", "Jindal Steel"]

def cement_companies():
    return ["UltraTech", "ACC", "Ambuja Cement", "Shree Cement", "Dalmia Bharat", "JK Cement"]

def list_beauty_cosmetics():
    return ["Lakme", "Nykaa", "Lotus Herbals", "Biotique", "VLCC", "Patanjali", "Forest Essentials"]

def describe_startup(name):
    name = name.lower()
    data = {
        "byju's": "Byju’s is India’s leading edtech platform offering video-based learning programs.",
        "ola": "Ola is a cab aggregator and electric vehicle company based in Bengaluru.",
        "swiggy": "Swiggy is a leading food delivery startup operational across Indian cities.",
        "paytm": "Paytm is a digital payment and financial services company offering wallets, UPI, and more.",
        "razorpay": "Razorpay is a fintech startup providing payment gateway and business banking solutions.",
    }
    return data.get(name, "Startup description not found.")

def sports_equipment_brands():
    return ["SG", "MRF", "SS", "Cosco", "Nivia", "Vector X"]

def electronics_companies():
    return ["Micromax", "Lava", "Karbonn", "Boat", "Noise", "Zebronics"]

def mobile_manufacturers():
    return ["Micromax", "Lava", "Karbonn", "Reliance LYF", "JioPhone"]

def export_based_companies():
    return ["Tata Consultancy Services", "Infosys", "Wipro", "Sun Pharma", "Bharat Forge", "Reliance"]

def healthcare_companies():
    return ["Apollo Hospitals", "Fortis", "AIIMS", "Max Healthcare", "Medanta", "Manipal"]

def top_employers():
    return ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini India", "Accenture India"]

def companies_in_stock_market():
    return ["Tata Steel", "Reliance", "Infosys", "HDFC Bank", "ICICI", "L&T", "Bajaj Finance", "ITC", "ONGC", "NTPC"]

def indigenously_innovated():
    return ["Bharat Biotech", "Amul", "DRDO", "ISRO", "Razorpay", "Zerodha", "Tata"]

def sustainable_companies():
    return ["Adani Green", "Tata Power", "ReNew Power", "Suzlon Energy", "NTPC Green"]

def biggest_employment_creators():
    return ["Indian Railways", "TCS", "Infosys", "Reliance", "BHEL", "L&T"]

def smart_city_contributors():
    return ["L&T", "Tata Projects", "Wipro Infrastructure", "BEL", "Bharat Electronics"]

def ai_focused_companies():
    return ["Haptik", "Arya.ai", "Yellow.ai", "Niki.ai", "TCS", "Infosys", "Wipro"]

def list_indian_brands_global_presence():
    return ["Tata Motors (Jaguar-Land Rover)", "Infosys", "Wipro", "Zerodha", "Ola Electric", "Mahindra"]

def ethical_indian_brands():
    return ["Amul", "Tata", "LIC", "ISRO", "Patanjali", "Narayana Hrudayalaya"]

def india_on_forbes():
    return ["Reliance Industries", "Tata Group", "Infosys", "HDFC Bank", "ICICI", "SBI", "Wipro"]

def top_startup_incubators():
    return ["T-Hub", "CIIE at IIM Ahmedabad", "NSRCEL", "Startup India", "NASSCOM 10K", "STPI"]

def company_headquarters(name):
    hq = {
        "tata": "Mumbai",
        "infosys": "Bengaluru",
        "wipro": "Bengaluru",
        "reliance": "Mumbai",
        "mahindra": "Mumbai",
        "hdfc": "Mumbai",
        "zoho": "Chennai",
        "paytm": "Noida",
        "byju's": "Bengaluru"
    }
    return hq.get(name.lower(), "Headquarters info not available.")

def industries_in_india():
    return ["Agriculture", "Automobile", "IT", "Pharma", "FMCG", "Finance", "Oil & Gas", "Steel", "E-commerce", "Aerospace"]