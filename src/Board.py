from Square import Square
import random

class Board:
    def __init__(self):
        self.board = []
        k = 0
        for i in range(9):
            for j in range(9):
                self.board.append(Square(i * 50, j * 50))
                k += 1

    def update(self, index, val):
        self.board[index].update(str(val))

    def update_xy(self, i, j, val):
        self.board[(i * 9) + j].update(str(val))

    def get(self, index):
        return int(self.board[index])

    def get_xy(self, i, j):
        return int(self.board[(i * 9) + j])

    def draw(self, window):
        for square in self.board:
            square.draw(window)