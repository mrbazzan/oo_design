
from card import BlackJack, Deck, Hand


def card():
    return BlackJack(*next(shuffled_deck))


def blackjack_one(h):
    print('HAND: ', h)
    while h.soft_total() <= 16:
        h.add(card())
        print('Adding Card: ', h)
    
        if h.soft_total() in range(17, 22) or h.hard_total() in range(17, 22):
            print('Soft and Hard between 17–21: ', h)
            break
        if h.soft_total() >= 21 and h.hard_total() <= 16:
            print('Hard <= 16 and Soft > 21: ', h)
            h.add(card())


def blackjack_two(h):
    print('Hand: ', h)
    while h.soft_total() <= 21 and h.hard_total() <= 21:
        h.add(card())
        print('Adding Card: ', h)


deck = Deck()
shuffled_deck = deck.deal()

first_card, second_card = card(), card()
hand = Hand(first_card, second_card)

# blackjack_one(hand)
# blackjack_two(hand)
