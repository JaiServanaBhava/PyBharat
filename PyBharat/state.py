# states.py
def StateCapital(statename):
    states = {
        "andhrapradesh": "Amaravati",
        "arunachalpradesh": "Itanagar",
        "assam": "Dispur",
        "bihar": "Patna",
        "chhattisgarh": "Raipur",
        "goa": "Panaji",
        "gujarat": "Gandhinagar",
        "haryana": "Chandigarh",
        "himachal pradesh": "Shimla",
        "jharkhand": "Ranchi",
        "karnataka": "Bengaluru",
        "kerala": "Thiruvananthapuram",
        "madhya pradesh": "Bhopal",
        "maharashtra": "Mumbai",
        "manipur": "Imphal",
        "meghalaya": "Shillong",
        "mizoram": "Aizawl",
        "nagaland": "Kohima",
        "odisha": "Bhubaneswar",
        "punjab": "Chandigarh",
        "rajasthan": "Jaipur",
        "sikkim": "Gangtok",
        "tamil nadu": "Chennai",
        "telangana": "Hyderabad",
        "tripura": "Agartala",
        "uttarpradesh": "Lucknow",
        "uttarakhand": "Dehradun",
        "westbengal": "Kolkata"
    }

    key =statename.replace(" ", "").lower()
   
    if key in states:
        print(f"The capital of {statename.title()} is {states[key]}.")
    else:
        print("Invalid state name. Please enter a valid Indian state.")
        
        
def CapitalState(capitalname):
    capitals = {
        "amaravati": "Andhra Pradesh",
        "itanagar": "Arunachal Pradesh",
        "dispur": "Assam",
        "patna": "Bihar",
        "raipur": "Chhattisgarh",
        "panaji": "Goa",
        "gandhinagar": "Gujarat",
        "chandigarh": "Haryana / Punjab",
        "shimla": "Himachal Pradesh",
        "ranchi": "Jharkhand",
        "bengaluru": "Karnataka",
        "thiruvananthapuram": "Kerala",
        "bhopal": "Madhya Pradesh",
        "mumbai": "Maharashtra",
        "imphal": "Manipur",
        "shillong": "Meghalaya",
        "aizawl": "Mizoram",
        "kohima": "Nagaland",
        "bhubaneswar": "Odisha",
        "jaipur": "Rajasthan",
        "gangtok": "Sikkim",
        "chennai": "Tamil Nadu",
        "hyderabad": "Telangana",
        "agartala": "Tripura",
        "lucknow": "Uttar Pradesh",
        "dehradun": "Uttarakhand",
        "kolkata": "West Bengal"
    }

    key = capitalname.replace(" ", "").lower()
    
    if key in capitals:
        print(f"The state with capital {capitalname.title()} is {capitals[key]}.")
    else:
        print("Invalid capital name. Please enter a valid Indian state capital.")
        
def is_UnionTerritory(name):
    union_territories = {
        "andaman and nicobar islands",
        "chandigarh",
        "dadra and nagar haveli and daman and diu",
        "delhi",
        "jammu and kashmir",
        "ladakh",
        "lakshadweep",
        "puducherry"
    }
    
    names = name.replace(" ","").lower()
    
    if names in union_territories:
        print(f"{name.title()} is a Union Territory of India.")
    else:
        print(f"{name.title()} is NOT a Union Territory of India.") 
def StateCount():
    print("28")
def UnionTerritoyCount():
    print("7")
"""is_UnionTerritory("Ladakh")
is_UnionTerritory("lucknow")
StateCapital("andhra pradesh")
StateCapital("amaravati")
CapitalState("andhra pradesh")
CapitalState("patna")"""
