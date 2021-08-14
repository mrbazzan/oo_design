import random


class Die:
    def __init__(self):
        self.sides = 6
        self.value = None
        self.roll()

    def roll(self):
        self.value = random.randint(1, self.sides)

    def get_roll(self):
        return self.value

    def __repr__(self):
        return f"Die({self.value})"


class Dice:
    def __init__(self):
        self.dice = Die(), Die()
        self.dice_value = None

    def roll(self):
        for die in self.dice:
            die.roll()

    def get_roll_tuple(self):
        return tuple([die.get_roll() for die in self.dice])


d = Dice()
print(d.get_roll_tuple())
