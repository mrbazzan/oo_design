
import random
from tic import Board, TicTacToe


def play():

    """TIC-TAC-TOE AGAINST HUMAN"""

    intro_board = {
        1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6",
        7: "7", 8: "8", 9: "9"
    }

    game_board = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }

    Board(intro_board).showBoard()

    counter = 0

    player_one = input("Enter your name(PLAYER 1): ")
    player_two = input("Enter your name(PLAYER 2): ")

    board = Board(game_board)
    board.showBoard()

    game = TicTacToe()

    start = random.choice([player_one, player_two])

    while counter <= 8:
        print(f"{start}\'s turn")

        choice = game.input_move()

        game_board[int(choice)] = game.move
        game.move = game.change_move()

        board.showBoard()

        if counter > 3:
            if board.answer() == "Win":
                print(f"{start} Wins")
                return

        if start == player_one:
            start = player_two
        else:
            start = player_one

        counter += 1
    else:
        print("Draw")


if __name__ == '__main__':
    play()

"""CC: AUTOMATE THE BORING STUFF WITH PYTHON """
