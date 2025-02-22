animal:str = str(input("Inserire nome animale: "))

match animal:
    case _ if animal in ["cane", "gatto", "cavallo", "elefante", "leone"]:
        print(f"{animal} appartiene alla categoria dei Mammiferi")
    case _ if animal in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print(f"{animal} appartiene alla categoria dei Rettili")
    case _ if animal in ["aquila", "pappagallo", "gufo", "falco"]:
        print(f"{animal} appartiene alla categoria degli Uccelli ")
    case _ if animal in ["squalo", "trota", "salmone", "carpa"]:
        print(f"{animal} appartiene alla categoria dei Pesci")
    case _:
        print(f"Non so dire la categoria dell'animale '{animal}'.")