
import random

"""ROCK-PAPER-SCISSORS GAME"""


class Player:

    def __init__(self, user):
        value = ["rock", "paper", "scissors"]
        self.user = user
        self.comp = random.choice(value)

    def choice(self):
        if self.comp == self.user:
            return "Draw"

        elif self.comp == "rock":
            if self.user != "paper":
                return "Computer Wins"
            return "Gamer Wins"

        elif self.comp == "paper":
            if self.user != "scissors":
                return "Computer Wins"
            return "Gamer Wins"

        elif self.comp == "scissors":
            if self.user != "rock":
                return "Computer Wins"
            return "Gamer Wins"

    def __str__(self):
        return f"User's choice is {self.user}, while computer's choice is {self.comp}"


def intro():
    print("""To play:
           Enter rock, paper or scissors""")
    print()


def play():
    intro()
    counter = 0
    while counter < 5:
        userPick = input("What do you pick? ").lower()
        while userPick not in ["rock", "paper", "scissors"]:
            userPick = input("What do you pick? ").lower()
        comPick = Player(userPick)
        print(comPick)
        gameDecider = comPick.choice()
        print(gameDecider)
        counter += 1


if __name__ == '__main__':
    play()
