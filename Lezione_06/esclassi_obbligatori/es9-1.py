class Restaurant:
    def __init__(self, name:str, cuisine_type:str):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f"Name: {self.name}\nCuisine type: {self.cuisine_type}")

    def open_restaurant(self) -> None:
        print(f"{self.name} is Open")

    
restaurant:Restaurant = Restaurant("Pizzeria", "pizza")

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

