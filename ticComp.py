
import random
from tic import Board, TicTacToe


def play():
    """TIC-TAC-TOE AGAINST DUMB COMPUTER"""

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

    name = input("Enter your name: ")

    board = Board(game_board)
    board.showBoard()

    game = TicTacToe()

    start = random.choice([name, "Computer"])

    while counter <= 8:

        print(f"{start}\'s turn")

        if start == name:
            choice = game.input_move()
            game_board[int(choice)] = game.move

        elif start == "Computer":
            choice = game.random_move()
            game_board[int(choice)] = game.change_move()

        board.showBoard()

        if counter > 3:
            if board.answer() == "Win":
                print(f"{start} Wins")
                break

        if start == name:
            start = "Computer"
        else:
            start = name

        counter += 1
    else:
        print("Draw")


if __name__ == '__main__':
    play()
