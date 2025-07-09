# indian_awards.py

def AwardDetails(awardd):
    awards = {
        "bharatratna": "The highest civilian award of India, given for exceptional service towards the advancement of Art, Literature, Science, and Public Services.",
        "padmavibhushan": "Second-highest civilian award in India, given for exceptional and distinguished service in any field.",
        "padmabhushan": "Third-highest civilian award, awarded for distinguished service of a high order.",
        "padmashri": "Fourth-highest civilian award in India, given for distinguished service in various disciplines.",
        "gallantryawards": "Includes Param Vir Chakra, Ashoka Chakra, Vir Chakra — given for bravery and valor in military service.",
        "paramvirchakra": "India's highest wartime military decoration awarded for showing distinguished acts of valor during war.",
        "ashokachakra": "India's highest peacetime military award for valor, courageous action or self-sacrifice away from the battlefield.",
        "virchakra": "Third-highest wartime military award for acts of gallantry in the presence of the enemy.",
        "mahavirchakra": "Second-highest wartime gallantry award.",
        "kirtichakra": "Second-highest peacetime gallantry award.",
        "senamedal": "Awarded to members of the Indian Army for individual acts of exceptional devotion to duty or courage.",
        "arjunaaward": "Presented by the Ministry of Youth Affairs and Sports to recognize outstanding achievement in national sports.",
        "rajivgandhikhelratna": "Now renamed as **Major Dhyan Chand Khel Ratna Award**, it is India’s highest sporting honor.",
        "dronacharyaaward": "Presented to coaches for producing medal winners at prestigious international sports events.",
        "tenzingnorgeyaward": "Given for outstanding achievement in the field of adventure activities on land, sea and air.",
        "bharatiyajnanpithaward": "India’s highest literary award given for outstanding contribution to literature.",
        "sahityaakademiaward": "Given annually by the Sahitya Akademi for outstanding books of literary merit in 24 Indian languages.",
        "nationalfilmawards": "Presented by the Government of India to honor the best films in Indian cinema every year.",
        "dadasahebphalkeaward": "India’s highest award in cinema for lifetime achievement in Indian film industry.",
        "bharatenduharishchandraaward": "Awarded for outstanding works in Hindi journalism and literature.",
        "kalidassamman": "Given for excellence in classical music, dance, theatre and visual arts.",
        "shantiswarupbhatnagaraward": "Prestigious science award in India given for notable research in various fields of science.",
        "ramanmagaysayaward": "Although international, it's often awarded to Indians for public service and leadership in Asia.",
        "indiragandhipeaceprize": "Awarded for peace, disarmament and development efforts.",
        "lalbahadurshastrinationalaward": "Awarded for excellence in public administration, academics and management.",
        "narishaktipuraskar": "Given annually to women and institutions for exceptional contribution to women empowerment.",
        "nationalbraveryaward": "Given to children for their act of bravery and meritorious service.",
        "balshaktipuraskar": "National award for children showing courage, innovation, and academic excellence.",
        "dr.b.c.royaward": "India's highest medical honor, awarded for excellence in the field of medicine.",
        "jeevanrakshapadak": "Awarded for saving lives in circumstances of grave bodily injury or danger.",
        "civilservicesawards": "Presented for exceptional performance in governance, including the Prime Minister’s Award for Excellence.",
        "sangeetnatakakademiaward": "Given for excellence in music, dance, and drama by the Sangeet Natak Akademi.",
        "lataaward": "Lata Mangeshkar Award is given by various Indian states for excellence in music.",
        "bismillahkhanaward": "Ustad Bismillah Khan Yuva Puraskar for young artists in the field of music, dance, and drama.",
        "vishwakarmayojanaaward": "Awarded for innovative engineering solutions through the Vishwakarma Scheme.",
        "vayoshreshthaaward": "Conferred to senior citizens for distinguished service in various fields.",
        "iccrdistinguishedindianaward": "Given by Indian Council for Cultural Relations for global promotion of Indian culture.",
        "rajivgandhiworldtelecomaward": "Recognizes excellence in telecom sector contributions.",
        "abdusalamaward": "Award for excellence in mathematical sciences given by Indian National Science Academy.",
        "nationalteachersaward": "Awarded annually to teachers for exemplary teaching contributions.",
        "nationalictaward": "Given to teachers for innovation in education using ICT tools.",
        "eklavyaaward": "State-level award for excellence in sports for school students.",
        "bhimaward": "Maharashtra state-level sports award for outstanding sportspersons.",
        "maulanaabulkalamazadaward": "Highest award for sports institutions or universities.",
        "rajivgandhiwomanempowermentaward": "Recognizes efforts towards women's rights and empowerment.",
        "tagoreliteraryaward": "Awarded for outstanding contribution to Indian literature, inspired by Rabindranath Tagore.",
        "dr.apjabdulkalamaward": "Given by state governments or institutions for contributions in science, youth development, and innovation.",
        "indianachieversaward": "Award for individuals contributing in business, entrepreneurship, or leadership.",
        "indianofyearaward": "Awarded by media houses like CNN-IBN to individuals excelling in various fields.",
        "championsofchangeaward": "Given for social welfare, community development, and nation-building initiatives.",
        "bharatratnagauravaward": "Honorary recognition given by private or non-government institutions for distinguished achievements."
    }

    key = awardd.replace(" ", "").lower()
    
    if key in awards:
        print(f"{awardd.title()}:\n{awards[key]}")
    else:
        print("Invalid Award Name. Please check your spelling or spacing.")

# Example usage
#AwardDetails("bharat ratna")