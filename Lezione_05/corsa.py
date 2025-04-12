import random

#Funzione che mostra le posizioni della gara
def displayPos(pos_tartaruga:int, pos_lepre:int) -> None:
    percorso:list[str] = ["_"] * 70

    if pos_lepre == pos_tartaruga:
        percorso[pos_tartaruga - 1] = "OUCH"
    else:
        percorso[pos_tartaruga - 1] = "T"
        percorso[pos_lepre - 1] = "H"

    print(*percorso)


#Funzione che muove la tartaruga
def tartaruga(p:int) -> int:

    i = random.randint(1, 10)

    if 1 <= i <= 5:
        p += 3
    elif 6 <= i <= 7:
        p -= 6
    else:
        p += 1
    
    if p < 1:
        return 1
    elif p > 70:
        return 70
    else:
        return p


#Funzione che muove la lepre
def lepre(p:int) -> int:

    i = random.randint(1, 10)

    if 1 <= i <= 2:
        p = p
    elif 3 <= i <= 4:
        p += 9
    elif i == 5:
        p -= 12
    elif 6 <= i <= 8:
        p += 1
    else:
        p -= 2
    
    if p < 1:
        return 1
    elif p > 70:
        return 70
    else:
        return p


#Svolgimento della gara
print("BANG!!! AND THEY ARE OFF!!!")

pos_tartaruga:int = 1
pos_lepre:int = 1

while True:
    
    #Muove tartaruga e lepre e mostra le posizioni
    pos_tartaruga = tartaruga(pos_tartaruga)
    pos_lepre = lepre(pos_lepre)
    displayPos(pos_tartaruga, pos_lepre)

    #Se uno dei due arriva o va oltre 70 vince
    #Se arrivano entrambi pareggio
    if pos_tartaruga >= 70 and pos_lepre >= 70:
        print("IT'S A TIE.")
        break
    elif pos_lepre >= 70:
        print("HARE WINS || YUCH!!!")
        break
    elif pos_tartaruga >= 70:
        print("TORTOISE WINS! || VAY!!!")
        break