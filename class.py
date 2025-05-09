class RomanEmperor:
    """Class representing a Roman Emperor with relevant historical information."""
    
    def __init__(self, name, birth, death, reign_start, reign_end, dynasty=None, 
                 notable_achievements=None, cause_of_death=None, predecessor=None, successor=None,
                 wives=None, zodiac=None):
        self.name = name
        self.birth = birth
        self.death = death
        self.reign_start = reign_start
        self.reign_end = reign_end
        self.dynasty = dynasty
        self.notable_achievements = notable_achievements or []
        self.cause_of_death = cause_of_death
        self.predecessor = predecessor
        self.successor = successor
        self.wives = wives or []
        self.zodiac = zodiac
        
    def reign_duration(self):
        """Calculate the duration of the emperor's reign in years."""
        return self.reign_end - self.reign_start
    
    def age_at_death(self):
        """Calculate the emperor's age at death."""
        return self.death - self.birth
    
    def age_at_accession(self):
        """Calculate the emperor's age when they became emperor."""
        return self.reign_start - self.birth
    
    def __str__(self):
        """String representation of the emperor."""
        info = [
            f"Name: {self.name}",
            f"Lived: {self.birth} CE - {self.death} CE (Age: {self.age_at_death()} years)",
            f"Reign: {self.reign_start} CE - {self.reign_end} CE ({self.reign_duration()} years)",
            f"Dynasty: {self.dynasty}" if self.dynasty else "Dynasty: None",
            f"Zodiac Sign: {self.zodiac}" if self.zodiac else "Zodiac Sign: Unknown"
        ]
        
        if self.wives:
            info.append("Wives/Consorts:")
            for wife in self.wives:
                info.append(f"  - {wife}")
        
        if self.notable_achievements:
            info.append("Notable Achievements:")
            for achievement in self.notable_achievements:
                info.append(f"  - {achievement}")
                
        if self.cause_of_death:
            info.append(f"Cause of Death: {self.cause_of_death}")
            
        return "\n".join(info)


class RomanEmpire:
    """Class representing the Roman Empire and its succession of emperors."""
    
    def __init__(self):
        self.emperors = []
        self.dynasties = set()
        
    def add_emperor(self, emperor):
        """Add an emperor to the empire."""
        self.emperors.append(emperor)
        if emperor.dynasty:
            self.dynasties.add(emperor.dynasty)
    
    def get_emperor_by_name(self, name):
        """Find an emperor by name (case-insensitive partial match)."""
        for emperor in self.emperors:
            if name.lower() in emperor.name.lower():
                return emperor
        return None
    
    def get_emperor_by_year(self, year):
        """Find the emperor(s) who ruled during a specific year."""
        ruling_emperors = []
        for emperor in self.emperors:
            if emperor.reign_start <= year <= emperor.reign_end:
                ruling_emperors.append(emperor)
        return ruling_emperors
    
    def get_emperors_by_dynasty(self, dynasty):
        """Get all emperors belonging to a specific dynasty."""
        return [emperor for emperor in self.emperors if emperor.dynasty == dynasty]
    
    def get_emperors_by_period(self, start_year, end_year):
        """Get all emperors who reigned during a specific period."""
        return [emperor for emperor in self.emperors 
                if not (emperor.reign_end < start_year or emperor.reign_start > end_year)]
    
    def get_emperors_by_zodiac(self, zodiac_sign):
        """Get all emperors with a specific zodiac sign."""
        return [emperor for emperor in self.emperors if emperor.zodiac == zodiac_sign]
    
    def get_longest_reigning(self, top_n=1):
        """Get the top N longest-reigning emperors."""
        return sorted(self.emperors, key=lambda x: x.reign_duration(), reverse=True)[:top_n]
    
    def get_shortest_reigning(self, top_n=1):
        """Get the top N shortest-reigning emperors."""
        return sorted(self.emperors, key=lambda x: x.reign_duration())[:top_n]
    
    def get_oldest_at_death(self, top_n=1):
        """Get the top N oldest emperors at death."""
        return sorted(self.emperors, key=lambda x: x.age_at_death(), reverse=True)[:top_n]
    
    def get_youngest_at_accession(self, top_n=1):
        """Get the top N youngest emperors at accession."""
        return sorted(self.emperors, key=lambda x: x.age_at_accession())[:top_n]
    
    def get_most_achievements(self, top_n=1):
        """Get the top N emperors with the most notable achievements."""
        return sorted(self.emperors, key=lambda x: len(x.notable_achievements), reverse=True)[:top_n]
        
    def get_emperors_by_wife(self, wife_name):
        """Get all emperors who were married to a woman with the given name."""
        emperors_with_wife = []
        for emperor in self.emperors:
            for wife in emperor.wives:
                if wife_name.lower() in wife.lower():
                    emperors_with_wife.append(emperor)
                    break
        return emperors_with_wife


