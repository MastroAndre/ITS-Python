voto:int = int(input("Inserire un voto: "))
match voto:
    case voto if voto >= 1 and voto <= 3:
        print("Gravemente insufficiente")
    case voto if voto == 4 or voto == 5:
        print("Insufficiente")
    case voto if voto == 6 or voto == 7:
        print("Sufficiente")
    case voto if voto == 8 or voto == 9:
        print("Molto buono")
    case 10:
        print("Eccellente")
    case _:
        print("Voto non valido")