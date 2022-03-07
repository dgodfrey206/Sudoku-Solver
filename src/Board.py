from Square import Square
import random

class Board:
    def __init__(self):
        self.board = []
        self.width = 9
        self.height = 9
        
        for w in range(self.width):
            for h in range(self.height):
                self.board.append(Square(h * 50, w * 50))

    def update(self, index, val):
        self.board[index].update(str(val))

    def update_xy(self, i, j, val):
        self.board[(i * self.width) + j].update(str(val))

    def get(self, index):
        return int(self.board[index].text)

    def get_xy(self, i, j):
        return int(self.board[(i * self.width) + j].text)

    def draw(self, window):
        for square in self.board:
            square.draw(window)