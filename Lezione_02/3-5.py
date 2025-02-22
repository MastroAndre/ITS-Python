guests:list = ["Jeff Bezos", "Sapobully", "Marco", "Flavio"]
mess:str = "you are invited for dinner."
print(f"Hey {guests[0]}, {mess}")
print(f"Hey {guests[1]}, {mess}")
print(f"Hey {guests[2]}, {mess}")
print(f"Hey {guests[3]}, {mess}")
print(f"{guests[2]} can't come for dinner.")
guests[2] = "Giulio"
print(f"Hey {guests[0]}, {mess}")
print(f"Hey {guests[1]}, {mess}")
print(f"Hey {guests[2]}, {mess}")
print(f"Hey {guests[3]}, {mess}")
