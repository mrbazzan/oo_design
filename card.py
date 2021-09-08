
import random


# A card has a rank—ace, two to ten, jack, queen and king—and a suit—clubs, diamonds, hearts, spades.


class Card:
    rank_converter = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{}{}".format(self.rank_converter[self.rank] if self.rank in self.rank_converter else self.rank,
                             self.suit)

    def __eq__(self, other):
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False

    def __ne__(self, other):
        if self.rank != other.rank and self.suit != other.suit:
            return True
        return False

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            if self.suit < other.suit:
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        if self.rank > other.rank:
            return False
        return True

    def __gt__(self, other):
        if self.rank <= other.rank:
            return False
        return True

    def __ge__(self, other):
        if self.rank < other.rank:
            return False
        return True


class Deck:
    def __init__(self):
        self.deck = [str(rank) + suit for suit in ('C', 'D', 'H', 'S') for rank in range(1, 14)]

    def deal(self):
        random.shuffle(self.deck)
        for card in self.deck:
            yield card


class BlackJack(Card):
    # cards in blackjack have a point value.
    # Aces are 1 point(i.e total is called `hard total`) or 11 points(i.e soft total).
    def get_hard_value(self):
        if self.rank in (11, 12, 13):
            return 10
        return self.rank

    def get_soft_value(self):
        if self.rank == 1:
            return 11
        elif self.rank in (11, 12, 13):
            return 10
        return self.rank
