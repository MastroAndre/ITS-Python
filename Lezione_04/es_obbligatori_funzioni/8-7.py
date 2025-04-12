def make_album(artist:str, title:str, songs:int = None):
    album:dict = {"Artista": artist, "Titolo": title, "Numero canzoni": songs}
    print(album)

make_album("Giorgio", "WOW")
make_album("Pierpaolo", "No vabbè", 12)
make_album("Big G", "Raffreddore", 9)
