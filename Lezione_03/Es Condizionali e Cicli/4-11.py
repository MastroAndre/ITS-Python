pizze:list = ["margherita", "boscaiola", "crostino"]
friend_pizzas:list = ["margherita", "boscaiola", "crostino"]

pizze.append("marinara")
friend_pizzas.append("4 formaggi")

print("My favourite pizzas are:")
for i in pizze:
    print(i)

print("My friend's favourite pizzas are:")
for p in friend_pizzas:
    print(p)