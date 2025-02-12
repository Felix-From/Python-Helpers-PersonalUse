import random;
import datetime;

class RandomValues:
    """
    The RandomValues class provides methods to generate random values for personal information, arrays, and product details.
    
    Classes:
    
        Person:
            The Person class provides methods to generate random personal information such as names, addresses, birth dates, telephone numbers, and bank balances.
            Attributes:
                first_names (list): A list of possible first names.
                last_names (list): A list of possible last names.
                street_names (list): A list of possible street names.
            Methods:
                getName() -> str:
                getLastName() -> str:
                getBirthDay() -> datetime.date:
                getTelNumber(length: int = 10) -> str:
                getAddress(with_Number: bool = True) -> str:
                getBankBalance(allow_Minus: bool = True, as_Int: bool = True) -> Union[int, float]:

        Array:
            The Array class provides methods to generate arrays of random integers, strings, floats, and mixed types.
            Methods:
                getArrayRandInt(min_num: int = 0, max_num: int = 9, length: int = 10) -> list:
                getArrayRandStr(str_length: int = 5, length: int = 10) -> list:
                getArrayRandFloat(min_num: float = -1, max_num: float = 1, rounding: int = 2, length: int = 10) -> list:
                getArrayRandMixed(can_None: bool = False, allow_Minus: bool = False, length: int = 10) -> list:
                
        Product:
            The Product class provides methods to generate random product information such as names, sizes, descriptions, prices, and stock.
            Attributes:
                product_names (list): A list of possible product names.
                product_sizes (list): A list of possible product sizes.
                descriptions (list): A list of possible product descriptions.
            Methods:
                getName() -> str:
                getPrice(min_num = 9.99, max_num = 119.99) -> float:
                getSize() -> str:
                getDescription() -> str:
                getStock(min_num = 0, max_num = 50) -> int:
    """
    
    class Person:
        """
        The Person class provides methods to generate random personal information such as names, addresses, birth dates, telephone numbers, and bank balances.
        Attributes:
            first_names (list): A list of possible first names.
            last_names (list): A list of possible last names.
            street_names (list): A list of possible street names.
        Methods:
            getName() -> str:
                Returns a random first name from the list of first names.
            getLastName() -> str:
                Returns a random last name from the list of last names.
            getBirthDay() -> datetime.date:
                Returns a random birth date for a person aged between 18 and 60 years.
            getTelNumber(length: int = 10) -> str:
                Returns a random telephone number of the specified length.
            getAddress(with_Number: bool = True) -> str:
                Returns a random address, optionally including a house number.
            getBankBalance(allow_Minus: bool = True, as_Int: bool = True) -> Union[int, float]:
                Returns a random bank balance, optionally allowing negative values and specifying the return type as integer or float.
        """
        first_names = [
        "Lena", "Maximilian", "Hannah", "Paul", "Sophia", "Leon", "Emilia", "Elias", "Marie", "Ben",
        "Mia", "Noah", "Anna", "Felix", "Emma", "Lukas", "Lina", "Julian", "Lea", "Finn",
        "Clara", "Luis", "Ella", "Tim", "Charlotte", "Jonas", "Johanna", "Niklas", "Luisa", "David",
        "Sarah", "Tom", "Isabella", "Fabian", "Amelie", "Simon", "Franziska", "Tobias", "Helena", "Matteo",
        "Nina", "Samuel", "Eva", "Jan", "Laura", "Florian", "Sophie", "Sebastian", "Melina", "Marco",
        "Marlene", "Alexander", "Annika", "Oliver", "Jana", "Dominik", "Carla", "Patrick", "Theresa", "Konstantin",
        "Rebecca", "Benedikt", "Valentina", "Philipp", "Antonia", "Moritz", "Selina", "Christoph", "Helene", "Dennis",
        "Jasmin", "Kevin", "Vanessa", "Raphael", "Lisa", "Stefan", "Katharina", "Marc", "Miriam", "Daniel",
        "Veronika", "Adrian", "Anja", "Marcel", "Elena", "Rene", "Julia", "Timo", "Angelina", "Markus",
        "Celina", "Johannes", "Emily", "Andreas", "Mira", "Christian", "Jule", "Thomas", "Caroline", "Manuel"
        ]

        last_names = [
            "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
            "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann", "Schwarz", "Zimmermann", "Braun",
            "Krüger", "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier", "Lehmann",
            "Schmid", "Schulze", "Maier", "Köhler", "Herrmann", "König", "Mayer", "Walter", "Möller", "Huber",
            "Frank", "Berger", "Peters", "Lang", "Scholz", "Jung", "Keller", "Fuchs", "Schubert", "Weiß",
            "Dieter", "Pohl", "Lorenz", "Baumann", "Roth", "Schuster", "Graf", "Jäger", "Schumacher", "Ludwig",
            "Böhm", "Heinrich", "Albrecht", "Schön", "Kraus", "Ott", "Busch", "Simon", "Fiedler", "Brandt",
            "Götz", "Arnold", "Kuhn", "Winkler", "Binder", "Bach", "Sauer", "Hoppe", "Dietrich", "Kern",
            "Stephan", "Bergmann", "Schilling", "Frey", "Seidel", "Brunner", "Voigt", "Nowak", "Adam",
            "Haas", "Schuster", "Ulrich", "Wirth", "Hauser", "Krieger", "Reinhardt", "Wegner", "Behrens", "Brand"
        ]
        
        street_names = [
            "Hauptstraße", "Bahnhofstraße", "Dorfstraße", "Schulstraße", "Gartenstraße", "Ringstraße", "Kirchstraße", "Feldstraße", "Bergstraße", "Lindenstraße",
            "Goethestraße", "Schillerstraße", "Mühlenstraße", "Rosenstraße", "Birkenweg", "Parkstraße", "Brunnenstraße", "Sonnenstraße", "Friedrichstraße", "Jahnstraße",
            "Beethovenstraße", "Mozartstraße", "Bachstraße", "Lessingstraße", "Theodor-Heuss-Straße", "Wilhelmstraße", "Schubertstraße", "Uhlandstraße", "Rathausstraße", "Am Sportplatz",
            "Poststraße", "Dammstraße", "Marktplatz", "Kastanienweg", "Am Hang", "Neue Straße", "Tulpenweg", "Nelkenweg", "Eichenweg", "Erlenweg",
            "Tannenweg", "Ahornweg", "Fichtenweg", "Akazienweg", "Platanenweg", "Im Wiesengrund", "Am Waldrand", "Wiesenstraße", "Seestraße", "Weidenweg",
            "An der Mühle", "An der Kirche", "An der Schule", "Dorfplatz", "Schloßstraße", "Buchenweg", "Kiefernweg", "Industriestraße", "Werkstraße", "Grenzstraße"
        ]
        random.shuffle(first_names)
        random.shuffle(last_names)
        random.shuffle(street_names)
        
        @classmethod
        def getName(cls):
            """
            getName() -> str:
                Returns a random first name from the list of first names."""
            return random.choice(cls.first_names)
        
        @classmethod
        def getLastName(cls):
            """
            getLastName() -> str:
                Returns a random last name from the list of last names."""
            return random.choice(cls.last_names)
        
        def getBirthDay()->datetime.date:
            """
            getBirthDay() -> datetime.date:
                Returns a random birth date for a person aged between 18 and 60 years."""
            date = datetime.date.today()
            date = datetime.date(
                                random.randint((date.year-60),(date.year-18)) # Year
                                ,random.randint(1,12) # Month
                                ,random.randint(1,28)); # Day
            return date;
        
        def getTelNumber(length = 10):
            """
            getTelNumber(length: int = 10) -> str:
                Returns a random telephone number of the specified length."""
            return "".join(str(random.randint(0, 9)) for _ in range(length))
        
        @classmethod
        def getAddress(cls,with_Number = True):
            """
            getAddress(with_Number: bool = True) -> str:
                Returns a random address, optionally including a house number."""
            return (random.choice(cls.street_names) + (" " + str(random.randint(1, 117)) if with_Number else ""))

        def getBankBalance(allow_Minus=True, as_Int=True):
            """
            getBankBalance(allow_Minus: bool = True, as_Int: bool = True) -> Union[int, float]:
                Returns a random bank balance, optionally allowing negative values and specifying the return type as integer or float."""
            # Old Legacy Code :D ((random.randint(-1234,5432)) if allow_Minus else (random.randint(1,5432))) if as_Int else (round((random.randrange(-1234,5432)/1.5),2) if allow_Minus else round((random.randrange(1,5432)/1.5))
            if as_Int:
                if allow_Minus:
                    return random.randint(-1234, 5432)
                else:
                    return random.randint(1, 5432)
            else:
                if allow_Minus:
                    return round(random.uniform(-1234, 5432), 2)
                else:
                    return round(random.uniform(1, 5432), 2)
    
    class Array(Person):
        class Array:
            """
            A class to generate arrays of random integers, strings, floats, and mixed types.

            Methods
            -------
            getArrayRandInt(min_num=0, max_num=9, length=10):
                Generates an array of random integers within a specified range.

            getArrayRandStr(str_length=5, length=10):
                Generates an array of random strings of a specified length.

            getArrayRandFloat(min_num=-1, max_num=1, rounding=2, length=10):
                Generates an array of random floats within a specified range and rounding precision.

            getArrayRandMixed(can_None=False, allow_Minus=False, length=10):
                Generates an array of mixed types (strings, integers, floats, and optionally None).
            """
            
        def getArrayRandInt(min_num = 0, max_num = 9,length = 10):
            """
            getArrayRandInt(min_num=0, max_num=9, length=10):
                Generates an array of random integers within a specified range."""
            return [(random.randint(min_num, max_num)) for _ in range(length)]
        
        def getArrayRandStr(str_length = 5,length = 10):
            """
            getArrayRandStr(str_length=5, length=10):
                Generates an array of random strings of a specified length."""
            return ["".join(chr(random.randint(65, 90)) for __ in range(str_length)) for _ in range(length)]
        
        def getArrayRandFloat(min_num = -1, max_num =1, rounding=2, length = 10):
            """
            getArrayRandFloat(min_num=-1, max_num=1, rounding=2, length=10):
                Generates an array of random floats within a specified range and rounding precision."""
            return [(round(random.uniform(min_num,max_num),rounding)) for _ in range(length)]
        
        def getArrayRandMixed(can_None = False, allow_Minus = False, length = 10):
            """
            getArrayRandMixed(can_None=False, allow_Minus=False, length=10):
                Generates an array of mixed types (strings, integers, floats, and optionally None)."""
            result = []
            for _ in range(length):
                temp = random.randint(0,3 if can_None else 2)
                if temp == 0 : #String
                    result.append("".join(chr(random.randint(65, 90)) for _ in range(5)))
                elif temp == 1 : # Int
                    result.append(random.randint(0,15000))
                elif temp == 2 :
                    result.append(round(random.uniform(-20 if allow_Minus else 0,30),2))
                else:
                    result.append(None)
            return result

    class Product:
        """
        A class to generate Product info such as name, size, description, price, and stock.
        
        Attributes:
            product_names : list
                A list of possible product names.
            product_sizes : list
                A list of possible product sizes.
            descriptions : list
                A list of possible product descriptions.
        
        Methods:
            getName() -> str:
                Returns a random product name from the product_names list.
            getPrice(min_num = 9.99, max_num = 119.99) -> float:
                Returns a random price between min_num and max_num.
            getSize() -> str:
                Returns a random product size from the product_sizes list.
            getDescription() -> str:
                Returns a random product description from the descriptions list.
            getStock(min_num = 0, max_num = 50) -> int:
                Returns a random stock value between min_num and max_num.
        """
        
        product_names = [
            "Nutella", "80kg Stahlofen", "Backofenpommes", "Wunderbohrer 3000", "Megastarker Panzertape-Roller",
            "Selbstumrührender Kaffeebecher", "Turboschnelle Mikrowelle", "Hyperflexibler Gartenschlauch",
            "Unkaputtbare Sonnenbrille", "Der letzte Kugelschreiber", "Fliegender Rasenmäher",
            "Alleskönner-Kleber", "Unsichtbarer Wandhaken", "Magnetischer Seifenspender",
            "Smarte Toilettenbürste", "WLAN-fähiger Toaster", "Selbsterhitzende Bettdecke",
            "Klimaneutraler Laubbläser", "Elektrischer Schuhlöffel", "Titanverstärkte Kaffeetasse",
            "Anti-Schwerkraft Stuhl", "Koffein-infundiertes Duschgel", "Doppel-Sockenschuhe",
            "Vibrationsbetriebene Zahnbürste", "Multifunktionale Heißklebepistole", "Ultra-leichter Vorschlaghammer",
            "Selbstkühlende Wasserflasche", "Selbstnachfüllender Tintenfüller", "Bügelfreies Hemd",
            "Roboter-Rasenmäher", "Der letzte Schraubenzieher", "Energieeffiziente Taschenlampe",
            "Schwerkraftresistenter Fallschirm", "Kugelsicherer Fahrradhelm", "Autonome Putzdrohne",
            "Fernsteuerbarer Einkaufswagen", "Der intelligente Einkaufszettel", "Nie-mehr-verlorene Socken",
            "Solargepowerte Nachttischlampe", "Rasiermesser-scharfe Butterschaufel", "100% Wasserfeste Gummiente",
            "Bluetooth-fähige Zahnbürste", "Flammenresistente Grillhandschuhe", "Energiesparender Haarföhn",
            "Schwerkraftreduzierende Hanteln", "Anti-Diebstahl Keksdose", "Robustes USB-Kabel",
            "Drahtlose Verlängerungsschnur", "Lärmabsorbierende Ohrenstöpsel", "Solarbetriebene Handwärmer",
            "Gehirnaktivierender Kaugummi", "Magnetische Pizzaschneider", "Nie-verknotete Kopfhörer",
            "Der unsichtbare Kleiderbügel", "Superleiser Staubsauger", "Automatischer Türöffner",
            "3D-druckbares Essbesteck", "Klimaanlagen-kompatible Wolldecke", "Unzerstörbare Haargummis",
            "Die letzte Schere, die du brauchst", "Biologisch abbaubare Klebebänder",
            "Der smarte Wasserkocher", "Selbstbewässernder Blumentopf", "Wärmende Socken mit USB",
            "Anti-Rutsch Seife", "Unzerstörbare Gabel", "Doppelseitiger Kaffeebecher",
            "Universelle Fernbedienung für alles", "Unhörbarer Wecker", "Der selbstreinigende Teppich",
            "Der bruchsichere Spiegel", "Ewiges Feuerzeug", "Stromsparende Weihnachtslichterkette",
            "Magnetische Wandfarbe", "Smarte Kühlschrankmagneten", "Automatische Geschenkeverpackung",
            "Sicherheits-Laserschere", "Schwerkraft-angepasste Socken", "Der beste Toaster der Welt",
            "Automatischer Mülleimer", "Der bruchfeste Eierlöffel", "Vibrations-Klingel",
            "Anti-Licht Lampe", "Der perfekte Pizzastein","Luftfilter für deine Gedanken", 
            "Der selbstkochende Kochtopf", "Superweiche Kuscheldecke",
            "Das Unendliche-Klebeband", "Der hypermoderne Sandkasten", "Kaffee mit integriertem Löffel",
            "Energiesparender Staubsauger", "Nie-wieder-verknotete Kabelbinder", "Das ultimative Ladekabel",
            "Die selbstauffüllende Seifenschale", "Multifunktionaler Spülmaschinenkorb", "Nie-leer-werdender Kuli"
        ]
        
        product_sizes = [
            "5 Eimer randvoll",
            "8 Paletten",
            "3 Einkaufswagen bis oben hin",
            "Eine Badewanne randvoll",
            "2 Umzugskartons, aber ordentlich gestapelt",
            "10 Türme a 3 Kisten",
            "1 Kofferraum, wenn man gut packt",
            "4 Regalböden voll",
            "Eine Waschmaschinentrommel voll",
            "6 Kisten, die eigentlich zu schwer sind",
            "1 LKW Ladung",
            "1/16 Pfund"
        ]

        descriptions = [
            "Das Ding!, das jeder haben will", "Perfekt für alle, die eigentlich nichts brauchen",
            "Löst Probleme, die du nie hattest", "Mehr als nur ein Ding - ein Erlebnis!",
            "Ersetzt mindestens drei Dinge, die du schon besitzt", "So gut, dass du es doppelt kaufen willst",
            "Ein Muss für alle, die immer auf der Suche nach dem neuesten Unsinn sind",
            "Ein Design-Meisterwerk, das niemand versteht", "Viel zu teuer, aber hey - warum nicht?",
            "Endlich da, obwohl keiner gefragt hat", "Minimalistisches Chaos in Perfektion",
            "Macht genau das, was du denkst - und noch weniger", "Für alle, die schon alles haben und trotzdem mehr wollen",
            "Funktioniert! Meistens.", "Nie wieder ohne! Bis du es verlierst.", "Nachhaltig - irgendwie.",
            "Definitiv ein Gesprächsstarter", "100% Zufriedenheit! Außer wenn nicht.", "Technologisch fortgeschritten, aber unnötig",
            "Mehr Features als du jemals brauchen wirst", "Sieht futuristisch aus, fühlt sich aber normal an",
            "Passt in jede Tasche! Außer wenn nicht.", "Besser als nix", "Reduziert Stress - oder erzeugt ihn",
            "Lässt dich smarter aussehen, als du bist", "Fühlt sich luxuriös an, ist es aber nicht",
            "Genau das, was du nicht wusstest, dass du brauchst", "Inspiriert dich! Vielleicht.",
            "Garantiert Aufmerksamkeit - aber nicht immer die gute", "Genial einfach, aber nicht einfach genial",
            "Kompliziert gemacht, damit du es einfacher hast", "Nie mehr ohne! Außer du vergisst es",
            "Löst kein Problem, sieht aber schick aus", "Das perfekte Geschenk für Leute, die du nicht magst",
            "So praktisch, dass du es nie benutzt", "Erstaunlich nutzlos und doch faszinierend",
            "Ein Klassiker der Zukunft - vielleicht", "Erhöht deinen Status um genau 0 Punkte",
            "Passt zu allem, was du nicht hast", "So robust, dass es trotzdem kaputt geht",
            "Für die einen Schrott, für die anderen Kunst", "Innovativ - laut Hersteller",
            "Nachhaltig! Bis du es wegwirfst.", "Funktioniert perfekt, wenn du keine Ansprüche hast"
        ]
        
        random.shuffle(product_names)
        random.shuffle(product_sizes)
        random.shuffle(descriptions)
        
        @classmethod
        def getName(cls) -> str:
            """
            getName() -> str:
                Returns a random product name from the product_names list."""
            return random.choice(cls.product_names)
        def getPrice(min_num = 9.99, max_num = 119.99) -> float:
            """
            getPrice(min_num = 9.99, max_num = 119.99) -> float:
                Returns a random price between min_num and max_num."""
            return round(random.uniform(min_num,max_num),2)
        @classmethod
        def getSize(cls) -> str:
            """
            getSize() -> str:
                Returns a random product size from the product_sizes list."""
            return random.choice(cls.product_sizes)
        @classmethod
        def getDescription(cls):
            """
            getDescription() -> str:
                Returns a random product description from the descriptions list."""
            return random.choice(cls.descriptions)
        def getStock(min_num = 0, max_num = 50):
            """
            getStock(min_num = 0, max_num = 50) -> int:
                Returns a random stock value between min_num and max_num."""
            return random.randint(min_num,max_num)
        
