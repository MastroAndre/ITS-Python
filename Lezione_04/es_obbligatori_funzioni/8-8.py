def make_album(artist:str, title:str, songs:int = None):
    album:dict = {"Artista": artist, "Titolo": title, "Numero canzoni": songs}
    return album

i = 0
while i < 3:
    print(make_album(artist=str(input("Iserisci artista: ")), title=str(input("Inserisci titolo: ")), songs=int(input("Inserisci numero canzoni: "))))
    i += 1
