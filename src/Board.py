from Square import Square
import random

class Board:
    def __init__(self, w=9, h=9):
        self.board = []
        self.width = w
        self.height = h
        
        for w in range(self.width):
            for h in range(self.height):
                self.board.append(Square(h * 50, w * 50))

    def get_square_xy(self, i, j):
        return self.board[(i * self.width) + j]

    def get_square(self, index):
        return self.board[index]

    def update(self, index, val):
        self.get_square(index).update(str(val))

    def update_xy(self, i, j, val):
        self.get_square_xy(i, j).update(str(val))

    def get(self, index):
        return int(self.get_square(index).text)

    def get_xy(self, i, j):
        return int(self.get_square_xy(i, j).text)

    def draw(self, window):
        for square in self.board:
            square.draw(window)