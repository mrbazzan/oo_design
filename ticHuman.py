
"""TIC-TAC-TOE AGAINST HUMAN"""

import random


class Board:

    def __init__(self, board):
        self.board = board

    def showBoard(self):
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-+-+- ")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-+-+- ")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print()

    def answer(self):
        answerList = ((1, 2, 3), (4, 5, 6), (3, 6, 9), (7, 8, 9), (2, 5, 8), (1, 4, 7), (3, 5, 7), (1, 5, 9))
        while True:
            for anyValue in answerList:
                if self.board[anyValue[0]] == self.board[anyValue[1]] == self.board[anyValue[2]] == "X":
                    return "Win"
                elif self.board[anyValue[0]] == self.board[anyValue[1]] == self.board[anyValue[2]] == "O":
                    return "Win"
            return


class Player:
    move = random.choice(["O", "X"])

    def __init__(self, name="Computer"):
        self.name = name

    def changeMove(self):
        if self.move == "O":
            self.move = "X"
            return self.move
        else:
            self.move = "O"
            return self.move


def intro():
    dictBoard = {
        1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6",
        7: "7", 8: "8", 9: "9"
    }
    Board(dictBoard).showBoard()


def play():
    intro()
    gameBoard = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }
    counter = 0
    value = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    playerOne = input("Enter your name(PLAYER 1): ")
    playerTwo = input("Enter your name(PLAYER 2): ")
    Board(gameBoard).showBoard()
    baz = Player(playerOne)
    ply = Player(playerTwo)
    start = random.choice([baz.name, ply.name])
    while counter <= 8:

        print(f"{start}\'s turn")
        choice = input("Enter your move: ")

        while choice not in value:
            choice = input("Enter your move: ")

        if choice in value:
            value.remove(choice)

        gameBoard[int(choice)] = baz.move
        baz.changeMove()

        Board(gameBoard).showBoard()

        if Board(gameBoard).answer() == "Win":
            print(f"{start} Wins")
            return
        else:
            if start == baz.name:
                start = ply.name
            else:
                start = baz.name

        counter += 1
    else:
        print("Draw")


if __name__ == '__main__':
    play()

"""CC: AUTOMATE THE BORING STUFF WITH PYTHON """
