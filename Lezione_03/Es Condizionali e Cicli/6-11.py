cities:dict = {
    "Roma": {
        "Country": "Italia",
        "Population": 3000000,
        "Fact":"Impero Romano"
        },
    "Bangkok": {
        "Country": "Tailandia",
        "Population":40000,
        "Fact": "Non lo so"
        },
    "Santiago":{
        "Country": "Cile",
        "Population": 6300000,
        "Fact": "Ciao"
        }
    }

for city, info in cities.items():
    Country:str = info["Country"]
    Population:int = info["Population"]
    Fact:str = info["Fact"]

print(f"{city} sta in {Country}")
print(f"La popolazione di {city} è di {Population} abitanti")
print(f"In {city} è successo questo fatto: {Fact}")