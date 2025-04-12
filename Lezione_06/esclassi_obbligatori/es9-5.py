class User:
    def __init__(self, first_name:str, last_name:str, age:int, login_attempts:int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self) -> None:
        print(self.first_name, self.last_name, self.age)

    def greet_user(self) -> None:
        print(f"Welcome {self.first_name}!")

    def increment_login_attempts(self) -> None:
        self.login_attempts += 1

    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

mario:User = User("Mario", "Rossi", 25)

print(mario.login_attempts)

mario.increment_login_attempts()
mario.increment_login_attempts()
mario.increment_login_attempts()
mario.increment_login_attempts()
print(mario.login_attempts)

mario.reset_login_attempts()
print(mario.login_attempts)