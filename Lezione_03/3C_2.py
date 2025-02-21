voto:int = int(input("Inserisci voto: "))
match voto:
    case voto if voto >= 66 and voto <= 69:
        print("GPA: 1.0")
    case voto if voto >= 70 and voto <= 75:
        print("GPA: 1.7")
    case voto if voto >= 76 and voto <= 80:
        print("GPA: 2.0")
    case voto if voto >= 81 and voto <= 85:
        print("GPA: 2.3")
    case voto if 86<= voto <= 90:
        print("GPA: 2.7")
    case voto if 91 <= voto <= 95:
        print("GPA: 3.0")
    case voto if 96 <= voto <= 100:
        print("GPA: 3.3")
    case voto if 101 <= voto <= 105:
        print("GPA: 3.7")
    case voto if 106 <= voto <= 110:
        print("GPA: 4.0")
    case _:
        print("Voto non valido")