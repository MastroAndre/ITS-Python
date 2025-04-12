person_1:dict = {"first_name": "Andrea", "last_name": "Rossi", "age": 19, "city": "Bologna"}
person_2:dict = {"first_name": "Tony", "last_name": "Effe", "age": 30, "city": "Rome"}
person_3:dict = {"first_name": "Giorgio", "last_name": "Franco", "age": 6, "city": "Milano"}

people:list = [person_1, person_2, person_3]

for p in people:
    for i in p:
        print(f"{i} --> {p[i]}")
    print("\n")