print("Inserisci risultato moneta 't' testa e 'c' croce")
i:int = 1
testa:int = 0
croce:int = 0
not_valid:int = 0

for i in range(8):
    moneta:str = str(input(f"Lancio {i + 1}: "))
    match moneta:
        case "t"|"T":
            testa += 1
        
        case "c"|"C":
            croce +=1
        
        case _:
            not_valid += 1
            print("Scelta non valida")

percentuale_testa:float = (testa * 100) / (8 - not_valid)
percentuale_croce:float = (croce * 100) / (8 - not_valid)

print(f"\nLanci validi: {8 - not_valid}")
print(f"\nTotale 'testa': {testa}")
print(f"Percentuale 'testa': {percentuale_testa:.2f}%")
print(f"\nTotale 'croce': {croce}")
print(f"Percentuale 'croce': {percentuale_croce:.2f}%")