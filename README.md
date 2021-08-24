
# OO Design

    Games built with OOP programming
   
Using **Object Oriented Programming** to build:
    
- rpscissors.py -------------- Rock, Paper, Scissors game

    ![example](/assets/rps.gif)

- ticComp.py ---------------- Tic-Tac-Toe against Computer(Dumb)
    
    ![example](/assets/comp.gif)

- ticHuman.py --------------- Tic-Tac-Toe against Human
    
    ![example](/assets/human.gif)
    

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