def create_roman_empire():
    """Create and populate the Roman Empire with historical emperors."""
    empire = RomanEmpire()
    
    # Julio-Claudian Dynasty
    augustus = RomanEmperor(
        name="Augustus (Octavian)",
        birth=-63,  # 63 BCE
        death=14,   # 14 CE
        reign_start=-27,  # 27 BCE
        reign_end=14,
        dynasty="Julio-Claudian",
        notable_achievements=[
            "First Roman Emperor",
            "Established the Pax Romana (Roman Peace)",
            "Rebuilt much of Rome's infrastructure",
            "Established a standing army and Praetorian Guard"
        ],
        cause_of_death="Natural causes",
        wives=[
            "Clodia Pulchra (divorced)",
            "Scribonia (divorced)",
            "Livia Drusilla"
        ],
        zodiac="Libra"
    )
    
    tiberius = RomanEmperor(
        name="Tiberius",
        birth=-42,
        death=37,
        reign_start=14,
        reign_end=37,
        dynasty="Julio-Claudian",
        notable_achievements=[
            "Expanded the empire in Germania",
            "Reformed the imperial treasury",
            "Military victories in Pannonia and Illyricum"
        ],
        cause_of_death="Either natural causes or murdered by Caligula",
        predecessor="Augustus",
        wives=[
            "Vipsania Agrippina (divorced)",
            "Julia the Elder (Augustus's daughter)"
        ],
        zodiac="Scorpio"
    )
    
    caligula = RomanEmperor(
        name="Caligula (Gaius)",
        birth=12,
        death=41,
        reign_start=37,
        reign_end=41,
        dynasty="Julio-Claudian",
        notable_achievements=[
            "Built new aqueducts and harbors",
            "Annexed Mauretania"
        ],
        cause_of_death="Assassinated by Praetorian Guard",
        predecessor="Tiberius",
        wives=[
            "Junia Claudilla",
            "Livia Orestilla (briefly)",
            "Lollia Paulina (briefly)",
            "Milonia Caesonia"
        ],
        zodiac="Virgo"
    )
    
    claudius = RomanEmperor(
        name="Claudius",
        birth=-10,
        death=54,
        reign_start=41,
        reign_end=54,
        dynasty="Julio-Claudian",
        notable_achievements=[
            "Conquered Britain",
            "Expanded the imperial bureaucracy",
            "Built many public works including the Aqua Claudia aqueduct",
            "Reformed the legal system"
        ],
        cause_of_death="Poisoned (likely by his wife Agrippina)",
        predecessor="Caligula",
        wives=[
            "Plautia Urgulanilla (divorced)",
            "Aelia Paetina (divorced)",
            "Valeria Messalina (executed)",
            "Agrippina the Younger (his niece)"
        ],
        zodiac="Leo"
    )
    
    nero = RomanEmperor(
        name="Nero",
        birth=37,
        death=68,
        reign_start=54,
        reign_end=68,
        dynasty="Julio-Claudian",
        notable_achievements=[
            "Built the Domus Aurea (Golden House)",
            "Initially popular for tax reforms",
            "Diplomatic solution to conflict with Parthia"
        ],
        cause_of_death="Suicide after being declared a public enemy",
        predecessor="Claudius",
        wives=[
            "Claudia Octavia (executed)",
            "Poppaea Sabina (died; possibly kicked to death by Nero)",
            "Statilia Messalina"
        ],
        zodiac="Sagittarius"
    )
    
    # Year of the Four Emperors (69 CE)
    galba = RomanEmperor(
        name="Galba",
        birth=-3,
        death=69,
        reign_start=68,
        reign_end=69,
        dynasty="Year of the Four Emperors",
        notable_achievements=[
            "First emperor in the Year of the Four Emperors",
            "Attempted financial reforms"
        ],
        cause_of_death="Assassinated in a coup led by Otho",
        predecessor="Nero",
        wives=[],  # Galba never married
        zodiac="Capricorn"
    )
    
    otho = RomanEmperor(
        name="Otho",
        birth=32,
        death=69,
        reign_start=69,
        reign_end=69,
        dynasty="Year of the Four Emperors",
        notable_achievements=[
            "Former governor of Lusitania",
            "Briefly recognized by the Senate"
        ],
        cause_of_death="Suicide after defeat in battle",
        predecessor="Galba",
        wives=[
            "Poppaea Sabina (later married Nero)"
        ],
        zodiac="Aries"
    )
    
    vitellius = RomanEmperor(
        name="Vitellius",
        birth=15,
        death=69,
        reign_start=69,
        reign_end=69,
        dynasty="Year of the Four Emperors",
        notable_achievements=[
            "Former governor of Germania Inferior",
            "Lavish banquets and entertainments"
        ],
        cause_of_death="Executed by Vespasian's troops",
        predecessor="Otho",
        wives=[
            "Petronia",
            "Galeria Fundana"
        ],
        zodiac="Virgo"
    )
    
    # Flavian Dynasty
    vespasian = RomanEmperor(
        name="Vespasian",
        birth=9,
        death=79,
        reign_start=69,
        reign_end=79,
        dynasty="Flavian",
        notable_achievements=[
            "Restored stability after civil war",
            "Began construction of the Colosseum",
            "Financial reforms and balanced budget",
            "Conquered Judaea and destroyed the Temple in Jerusalem"
        ],
        cause_of_death="Natural causes",
        predecessor="Vitellius",
        wives=[
            "Flavia Domitilla",
            "Caenis (concubine after Domitilla's death)"
        ],
        zodiac="Scorpio"
    )
    
    titus = RomanEmperor(
        name="Titus",
        birth=39,
        death=81,
        reign_start=79,
        reign_end=81,
        dynasty="Flavian",
        notable_achievements=[
            "Completed the Colosseum",
            "Handled the eruption of Mount Vesuvius",
            "Provided relief after a fire in Rome"
        ],
        cause_of_death="Fever (possibly malaria)",
        predecessor="Vespasian",
        wives=[
            "Arrecina Tertulla (died)",
            "Marcia Furnilla (divorced)"
        ],
        zodiac="Capricorn"
    )
    
    domitian = RomanEmperor(
        name="Domitian",
        birth=51,
        death=96,
        reign_start=81,
        reign_end=96,
        dynasty="Flavian",
        notable_achievements=[
            "Strengthened the economy and currency",
            "Expanded the border fortifications",
            "Major building programs in Rome",
            "Military campaigns in Germania and Dacia"
        ],
        cause_of_death="Assassinated in palace conspiracy",
        predecessor="Titus",
        wives=[
            "Domitia Longina"
        ],
        zodiac="Scorpio"
    )
    
    # Nerva-Antonine Dynasty (Five Good Emperors and more)
    nerva = RomanEmperor(
        name="Nerva",
        birth=30,
        death=98,
        reign_start=96,
        reign_end=98,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "Established the tradition of adoptive succession",
            "Land reforms to help the poor",
            "Reduced taxes and improved the grain supply"
        ],
        cause_of_death="Natural causes",
        predecessor="Domitian",
        wives=[],  # No known wives
        zodiac="Aquarius"
    )
    
    trajan = RomanEmperor(
        name="Trajan",
        birth=53,
        death=117,
        reign_start=98,
        reign_end=117,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "Expanded the Empire to its greatest territorial extent",
            "Conquered Dacia and its gold mines",
            "Extensive public building program",
            "Created alimenta welfare program for poor children",
            "Trajan's Column and Trajan's Forum"
        ],
        cause_of_death="Illness (possibly stroke)",
        predecessor="Nerva",
        wives=[
            "Pompeia Plotina"
        ],
        zodiac="Virgo"
    )
    
    hadrian = RomanEmperor(
        name="Hadrian",
        birth=76,
        death=138,
        reign_start=117,
        reign_end=138,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "Built Hadrian's Wall in Britain",
            "Extensive traveling throughout the empire",
            "Promoted Greek culture (philhellenism)",
            "Built the Pantheon in its current form",
            "Built his massive villa at Tivoli"
        ],
        cause_of_death="Heart failure",
        predecessor="Trajan",
        wives=[
            "Vibia Sabina (Trajan's grandniece)"
        ],
        zodiac="Aquarius"
    )
    
    antoninus_pius = RomanEmperor(
        name="Antoninus Pius",
        birth=86,
        death=161,
        reign_start=138,
        reign_end=161,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "One of the most peaceful reigns",
            "Effective administration and sound finances",
            "Legal reforms protecting slaves and orphans",
            "Built the Antonine Wall in Scotland"
        ],
        cause_of_death="Natural causes",
        predecessor="Hadrian",
        wives=[
            "Faustina the Elder"
        ],
        zodiac="Virgo"
    )
    
    marcus_aurelius = RomanEmperor(
        name="Marcus Aurelius",
        birth=121,
        death=180,
        reign_start=161,
        reign_end=180,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "Philosopher emperor who wrote 'Meditations'",
            "Successfully defended borders against Germanic tribes",
            "Dealt with the Antonine Plague",
            "Last of the 'Five Good Emperors'"
        ],
        cause_of_death="Illness (possibly plague)",
        predecessor="Antoninus Pius",
        wives=[
            "Faustina the Younger (daughter of Antoninus Pius)"
        ],
        zodiac="Aries"
    )
    
    commodus = RomanEmperor(
        name="Commodus",
        birth=161,
        death=192,
        reign_start=180,
        reign_end=192,
        dynasty="Nerva-Antonine",
        notable_achievements=[
            "Ended wars with Germanic tribes",
            "Presented himself as Hercules",
            "Participated as a gladiator in the Colosseum"
        ],
        cause_of_death="Strangled in his bath after failed poisoning",
        predecessor="Marcus Aurelius",
        wives=[
            "Bruttia Crispina (exiled and later executed)"
        ],
        zodiac="Virgo"
    )
    
    # Severan Dynasty (selection)
    septimius_severus = RomanEmperor(
        name="Septimius Severus",
        birth=145,
        death=211,
        reign_start=193,
        reign_end=211,
        dynasty="Severan",
        notable_achievements=[
            "Military reforms favoring the army",
            "Campaigns in Parthia and Britain",
            "Increased the role of the military in government",
            "Restored stability after civil war"
        ],
        cause_of_death="Illness during campaign in Britain",
        predecessor="Pertinax/Didius Julianus",
        wives=[
            "Paccia Marciana (died)",
            "Julia Domna (Syrian noblewoman)"
        ],
        zodiac="Aries"
    )
    
    caracalla = RomanEmperor(
        name="Caracalla",
        birth=188,
        death=217,
        reign_start=211,
        reign_end=217,
        dynasty="Severan",
        notable_achievements=[
            "Constitutio Antoniniana (granted citizenship to all free men)",
            "Built the massive Baths of Caracalla",
            "Military campaigns against Germanic tribes and Parthians",
            "Doubled pay for soldiers"
        ],
        cause_of_death="Assassinated by a disgruntled soldier",
        predecessor="Septimius Severus",
        wives=[
            "Fulvia Plautilla (executed)"
        ],
        zodiac="Aries"
    )
    
    # Crisis of the Third Century (just a selection)
    diocletian = RomanEmperor(
        name="Diocletian",
        birth=244,
        death=311,
        reign_start=284,
        reign_end=305,
        dynasty="Tetrarchy",
        notable_achievements=[
            "Ended the Crisis of the Third Century",
            "Established the Tetrarchy (rule of four)",
            "Administrative reforms dividing the empire",
            "Economic reforms including price controls",
            "Major persecution of Christians"
        ],
        cause_of_death="Natural causes (retired)",
        predecessor="Numerian",
        wives=[
            "Prisca"
        ],
        zodiac="Capricorn"
    )
    
    # Constantine Dynasty
    constantine = RomanEmperor(
        name="Constantine the Great",
        birth=272,
        death=337,
        reign_start=306,
        reign_end=337,
        dynasty="Constantinian",
        notable_achievements=[
            "First Christian emperor",
            "Edict of Milan (religious tolerance)",
            "Founded Constantinople as new capital",
            "Convened the First Council of Nicaea",
            "Reunited the empire after civil wars",
            "Created new government and military structure"
        ],
        cause_of_death="Illness",
        predecessor="Constantius I Chlorus (in the West)",
        wives=[
            "Minervina",
            "Fausta (daughter of Maximian)"
        ],
        zodiac="Pisces"
    )
    
    # Add all emperors to the empire
    for emperor in [augustus, tiberius, caligula, claudius, nero, galba, otho, vitellius, 
                   vespasian, titus, domitian, nerva, trajan, hadrian, antoninus_pius, 
                   marcus_aurelius, commodus, septimius_severus, caracalla, diocletian, constantine]:
        empire.add_emperor(emperor)
    
    # Set successors
    augustus.successor = tiberius
    tiberius.successor = caligula
    caligula.successor = claudius
    claudius.successor = nero
    nero.successor = galba
    galba.successor = otho
    otho.successor = vitellius
    vitellius.successor = vespasian
    vespasian.successor = titus
    titus.successor = domitian
    domitian.successor = nerva
    nerva.successor = trajan
    trajan.successor = hadrian
    hadrian.successor = antoninus_pius
    antoninus_pius.successor = marcus_aurelius
    marcus_aurelius.successor = commodus
    
    return empire


