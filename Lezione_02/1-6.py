menu:dict = {"Pizza": 9.00, "Pasta": 10.50, "Hamburger": 15.50, "Cotoletta": 10.00, "Patatine fritte": 5.50, "Verdure del giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Acqua": 1.50, "Vino": 5.00}
ordine:dict = {"Pasta", "Cotoletta", "Patatine fritte", "Tiramisu", "Acqua"}
totale:float = (menu["Pasta"]) + (menu["Cotoletta"]) + (menu["Patatine fritte"]) + (menu["Tiramisu"]) + (menu["Acqua"])
print("{:.2f}".format(totale))