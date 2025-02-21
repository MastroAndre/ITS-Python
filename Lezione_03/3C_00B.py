name:str = str(input("Inserire nome: "))
gender:str = str(input("Inserire gender 'f' per femmina, 'm' per maschio: "))
print(f"Name: {name}")
match gender:
    case "f":
        print("Gender: Femmina")
    case "m":
        print("Gender: Maschio")
    case _:
        print("Error: 'gender' not found")
