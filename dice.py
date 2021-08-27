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

    def match_DIE(self, die):
        return self.match_VALUE(die.value)

    def match_VALUE(self, number):
        equal_set, unequal_set = set(), set()
        for die in self.dice:
            if die.value == number:
                equal_set.add(die)
            else:
                unequal_set.add(die)
        return {'equal-set': equal_set, 'unequal-set': unequal_set}


die_one, die_two, die_three = Die(), Die(), Die()
a = MultiDice([die_one, die_two, die_three])

print(a.match_DIE(die_one))

# print(die_three)
# print(a.get_DICE())
# a.roll()
#
# a.reroll(die_two, die_three)
