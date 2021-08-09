
"""TIC-TAC-TOE AGAINST DUMB COMPUTER"""


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
    # start = random.choice([baz.name, baz.move])

    def __init__(self, myName="Gamer"):
        self.name = myName

    def changeMove(self):
        if self.move == "O":
            self.move = "X"
            return self.move
        else:
            self.move = "O"
            return self.move

    # def changeName(self):
    #     if start == baz.name:
    #         start = baz.move
    #     else:
    #         start = baz.name


class Comp:

    def __init__(self):
        self.name = "Computer"

    @staticmethod
    def compMove(move):
        if move == "O":
            move = "X"
            return move
        else:
            move = "O"
            return move


class Move:
    def __init__(self, enter_value):
        self.value = enter_value

    def inputMove(self):
        choose = input("Enter your move: ")
        while choose not in self.value:
            choose = input("Enter your move: ")
        if choose in self.value:
            self.value.remove(choose)
        return choose

    def randomMove(self):
        myChoice = random.choice(self.value)
        while myChoice not in self.value:
            myChoice = random.choice(self.value)
        if myChoice in self.value:
            self.value.remove(myChoice)
        return myChoice


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
    name = input("Enter your name: ")
    Board(gameBoard).showBoard()

    baz = Player(name)
    comp = Comp()
    start = random.choice([baz.name, comp.name])

    while counter <= 8:

        print(f"{start}\'s turn")

        if start == baz.name:
            choice = Move(value).inputMove()
            gameBoard[int(choice)] = baz.move

        elif start == comp.name:
            newChoice = Move(value).randomMove()
            gameBoard[int(newChoice)] = comp.compMove(baz.move)

        Board(gameBoard).showBoard()

        if Board(gameBoard).answer() == "Win":
            print(f"{start} Wins")
            break
        else:
            if start == baz.name:
                start = comp.name
            else:
                start = baz.name

        counter += 1
    else:
        print("Draw")


if __name__ == '__main__':
    play()
