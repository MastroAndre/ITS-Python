animal:str = str(input("Inserire nome animale: "))
ex_habitat:str = str(input(f"Inserire l'habitat in cui vive l'animale {animal}: "))
habitat:str = ""

match animal:
    case "cane" | "gatto" | "cavallo" | "elefante" | "leone" | "balena" | "delfino":
        print(f"{animal} appartiene alla categoria dei Mammiferi")
        animal_type:str = "Mammiferi"

        match animal:
            case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
                habitat = "terra"

            case "balena"|"delfino":
                habitat = "acqua"
            
            case _:
                habitat = "non definito"

    case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
        print(f"{animal} appartiene alla categoria dei Rettili")
        animal_type:str = "Rettili"
        match animal:
            case "serpente"|"lucertola":
                habitat = "terra"
            
            case "tartaruga"|"coccodrillo":
                habitat = "terra e acqua"

    case "aquila" | "pappagallo" | "gufo" | "falco" | "cigno" | "anatra" | "gallina" | "tacchino":
        print(f"{animal} appartiene alla categoria degli Uccelli ")
        animal_type:str = "Uccelli"

        match animal:
            case "aquila"|"pappagallo"|"gufo"|"falco":
                habitat = "aria e terra"
            
            case "cigno"|"anatra":
                habitat = "terra e acqua"

            case "gallina"|"tacchino":
                habitat = "terra"

            case _:
                habitat = "non definito"
    case "squalo" | "trota" | "salmone" | "carpa":
        print(f"{animal} appartiene alla categoria dei Pesci")
        animal_type:str = "Pesci"
        habitat = "acqua"
    case _:
        print(f"Non so dire la categoria dell'animale '{animal}'.")
        animal_type:str = "Unknown"

if ex_habitat in habitat:
    print(f"L'animale {animal} appartiene alla categoria dei {animal_type} e può vivere nell'habitat {ex_habitat}")
else:
    print(f"L'animale {animal} appartiene alla categoria dei {animal_type}, ma non può vivere nell'habitat {ex_habitat}")


