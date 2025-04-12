import random

class LotteryMachine:
    def __init__(self, items:list):
        self.items = items

    def random_choise(self) -> None:
        win:list = random.choices(self.items, k = 4)
        print(f"Winning ticket: {win}")
        return win

    def display_message(self) -> None:
        print("Any ticket matching the winning 4 items wins a prize")

    def simulate_until_win(self, my_ticket:list) -> int:
        attempts:int = 0
        while True:
            if my_ticket == LotteryMachine.random_choise(self):
                break
            else:
                attempts += 1
        print(f"Attempts: {attempts}")


machine = LotteryMachine([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"])

my_ticket:list = [3, "d", "e", 9]

machine.simulate_until_win(my_ticket)

