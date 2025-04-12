class User:
    def __init__(self, first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self) -> None:
        print(self.first_name, self.last_name, self.age)

    def greet_user(self) -> None:
        print(f"Welcome {self.first_name}!")


mario:User = User("Mario", "Rossi", 25)
giulio:User = User("Giulio", "Bianchi", 42)

mario.describe_user()
mario.greet_user()

giulio.describe_user()
giulio.greet_user()