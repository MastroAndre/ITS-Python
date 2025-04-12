def make_car(marca:str, modello:str, **kwargs):
    car:dict = {"Marca": marca, "Modello": modello}

    for key, value in kwargs.items():
        car[key] = value
    
    print(car)

make_car("Fiat", "Panda", color = "blue", brakes = False)
