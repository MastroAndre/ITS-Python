class Restaurant:
    def __init__(self, name:str, cuisine_type:str, number_served:int = 0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self) -> None:
        print(f"Name: {self.name}\nCuisine type: {self.cuisine_type}")

    def open_restaurant(self) -> None:
        print(f"{self.name} is Open")
        
    def set_number_served(self, number_served:int) -> None:
        self.number_served = number_served

    def increment_number_served(self, increment:int) -> None:
        self.number_served += increment

    
restaurant:Restaurant = Restaurant("Pizzeria", "pizza")
print(restaurant.number_served)

restaurant.number_served = 50
print(restaurant.number_served)

restaurant.set_number_served(80)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)