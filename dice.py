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


class MultiDice:
    def __init__(self, dice):
        self.dice = frozenset(dice)

    def roll(self):
        for die in self.dice:
            die.roll()

    def get_DICE(self):
        return [die.get_roll() for die in self.dice]

    def re_roll(self, *dice):
        for die in dice:
            if die in self.dice:
                die.roll()

    def score(self):
        pass
