import random

"""ROCK-PAPER-SCISSORS GAME"""


# def play():
#     intro()
#     counter = 0
#     while counter < 5:
#         userPick = input("What do you pick? ").lower()
#         while userPick not in ["rock", "paper", "scissors"]:
#             userPick = input("What do you pick? ").lower()
#         comPick = Player(userPick)
#         print(comPick)
#         gameDecider = comPick.choice()
#         print(gameDecider)
#         counter += 1

# computer is also a player.


class Player:
    def __init__(self, pick):
        self.option = ['rock', 'paper', 'scissors']
        if pick in self.option:
            self.choice = pick

    def return_choice(self):
        return self.choice


class Computer(Player):
    def __init__(self):
        super(Computer, self).__init__(self, )
        self.choice = random.choice(self.option)


class Game:
    def __init__(self, pick):
        self.player = Player(pick).return_choice()
        self.computer = Computer().return_choice()

    def game_play(self):
        if self.computer == self.player:
            return "Draw"

        elif self.computer == "rock":
            if self.player != "paper":
                return "Computer Wins"
            return "Gamer Wins"

        elif self.computer == "paper":
            if self.player != "scissors":
                return "Computer Wins"
            return "Gamer Wins"

        elif self.computer == "scissors":
            if self.player != "rock":
                return "Computer Wins"
            return "Gamer Wins"


def intro():
    print("""To play:
           Enter rock, paper or scissors\n""")


def play():
    # user = input('Enter your name: ')

    user_pick = input('Enter your choice: ').lower()
    while user_pick not in ['rock', 'paper', 'scissors']:
        user_pick = input('Enter your choice: ')

    game = Game(user_pick)
    winner = game.game_play()

    print(f"Computer's choice is {game.computer}")
    print(winner)


if __name__ == '__main__':
    play()
