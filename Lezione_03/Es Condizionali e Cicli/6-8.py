pet1:dict = {"kind": "Dog", "owner": "Andrea"}
pet2:dict = {"kind": "Cat", "owner": "Giorgio"}
pet3:dict = {"kind": "Tiger", "owner": "Tony"}

pets:list = [pet1, pet2, pet3]

for p in pets:
    for i in p:
        print(f"{i}: {p[i]}")
    print("\n")
