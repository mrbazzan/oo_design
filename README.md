
# OO Design

    Designs built with OOP programming
   
Using **Object Oriented Programming** to build:
    
- rpscissors.py -------------- Rock, Paper, Scissors game

    ![example](/assets/rps.gif)

- ticComp.py ---------------- Tic-Tac-Toe against Computer(Dumb)
    
    ![example](/assets/comp.gif)

- ticHuman.py --------------- Tic-Tac-Toe against Human
    
    ![example](/assets/human.gif)

- stock.py ------------------ Stock Valuation 
    
    `A Block of stock has a number of attributes, including a purchase price, purchase date, and number of
    shares. Commonly, methods are needed to compute the total spent to buy the stock, and the current value
    of the stock. A Position is the current ownership of a company reflected by all of the blocks of stock. A
    Portfolio is a collection of Positions ; it has methods to compute the total value of all Blocks of stock.`
    
    `When we purchase stocks a little at a time, each Block has a different price. We want to compute the total
    value of the entire set of Block s, plus an average purchase price for the set of Blocks.`

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