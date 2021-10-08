
import random
import time
from card import Deck


class ExchangeDeck(Deck):
    def shuffle(self):
        for i in range(len(self.deck)):
            r = random.randrange(0, len(self.deck))
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def __str__(self):
        return 'ExchangeDeck'


class BuildDeck(Deck):
    def shuffle(self):
        s = []
        while self.deck:
            r = random.randrange(0, len(self.deck))
            s.append(self.deck.pop(r))
        self.deck = s

    def __str__(self):
        return 'BuildDeck'


class SortDeck(Deck):
    def shuffle(self):
        length = len(self.deck)
        self.deck.sort(key=lambda x: random.randrange(0, length))

    # TODO: Find the difference between .sort() and sorted().
    def __str__(self):
        return 'SortDeck'


class RandomShuffleDeck(Deck):
    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return 'RandomShuffleDeck'


d1 = ExchangeDeck()
d2 = BuildDeck()
d3 = SortDeck()
d4 = RandomShuffleDeck()

time_range = []

for deck in (d1, d2, d3, d4):
    start = time.time()
    for _ in range(100):
        deck.shuffle()
    finish = time.time()
    print(f"Time for {deck} is: ", finish-start)
    time_range.append(finish-start)

print('Fastest: ', min(time_range))
