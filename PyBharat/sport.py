def national_sport():
    return "Hockey is considered the national sport of India due to its historical success in Olympics."

def cricket_popularity():
    return "Cricket is the most popular sport in India, followed like a religion by millions."

def indian_olympic_medals():
    return {
        "Gold": ["Neeraj Chopra (Javelin Throw)", "Abhinav Bindra (Shooting)"],
        "Silver": ["Ravi Kumar Dahiya (Wrestling)", "Mirabai Chanu (Weightlifting)"],
        "Bronze": ["PV Sindhu", "Mary Kom", "Lovlina Borgohain"]
    }

def famous_cricketers():
    return ["Sachin Tendulkar", "Virat Kohli", "M.S. Dhoni", "Rohit Sharma", "Kapil Dev"]

def women_in_sports_india():
    return [
        "Saina Nehwal (Badminton)", "Mary Kom (Boxing)", "Dutee Chand (Athletics)", 
        "Mithali Raj (Cricket)", "Sakshi Malik (Wrestling)"
    ]

def kabaddi_success():
    return "India has won multiple World Cups in Kabaddi and dominates the Pro Kabaddi League."

def indian_sports_awards():
    return {
        "Rajiv Gandhi Khel Ratna": "Highest sporting honour",
        "Arjuna Award": "Performance-based excellence",
        "Dronacharya Award": "For outstanding coaches"
    }

def chess_grandmasters():
    return ["Viswanathan Anand", "R Praggnanandhaa", "D Gukesh", "Vidit Gujrathi", "Pentala Harikrishna"]

def traditional_indian_games():
    return ["Kho Kho", "Gilli Danda", "Mallakhamb", "Kabaddi", "Lagori (Seven stones)"]

def hockey_olympic_legacy():
    return "India has won 8 Olympic gold medals in hockey, the highest by any nation historically."

def athletics_medalists():
    return ["Neeraj Chopra", "Milkha Singh", "PT Usha", "Anju Bobby George", "Hima Das"]

def paralympic_champions():
    return [
        "Avani Lekhara (Shooting)", "Devendra Jhajharia (Javelin Throw)", "Mariyappan Thangavelu (High Jump)"
    ]

def popular_sports_states():
    return {
        "Punjab": "Wrestling, Hockey",
        "Kerala": "Athletics, Football",
        "Haryana": "Wrestling, Boxing",
        "Maharashtra": "Cricket, Chess",
        "Manipur": "Weightlifting, Martial Arts"
    }

def badminton_champions():
    return ["Saina Nehwal", "PV Sindhu", "Kidambi Srikanth", "Lakshya Sen", "Chirag Shetty"]

def tennis_legends():
    return ["Leander Paes", "Sania Mirza", "Mahesh Bhupathi", "Rohan Bopanna"]

def indian_super_league():
    return "ISL is India’s professional football league launched in 2013 to revive Indian football."

def wrestling_medalists():
    return ["Sushil Kumar", "Bajrang Punia", "Yogeshwar Dutt", "Sakshi Malik"]

def cricket_world_cup_wins():
    return {
        "1983": "Won under Kapil Dev",
        "2007": "T20 World Cup under MS Dhoni",
        "2011": "ODI World Cup under MS Dhoni"
    }

def indian_sport_inventions():
    return ["Chess (Chaturanga)", "Yoga Asana Games", "Mallakhamb", "Kabaddi"]

def famous_stadiums():
    return [
        "Eden Gardens (Kolkata)", "Wankhede Stadium (Mumbai)", "Jawaharlal Nehru Stadium (Delhi)",
        "M. A. Chidambaram (Chennai)", "Narendra Modi Stadium (Ahmedabad)"
    ]

def motorsports_in_india():
    return "India has hosted F1 races and supports MotoGP, Karting, and Rally events like INRC."

def sports_training_centers():
    return [
        "NIS Patiala", "Gopichand Badminton Academy", "SAI (Sports Authority of India)", "TOPS Scheme Camps"
    ]

def esports_and_gaming():
    return "Esports is booming in India with tournaments in games like BGMI, Free Fire, and Valorant."

def indigenous_martial_arts():
    return ["Kalaripayattu (Kerala)", "Silambam (Tamil Nadu)", "Thang-Ta (Manipur)", "Mardani Khel (Maharashtra)"]

def youth_olympics_performance():
    return "India won medals in shooting, judo, boxing and athletics in recent Youth Olympics."

def gully_cricket():
    return "Every street and colony in India plays informal cricket, a part of growing up."

def fit_india_movement():
    return "Launched by PM Modi in 2019 to encourage fitness culture in schools and colleges."

def olympic_council_of_india():
    return "The IOA governs Olympic sports in India and manages participation in international games."

def traditional_rural_sports():
    return ["Bullock Cart Racing", "Wrestling Akhadas", "Vallam Kali (Boat Race)", "Camel Race", "Tug of War"]

def winter_sports_india():
    return "Jammu & Kashmir, Himachal, and Uttarakhand host winter sports like skiing and ice hockey."

def female_cricket_team():
    return {
        "Captain": "Harmanpreet Kaur",
        "Top Players": ["Smriti Mandhana", "Shafali Verma", "Jemimah Rodrigues"],
        "Achievement": "Finalists of 2020 ICC T20 World Cup"
    }

def adventure_sports_india():
    return ["Paragliding (Bir Billing)", "Rafting (Rishikesh)", "Skiing (Gulmarg)", "Trekking (Himalayas)"]

def sports_in_schools():
    return "Khelo India, Fit India, and CBSE sports meet promote regular athletic competitions in schools."

def indian_flag_bearers_olympics():
    return ["Abhinav Bindra", "Mary Kom", "PV Sindhu", "Neeraj Chopra"]

def startup_in_sports_tech():
    return [
        "Dream11 (Fantasy League)", "Sportskeeda (News)", "Fittr (Fitness)", "MPL (Gaming)"
    ]

def describe_sport(sportname):
    data = {
        "cricket": "India's most popular game with IPL as a billion-dollar tournament.",
        "hockey": "India's national sport with an Olympic legacy.",
        "kabaddi": "Traditional contact sport now modernized with Pro Kabaddi League.",
        "badminton": "India excels with global wins by PV Sindhu and Saina Nehwal.",
        "chess": "India has over 80 grandmasters, pioneered by Viswanathan Anand."
    }
    return data.get(sportname.lower(), "Sport not found in Indian context.")