
# OO Design

    Designs built with OOP programming
   
Using **Object Oriented Programming** to build:
    
- rpscissors.py -------------- Rock, Paper, Scissors game

    ![example](/assets/rps.gif)

- ticComp.py ---------------- Tic-Tac-Toe against Computer(Dumb)
    
    ![example](/assets/comp.gif)

- ticHuman.py --------------- Tic-Tac-Toe against Human
    
    ![example](/assets/human.gif)

- dice.py ------------------- MultiDice games

- stock.py ------------------ Stock Valuation 
    
    `A Block of stock has a number of attributes, including a purchase price, purchase date, and number of
    shares. Commonly, methods are needed to compute the total spent to buy the stock, and the current value
    of the stock. A Position is the current ownership of a company reflected by all of the blocks of stock. A
    Portfolio is a collection of Positions ; it has methods to compute the total value of all Blocks of stock.`
    
    `When we purchase stocks a little at a time, each Block has a different price. We want to compute the total
    value of the entire set of Block s, plus an average purchase price for the set of Blocks.`

- dive_logging.py ---------------- Dive Logging and Surface Air Consumption Rate
    
    `The Surface Air Consumption Rate is used by SCUBA divers to predict the air consumption at a particular depth.`

- rational_number.py ---------------- Rational Numbers

    `A class that saves a rational number and perform arithmetic operations on this number or between two rational numbers.
    The values are returned in proper fraction form e.g 4/5, 6/7 et. c.`


- card.py ---------------- Playing Cards and Deck

    `A class that saves a card(rank: ace to king; suit: clubs to spades). There is also a deck class from which the card
    is shuffled and dealt.
    This cards can be manipulated to play games such as blackjack, poker et.c .`

## NOTES

- When defining new instance variable in a subclass, it must start out doing everything the superclass does.
  
  `super()` is used to achieve this others:
  
  i) Locates the superclass and then binds the given variables to create a superclass.
  
  ii) It is used to call a superclass within a subclass.
 
 The python code below explains it further;

```pythonstub
class Play:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.choice = None

    def return_choice(self):
        return self.choice


class Player(Play):
    def __init__(self, name, pick):
        print('Initial: ', self.__dict__)
        super(Player, self).__init__()
        print('Immediately after super: ', self.__dict__)
        self.choice = pick
        self.name = name
        print('After new instantiation: ', self.__dict__)
```

Printing out `Player` shows;

![Show-Picture](/assets/show-details.PNG)

This tells us that `super(Player, self).__init__()` calls the `__init__` method of the superclass, and it then gets updated with the new instance variable.