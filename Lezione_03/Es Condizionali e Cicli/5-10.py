current_users:list = ["Ale", "Andrea", "Gigi", "Mark", "Franci"]
new_users:list = ["Simon", "Franci", "Giulio", "Alberto", "Ale"]
for i in new_users:
    if i in current_users:
        print(f"{i} You need to enter a new username")
    else:
        print(f"Username '{i}' is avaible")