def FunctionTest_RandomValues():
    print("FunctionTest - RandomValues")
    print()
    print("Person Class:")
    print()
    print("Person Name: "+RandomValues.Person.getName(), end=" ")
    print("Person LastName: "+RandomValues.Person.getLastName())
    print("Person Birthday: "+RandomValues.Person.getBirthDay().strftime("%d.%m.%Y"))
    print("Person Address with Number: "+RandomValues.Person.getAddress())
    print("Person Address without Number: "+RandomValues.Person.getAddress(False))
    print("Bank Balance: " + str(RandomValues.Person.getBankBalance()))
    print("Bank Balance (no minus): " + str(RandomValues.Person.getBankBalance(allow_Minus=False)))
    print("Bank Balance (float): " + str(RandomValues.Person.getBankBalance(as_Int=False)))
    print("Bank Balance (no minus, float): " + str(RandomValues.Person.getBankBalance(allow_Minus=False, as_Int=False)))
    print()
    print("Array Class:")
    print()
    print("Array Int: " + str(RandomValues.Array.getArrayRandInt()))
    print("Array Int (min 3): " + str(RandomValues.Array.getArrayRandInt(min_num=3)))
    print("Array Int (3-5): " + str(RandomValues.Array.getArrayRandInt(min_num=3, max_num=5)))
    print("Array Int (3-5, length 20): " + str(RandomValues.Array.getArrayRandInt(min_num=3, max_num=5, length=20)))
    print("Array Int (max 5, length 10): " + str(RandomValues.Array.getArrayRandInt(max_num=5, length=10)))
    print("Array Int (length 20): " + str(RandomValues.Array.getArrayRandInt(length=20)))

    print("Array Str: " + str(RandomValues.Array.getArrayRandStr()))
    print("Array Str (length 20): " + str(RandomValues.Array.getArrayRandStr(length=20)))
    print("Array Str (str length 10): " + str(RandomValues.Array.getArrayRandStr(str_length=10)))
    print("Array Str (str length 10, length 20): " + str(RandomValues.Array.getArrayRandStr(str_length=10, length=20)))

    print("Array Float: " + str(RandomValues.Array.getArrayRandFloat()))
    print("Array Float (min -10): " + str(RandomValues.Array.getArrayRandFloat(min_num=-10)))
    print("Array Float (max 200): " + str(RandomValues.Array.getArrayRandFloat(max_num=200)))
    print("Array Float (1-30): " + str(RandomValues.Array.getArrayRandFloat(min_num=1, max_num=30)))
    print("Array Float (1-10, length 20): " + str(RandomValues.Array.getArrayRandFloat(min_num=1, max_num=10, length=20)))
    print("Array Float (rounding 4): " + str(RandomValues.Array.getArrayRandFloat(rounding=4)))
    print("Array Float (min 4, rounding 4): " + str(RandomValues.Array.getArrayRandFloat(min_num=4, rounding=4)))
    print("Array Float (length 20, rounding 4): " + str(RandomValues.Array.getArrayRandFloat(length=20, rounding=4)))

    print("Array Mix: " + str(RandomValues.Array.getArrayRandMixed()))
    print("Array Mix (can None): " + str(RandomValues.Array.getArrayRandMixed(can_None=True)))
    print("Array Mix (allow Minus, length 20): " + str(RandomValues.Array.getArrayRandMixed(allow_Minus=True, length=20)))
    print("Array Mix (length 20): " + str(RandomValues.Array.getArrayRandMixed(length=20)))

    print()
    print("Project Class")
    print()
    
    print("Name: "+RandomValues.Product.getName())
    print("Beschreibung: "+RandomValues.Product.getDescription())
    print("Preis: "+str(RandomValues.Product.getPrice())+" €")
    print("Größe: "+RandomValues.Product.getSize())
    print("Lager: "+str(RandomValues.Product.getStock()))

    # FunctionTest - RandomValues

    # Person Class:

    # Person Name: Amelie Person LastName: Seidel
    # Person Birthday: 13.10.2001
    # Person Address with Number: Schubertstraße 101
    # Person Address without Number: Nelkenweg
    # Bank Balance: 1832
    # Bank Balance (no minus): 277
    # Bank Balance (float): 2486.37
    # Bank Balance (no minus, float): 920.48

    # Array Class:

    # Array Int: [9, 6, 8, 1, 2, 5, 4, 4, 1, 2]
    # Array Int (min 3): [7, 3, 8, 3, 4, 4, 9, 5, 5, 5]
    # Array Int (3-5): [5, 4, 3, 4, 4, 3, 4, 4, 4, 4]
    # Array Int (3-5, length 20): [3, 5, 5, 3, 3, 5, 4, 5, 3, 5, 4, 5, 4, 3, 5, 4, 3, 4, 3, 5]
    # Array Int (max 5, length 10): [2, 5, 4, 4, 3, 2, 5, 5, 0, 0]
    # Array Int (length 20): [3, 5, 7, 2, 8, 8, 4, 4, 0, 9, 6, 7, 7, 7, 4, 4, 7, 2, 6, 8]
    # Array Str: ['SZHNN', 'AUXOQ', 'EJQJE', 'EFQHL', 'QAIBZ', 'KKWGR', 'NTZXS', 'VJHXR', 'WHEMP', 'ETVXJ']
    # Array Str (length 20): ['LNGMD', 'OPHIB', 'WWFCA', 'IBEGY', 'NZFWI', 'RWUPB', 'QZURO', 'IHDYL', 'NSCON', 'WERMD', 'BVWEY', 'IOXXR', 'VVOSE', 'SACIN', 'MECTR', 'XNHTV', 'QOUCN', 'AFPAP', 'HBOIN', 'JKSHO']
    # Array Str (str length 10): ['GUTKFZXERH', 'OQTPTBULTL', 'HDOPJSODWA', 'HDEYRHZVOJ', 'ZSNYTMMQYY', 'IYUGTKNPTC', 'KWAJEAXKVL', 'NZNUXETXYU', 'XWRITYPTQP', 'YWRIZSGQKU']
    # Array Str (str length 10, length 20): ['CFJAWLMEDQ', 'NDPMGZTDUC', 'AGZZIFHMVS', 'XTNPFTRMNQ', 'CNESHYBBTR', 'CBZSFNFQFW', 'LKLPGIUBNB', 'NKDGSMOBBY', 'SBGGIPCLXT', 'RDCPJNSDGK', 'PUZLUXCQYR', 'BVKTKEJGXR', 'WNRGGCQMHH', 'BHEMWVHRHB', 'EJWQTLJKNX', 'CZRRMGETEV', 'WITKQXQWJF', 'NJCFFSQKPD', 'KVVILZTVGM', 'LZRTBKJRNO']
    # Array Float: [0.59, -0.21, 0.33, 0.11, -0.36, 0.9, 0.08, 0.26, 0.08, 0.73]
    # Array Float (min -10): [-2.97, -5.57, -4.26, -9.95, -5.47, -2.62, -2.23, -2.6, -2.75, -3.32]
    # Array Float (max 200): [196.58, 71.65, 167.01, 152.27, 123.31, 185.99, 126.72, 148.57, 9.97, 129.55]
    # Array Float (1-30): [4.38, 10.78, 6.07, 22.78, 11.66, 16.46, 12.84, 22.37, 29.96, 16.63]
    # Array Float (1-10, length 20): [1.23, 8.46, 3.38, 6.7, 5.29, 2.72, 9.38, 3.61, 8.34, 5.11, 4.04, 5.57, 1.68, 6.15, 8.53, 3.3, 9.28, 5.5, 1.34, 1.18]
    # Array Float (rounding 4): [-0.8611, 0.2259, -0.7974, -0.902, -0.5398, -0.5072, 0.9169, -0.2083, 0.3718, -0.0902]
    # Array Float (min 4, rounding 4): [1.0618, 1.0143, 2.7822, 3.1242, 1.986, 3.1528, 3.8814, 2.0367, 2.8996, 3.2999]
    # Array Float (length 20, rounding 4): [0.0209, 0.4922, -0.9486, 0.5251, 0.3795, 0.2414, 0.1031, 0.2557, 0.327, -0.8648, 0.183, 0.2729, -0.9971, 0.085, 0.8949, -0.1815, -0.3249, 0.9436, -0.4766, -0.0333]
    # Array Mix: ['TUOYE', 15.52, 493, 'PCTCT', 17.52, 'RCPUJ', 1.71, 17.0, 'JRRZR', 'LCVBB']
    # Array Mix (can None): [6.05, 20.42, None, 4.01, None, 12.49, 'ZFSZF', 3456, 5461, 11.06]
    # Array Mix (allow Minus, length 20): [4904, 5.62, 'NYGPD', 7099, 'ACTKA', 24.38, 'UDBCY', -8.63, 'TANOX', 'ACLGN', 'ENWQV', 'JQPQS', 'YOEAU', 'HUKKH', 14740, -0.66, 20.13, -3.5, 14896, 3.62]
    # Array Mix (length 20): [8.79, 6.25, 2858, 'VNUTU', 12304, 2.2, 'FJAME', 'VQUIV', 22.9, 'HRNOE', 2550, 13494, 4070, 28.58, 'NNPLD', 29.28, 'JTFCS', 'OCUIG', 9641, 9.15]

    # Project Class

    # Name: Titanverstärkte Kaffeetasse
    # Beschreibung: Ein Muss für alle, die immer auf der Suche nach dem neuesten Unsinn sind
    # Preis: 31.74 €
    # Größe: 2 Umzugskartons, aber ordentlich gestapelt
    # Lager: 49
    