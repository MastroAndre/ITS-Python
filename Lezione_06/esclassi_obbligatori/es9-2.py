class Restaurant:
    def __init__(self, name:str, cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f"Name: {self.name}\nCuisine type: {self.cuisine_type}")

    def open_restaurant(self) -> None:
        print(f"{self.name} is Open")


sushi:Restaurant = Restaurant("Rist1", "sushi")
pizzeria:Restaurant = Restaurant("Rist2", "pizza")
ristorante:Restaurant = Restaurant("Rist3", "pesce")

sushi.describe_restaurant()
pizzeria.describe_restaurant()
ristorante.describe_restaurant()