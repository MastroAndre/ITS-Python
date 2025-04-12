cubes:list = []
for i in range(1, 11):
    cubes.append(i**3)

print(f"The first three items in the list are {cubes[1:3]}")
print(f"Three items from the middle of the list are {cubes[4:7]}")
print(f"The last three items in the list are {cubes[-3:11]}")