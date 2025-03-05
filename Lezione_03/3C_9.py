x:int = int(input("Inserisci coordinata X: "))
y:int = int(input("Inserisci coordinata Y: "))
point:tuple = (x, y)

match point:
    case (0, 0):
        print("Il punto si trova nell'origine")
    
    case (x, 0):
        print("Il punto si trova sull'asse x")

    case (0, y):
        print("Il punto si trova sull'asse y")
    
    case point if x > 0 and y > 0:
        print(f"Il punto {point} si trova nel primo quadrante")

    case point if x < 0 and y > 0:
        print(f"Il punto {point} si trova nel secondo quadrante")
    
    case point if x < 0 and y < 0:
        print(f"Il punto {point} si trova nel terzo quadrante")

    case point if x > 0 and y < 0:
        print(f"Il punto {point} si trova nel quarto quadrante")