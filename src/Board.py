from Square import Square
import pygame as pg

class Board:
    def __init__(self, w=9, h=9):
        self.board = []
        self.width = w
        self.height = h
        
        # Initialize board with 50x50 pixels squares
        for w in range(self.width):
            for h in range(self.height):
                self.board.append(Square(h * 50, w * 50))

    # Get square with 2d indexes
    def get_square_xy(self, i, j):
        return self.board[(i * self.width) + j]

    # Get square with 1d index
    def get_square(self, index):
        return self.board[index]

    # Update square with 1d index
    def update(self, index, val):
        self.get_square(index).update(str(val))

    # Update square with 2d index
    def update_xy(self, i, j, val):
        self.get_square_xy(i, j).update(str(val))

    # Gets the value of the square (number on the cell) using a 1d index
    def get(self, index):
        return int(self.get_square(index).text)

    # Gets the value of the square (number on the cell) using a 2d index
    def get_xy(self, i, j):
        return int(self.get_square_xy(i, j).text)

    def draw(self, window):
        for square in self.board:
            square.draw(window)
