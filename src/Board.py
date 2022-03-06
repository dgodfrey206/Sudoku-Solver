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
    def update(self, i, val):
        self.board[i].update(val)
    def get(self, i):
        return int(self.board[i])
    def draw(self, window):
        for square in self.board:
            square.draw(window)