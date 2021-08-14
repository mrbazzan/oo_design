
import random


class Play:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.choice = None

    def return_choice(self):
        return self.choice


class Player(Play):
    def __init__(self, name, pick):
        super(Player, self).__init__()
        self.choice = pick
        self.name = name


class Computer(Play):
    def __init__(self):
        super(Computer, self).__init__()
        self.choice = random.choice(self.options)


class Game:

    """ROCK-PAPER-SCISSORS GAME PLAY"""

    def __init__(self):
        self.computer = Computer()
        self.comp_choice = self.computer.return_choice()

    def game_play(self, player):
        player_choice = player.return_choice()
        name = player.name
        if self.comp_choice == player_choice:
            return "Draw"

        elif self.comp_choice == "rock":
            if player_choice != "paper":
                return "Computer Wins"
            return f"{name} Wins"

        elif self.comp_choice == "paper":
            if player_choice != "scissors":
                return "Computer Wins"
            return f"{name} Wins"

        elif self.comp_choice == "scissors":
            if player_choice != "rock":
                return "Computer Wins"
            return f"{name} Wins"


def play():
    print("""To play:
               Enter rock, paper or scissors\n""")

    user = input('Enter your name: ')
    count = 0
    while count < 5:
        user_pick = input('Enter your choice: ').lower()
        while user_pick not in ['rock', 'paper', 'scissors']:
            user_pick = input('Enter your choice: ')

        player = Player(user, user_pick)
        game = Game()
        winner = game.game_play(player)

        print(f"Computer's choice is {game.computer.choice}")
        print(winner + '\n')
        count += 1


if __name__ == '__main__':
    play()
