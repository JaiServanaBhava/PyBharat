def top_ecommerce_platforms():
    return [
        "Amazon India",
        "Flipkart",
        "Myntra",
        "Ajio",
        "Tata CLiQ",
        "Snapdeal",
        "Nykaa",
        "Meesho",
        "JioMart",
        "BigBasket",
        "1mg",
        "Pepperfry",
        "Croma",
        "Shopclues",
        "Lenskart"
    ]

def digital_payment_methods():
    return [
        "UPI (Google Pay, PhonePe, Paytm, BHIM)",
        "Net Banking",
        "Credit/Debit Cards",
        "Cash on Delivery (COD)",
        "Wallets (Paytm, Mobikwik)",
        "EMI & Pay Later Services"
    ]

def ecommerce_government_initiatives():
    return {
        "ONDC": "Open Network for Digital Commerce – democratizing e-commerce.",
        "Digital India": "Boosting online infrastructure and internet access.",
        "Make in India": "Encouraging local sellers on e-commerce platforms.",
        "Startup India": "Supporting e-commerce startups and tech innovation."
    }

def logistics_and_delivery_services():
    return [
        "Delhivery",
        "Ecom Express",
        "Blue Dart",
        "India Post",
        "XpressBees",
        "Shadowfax",
        "Ekart (Flipkart)",
        "Amazon Transport"
    ]

def ecommerce_categories():
    return [
        "Electronics",
        "Fashion",
        "Grocery",
        "Healthcare",
        "Home & Kitchen",
        "Books & Stationery",
        "Furniture",
        "Automobile Accessories",
        "Toys & Baby Products"
    ]

def ecommerce_laws_and_policies():
    return {
        "IT Rules 2021": "Regulates digital intermediaries and grievance redressal.",
        "Consumer Protection (E-commerce) Rules": "Ensures fair practices for buyers.",
        "GST Compliance": "Mandatory for e-commerce sellers.",
        "Data Privacy & Security Guidelines": "Protects user data on online platforms."
    }

def top_indian_startups_in_ecommerce():
    return [
        "Meesho", "Udaan", "Fynd", "Licious", "Zivame",
        "Mamaearth", "BoAt", "CarDekho", "FirstCry", "Zomato (for food)"
    ]

def ecommerce_retail_types():
    return {
        "B2C": "Business to Consumer (e.g., Flipkart, Amazon)",
        "B2B": "Business to Business (e.g., Udaan)",
        "C2C": "Consumer to Consumer (e.g., OLX, Facebook Marketplace)",
        "D2C": "Direct to Consumer (e.g., boAt, Mamaearth)"
    }

def ecommerce_festive_sales():
    return [
        "Flipkart Big Billion Days",
        "Amazon Great Indian Festival",
        "Myntra End of Reason Sale",
        "Nykaa Pink Friday Sale",
        "JioMart Festival Dhamaka"
    ]

def ecommerce_fraud_awareness():
    return [
        "Avoid fake websites with misspelled URLs.",
        "Use trusted payment gateways.",
        "Do not share OTP or bank info over call.",
        "Check reviews and seller ratings.",
        "Report frauds to cybercrime.gov.in"
    ]

def customer_rights():
    return {
        "Right to Return": "Most platforms offer 7–15 days return policy.",
        "Right to Refund": "Refund is processed once returned item is received.",
        "Right to Information": "Product description, price, and tax must be shown.",
        "Right to Complain": "Via help desk or grievance officer under IT Rules."
    }

def india_ecommerce_stats():
    return {
        "Internet users (2025 est.)": "900+ million",
        "E-commerce market size (2025)": "$120+ billion",
        "Top tier cities": "Delhi, Mumbai, Bangalore, Hyderabad, Chennai",
        "Rural growth": "Tier 2–3 cities and villages rapidly adopting e-commerce"
    }

def suggest_platform_by_category(category):
    suggestions = {
        "fashion": ["Myntra", "Ajio", "Tata CLiQ"],
        "electronics": ["Amazon", "Flipkart", "Croma"],
        "groceries": ["JioMart", "BigBasket", "Blinkit"],
        "beauty": ["Nykaa", "Purplle"],
        "furniture": ["Pepperfry", "Urban Ladder"],
        "health": ["1mg", "PharmEasy"],
        "books": ["Amazon", "Flipkart"]
    }
    return suggestions.get(category.lower(), "No specific platform found for this category.")

def ecommerce_summary():
    return """India's e-commerce sector is booming due to smartphone penetration, 
affordable internet, UPI adoption, and startup innovation. From groceries to gadgets, 
millions of Indians buy and sell online every day. ONDC and Digital India are driving 
a truly open, inclusive, and Atmanirbhar digital shopping ecosystem."""