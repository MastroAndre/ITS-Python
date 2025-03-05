day:int = int(input("Inserire il giorno: "))
month:int = int(input("Inserire il mese: "))
date:tuple = (day, month)
festa:str = ""

match date:
    case (1, 1):
        festa = "Capodanno"
    case (14, 2):
        festa = "San valentino"
    case (2, 6):
        festa = "Festa della Repubblica Italiana"
    case (15, 8):
        festa = "Ferragosto"
    case (31, 10):
        festa = "Halloween"
    case (25, 12):
        festa = "Natale"
    case _:
        print(f"Nessuna festività importante il giorno {day}/{month}")
    
if festa != "":
    print(f"Il giorno {day}/{month} è {festa}")