def main():
    """Main function to demonstrate the functionality."""
    roman_empire = create_roman_empire()
    
    print("=== ROMAN EMPERORS DATABASE ===")
    print(f"Total emperors in database: {len(roman_empire.emperors)}")
    print(f"Dynasties: {', '.join(sorted(roman_empire.dynasties))}")
    print("\n")
    
    # Example queries
    print("=== LONGEST REIGNING EMPERORS ===")
    for emperor in roman_empire.get_longest_reigning(3):
        print(f"{emperor.name}: {emperor.reign_duration()} years")
    print("\n")
    
    print("=== JULIO-CLAUDIAN DYNASTY ===")
    for emperor in roman_empire.get_emperors_by_dynasty("Julio-Claudian"):
        print(emperor.name)
    print("\n")
    
    print("=== EMPERORS WHO RULED DURING THE 1ST CENTURY CE ===")
    for emperor in roman_empire.get_emperors_by_period(1, 100):
        print(f"{emperor.name}: {emperor.reign_start} - {emperor.reign_end} CE")
    print("\n")
    
    print("=== DETAILED INFORMATION ABOUT AUGUSTUS ===")
    augustus = roman_empire.get_emperor_by_name("Augustus")
    print(augustus)
    print("\n")
    
    print("=== EMPERORS WHO DIED BY ASSASSINATION ===")
    assassinated = [emp for emp in roman_empire.emperors 
                   if emp.cause_of_death and "assassinated" in emp.cause_of_death.lower()]
    for emperor in assassinated:
        print(f"{emperor.name}: {emperor.cause_of_death}")
    print("\n")
    
    print("=== YOUNGEST EMPERORS AT ACCESSION ===")
    for emperor in roman_empire.get_youngest_at_accession(3):
        print(f"{emperor.name}: {emperor.age_at_accession()} years old")
    print("\n")
    
    print("=== EMPERORS WITH MOST ACHIEVEMENTS ===")
    for emperor in roman_empire.get_most_achievements(3):
        print(f"{emperor.name}: {len(emperor.notable_achievements)} notable achievements")
    print("\n")
    
    # New queries for wives and zodiac signs
    print("=== EMPERORS BY ZODIAC SIGN ===")
    zodiac_signs = set(emperor.zodiac for emperor in roman_empire.emperors if emperor.zodiac)
    for sign in sorted(zodiac_signs):
        emperors = roman_empire.get_emperors_by_zodiac(sign)
        emperor_names = [emp.name for emp in emperors]
        print(f"{sign}: {', '.join(emperor_names)}")
    print("\n")
    
    # Add emperor lookup by year
    while True:
        try:
            year_input = input("Enter a year to find who was emperor (e.g., 14, -27, or 'exit' to quit): ")
            if year_input.lower() == 'exit':
                break
                
            year = int(year_input)
            emperors = roman_empire.get_emperor_by_year(year)
            
            if emperors:
                print(f"\nIn the year {year} {'CE' if year >= 0 else 'BCE'}, the ruling emperor(s) were:")
                for emp in emperors:
                    print(f"\n{emp}")
            else:
                print(f"\nNo emperor in our database ruled in the year {year} {'CE' if year >= 0 else 'BCE'}.")
                
        except ValueError:
            print("Please enter a valid year (integer) or 'exit' to quit.")
        print()


if __name__ == "__main__":
    main()