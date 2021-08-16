
import random

"""TIC-TAC-TOE"""


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
        answer_list = ((1, 2, 3), (4, 5, 6), (3, 6, 9), (7, 8, 9), (2, 5, 8), (1, 4, 7), (3, 5, 7), (1, 5, 9))
        while True:
            for anyValue in answer_list:
                if self.board[anyValue[0]] == self.board[anyValue[1]] == self.board[anyValue[2]] == "X":
                    return "Win"
                elif self.board[anyValue[0]] == self.board[anyValue[1]] == self.board[anyValue[2]] == "O":
                    return "Win"
            return


class TicTacToe:
    def __init__(self, move=None):
        self.possible_choice = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.move = move or random.choice(['X', 'O'])

    def change_move(self):
        if self.move == "O":
            return 'X'
        else:
            return "O"

    def input_move(self):
        choose = input("Enter your move: ")
        while choose not in self.possible_choice:
            choose = input("Enter your move: ")

        self.possible_choice.remove(choose)
        return choose

    def random_move(self):
        choose = random.choice(self.possible_choice)
        while choose not in self.possible_choice:
            choose = random.choice(self.possible_choice)

        self.possible_choice.remove(choose)
        return choose
