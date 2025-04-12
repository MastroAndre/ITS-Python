import random

class Die:
    def __init__(self, sides:int = 6):
        self.sides = sides

    def roll_die(self) -> None:
        print(random.randint(1, self.sides))


six:Die = Die()

six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()

ten:Die = Die(10)

ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()

twenty:Die = Die(20)

twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
