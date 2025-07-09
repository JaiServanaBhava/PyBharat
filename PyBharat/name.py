import random

# Hindu Names
def hindu_male_names():
    return ["Arjun", "Vikram", "Raghav", "Suresh", "Manoj"]

def hindu_female_names():
    return ["Sita", "Lakshmi", "Anjali", "Radha", "Meera"]

# Muslim Names
def muslim_male_names():
    return ["Ayaan", "Imran", "Zaid", "Ahmed", "Faisal"]

def muslim_female_names():
    return ["Aisha", "Zara", "Fatima", "Nida", "Hina"]

# Christian Names
def christian_male_names():
    return ["John", "Michael", "Joseph", "Daniel", "Paul"]

def christian_female_names():
    return ["Mary", "Grace", "Lily", "Sarah", "Rebecca"]

# Sikh Names
def sikh_male_names():
    return ["Harpreet", "Gurmeet", "Rajinder", "Baljeet", "Jaspreet"]

def sikh_female_names():
    return ["Harleen", "Navjot", "Kiran", "Gurleen", "Simran"]

# Jain Names
def jain_male_names():
    return ["Sumer", "Namit", "Bhavin", "Manan", "Parshav"]

def jain_female_names():
    return ["Pavitra", "Suhani", "Kavya", "Ritika", "Shravani"]

# Buddhist Names
def buddhist_male_names():
    return ["Rahul", "Ananda", "Devdatta", "Subhuti", "Nanda"]

def buddhist_female_names():
    return ["Sujata", "Tara", "Mayadevi", "Khema", "Anopama"]

# Mythological & Epic Names
def mythological_names():
    return ["Ram", "Krishna", "Shiva", "Durga", "Hanuman"]

def epic_names_from_mahabharata():
    return ["Bhima", "Yudhishthira", "Karna", "Draupadi", "Abhimanyu"]

def epic_names_from_ramayana():
    return ["Lakshman", "Bharat", "Sita", "Ravana", "Vibhishan"]

# Common Indian Surnames
def common_indian_surnames():
    return ["Sharma", "Khan", "Das", "Patel", "Singh", "Varma", "Reddy"]

# Regional Names
def tamil_names():
    return ["Arul", "Senthil", "Karthik", "Jeya", "Dhanush"]

def telugu_names():
    return ["Naveen", "Charan", "Raju", "Bhavana", "Sravani"]

def bengali_names():
    return ["Subhash", "Anirban", "Sourav", "Rupali", "Moumita"]

def marathi_names():
    return ["Aditya", "Shrikant", "Ajinkya", "Asha", "Vaishnavi"]

def gujarati_names():
    return ["Kirit", "Hiren", "Mehul", "Rina", "Darshana"]

def manipuri_names():
    return ["Ningthou", "Lalit", "Sanajaoba", "Ibemhal", "Thoibi"]


def folk_names():
    return ["Gopal", "Bhola", "Gita", "Lalli", "Munna"]

# Special & Spiritual Names
def vedic_names():
    return ["Agni", "Soma", "Vayu", "Usha", "Aditi"]

def spiritual_names():
    return ["Om", "Yogi", "Guru", "Deva", "Sadhvi"]

# Bonus Features
def random_name():
    names = (
        hindu_male_names() + hindu_female_names() +
        muslim_male_names() + muslim_female_names() +
        christian_male_names() + christian_female_names() +
        sikh_male_names() + sikh_female_names() +
        jain_male_names() + jain_female_names() +
        buddhist_male_names() + buddhist_female_names() +
        tamil_names() + telugu_names() + bengali_names() + marathi_names() +
        gujarati_names() + manipuri_names() + folk_names() +
        vedic_names() + spiritual_names()
    )
    return random.choice(names)
print(random_name())