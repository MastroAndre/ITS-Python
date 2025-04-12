import random

class LotteryMachine:
    def __init__(self, items:list):
        self.items = items

    def random_choise(self) -> None:
        print(f"Winning ticket: {random.choices(self.items, k = 4)}")

    def display_message(self) -> None:
        print("any ticket matching the winning 4 items wins a prize")


machine = LotteryMachine([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"])

machine.random_choise()
machine.display_message()