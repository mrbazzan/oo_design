
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
        self.deck = [(rank, suit) for suit in ('C', 'D', 'H', 'S') for rank in range(1, 14)]

    def deal(self):
        for card in self.deck:
            yield card


# cards in blackjack have a point value.
# Aces are 1 point(i.e total is called `hard total`) or 11 points(i.e soft total).
class BlackJack(Card):
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


# Scoring Blackjack
# The objective of blackjack is to accumulate HAND with <= 21 points.
class Hand:
    def __init__(self, *cards):
        self.cards = list(cards[:2])

    def __str__(self):
        return ','.join(map(str, self.cards))

    def hard_total(self):
        return sum([card.get_hard_value() for card in self.cards])

    # def soft_total(self):
    #     soft_set = []
    #     cards = self.cards
    #     for card in cards:
    #         if card.get_soft_value() != card.get_hard_value():
    #             soft_set = card
    #             break
    #
    #     if not soft_set:
    #         return self.hard_total()
    #
    #     cards.remove(soft_set)
    #     return soft_set.get_soft_value() + sum(card.get_hard_value() for card in cards)

    def soft_total(self):
        ace = [(True, card) if card.rank == 1 else (False, card) for card in sorted(self.cards, key=lambda x: x.rank)]
        condition, cards = list(zip(*ace))

        if not any(condition):
            return self.hard_total()

        return cards[0].get_soft_value() + sum(card.get_hard_value() for card in cards[1:])

    def add(self, card):
        self.cards.append(card)


class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.rankCount = {}

    def straight_flush(self):
        if self.flush() and self.straight():
            return True
        return False

    def four_of_a_kind(self):
        if self.matches() == (1, 4):
            return True
        return False

    def matches(self):
        self.rankCount = {}
        for card in self.cards:
            if card.rank not in self.rankCount:
                self.rankCount[card.rank] = 1
            else:
                self.rankCount[card.rank] += 1

        return tuple(sorted(self.rankCount.values()))

    def full_house(self):
        if self.matches() == (2, 3):
            return True
        return False

    def straight(self):
        self.sort_by_rank()

        for card in range(len(self.cards) - 1):
            if self.cards[card].rank == 1 and self.cards[card + 1].rank == 10:
                continue
            if (self.cards[card].rank + 1) != self.cards[card + 1].rank:
                return False
        return True

    def flush(self):
        for card in range(len(self.cards) - 1):
            if self.cards[card].suit != self.cards[card + 1].suit:
                return False
        return True

    def three_of_a_kind(self):
        if self.matches() == (1, 1, 3):
            return True
        return False

    def high_card(self):
        return max(self.cards, key=lambda x: x.rank)

    def pair(self):
        if len(self.matches()) == 4:
            return True
        return False

    def two_pair(self):
        if self.matches() == (1, 2, 2):
            return True
        return False

    def sort_by_rank(self):
        self.cards = sorted(self.cards, key=lambda x: x.rank)

    def sort_by_match(self):
        for card in self.cards:
            card.match_count = self.rankCount[card.rank]

        self.cards = sorted(self.cards, key=lambda x: x.match_count)

    def sort_by_match_and_rank(self):
        for card in self.cards:
            card.match_count = self.rankCount[card.rank]

        self.cards = sorted(self.cards, key=lambda x: (x.match_count, x.rank))
