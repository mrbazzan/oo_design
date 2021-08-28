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

    def n_of_a_kind(self, n):
        for die in self.dice:
            if len(self.match_DIE(die)['equal-set']) == n:
                return die
        return None

    def large_straight(self):
        arranged_dice = sorted(self.get_DICE())

        for i in range(len(arranged_dice)-1):
            if arranged_dice[i] + 1 != arranged_dice[i+1]:
                return False
        return True

    def small_straight(self):
        pass

    def chance(self):
        return sum(self.get_DICE())
