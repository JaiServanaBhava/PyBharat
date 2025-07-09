def emergency_contacts():
    return {
        "Police": "100",
        "Fire Brigade": "101",
        "Ambulance": "102",
        "Disaster Management Services": "108",
        "National Emergency Number": "112",
        "Women Helpline": "1091",
        "Child Helpline": "1098",
        "Senior Citizen Helpline": "14567",
        "Cyber Crime Helpline": "1930",
        "Railway Enquiry": "139",
        "Road Accident Emergency": "1073",
        "Air Ambulance": "9540161344",  # Example private service
        "Anti-Terror Helpline": "1090",
        "National AIDS Helpline": "1097",
        "Mental Health Helpline (KIRAN)": "1800-599-0019",
        "Blood Requirement": "104",
        "Poison Control": "1066",
        "Traffic Helpline (city-specific)": "103",  # May vary
        "Electricity Complaint": "1912",
        "Gas Leakage": "1906",
        "Women Safety WhatsApp": "+91-7617-003322",
        "Central Vigilance Commission": "1964",
        "Consumer Helpline": "1800-11-4000",
        "Election Commission Helpline": "1950"
    }

def get_helpline(service_name):
    services = list_emergency_contacts()
    key = service_name.strip().lower()
    
    for name, number in services.items():
        if key in name.lower():
            return f"{name}: {number}"
    return "⚠️ No matching emergency service found."

# Optional function to print all in neat format
def all_emergency_contacts():
    services = list_emergency_contacts()
    for service, number in services.items():
        print(f"{service}: {number}")