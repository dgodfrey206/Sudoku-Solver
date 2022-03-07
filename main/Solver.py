from math import fabs
import sys
sys.path.append('../src')

import pygame as pg
from Board import Board
from Square import Square

import numpy

pg.init()

screen_width = 450
screen_height = 450

example_board = [  0,6,9,8,0,0,0,0,0,
                   3,0,4,7,0,6,5,0,0,
                   2,0,0,5,9,0,6,0,0,
                   0,2,0,0,0,0,0,1,0,
                   9,0,0,1,0,7,0,0,8,
                   0,3,0,0,0,0,0,4,0,
                   0,0,2,0,5,4,0,0,7,
                   0,0,3,2,0,1,4,0,5,
                   0,0,0,0,0,9,2,6,0]

class Solver:
    def __init__(self):
        self.board = Board()
        self.index = 0
        self.invalid = False # the board can be solved
        self.square_complete = True
        self.blanks = [] # stack; contains the index of squares to be worked on
        # populate board
        
        for i in range(81):
            self.board.update(i, example_board[i])
    def step(self): # perform next step in the solution
        # if the current square is complete, search for the next blank space
        if self.square_complete:
            while self.index < 81:
                val = self.board.get(self.index)
                if val == 0:
                    # this is a square we need to work on, so turn square_complete to False
                    square_complete = False
                    break
                self.index += 1
        else:
            val = self.board.get(self.index)
            # if it is unique 
            if self.is_valid_square(self.index):
                # set square_complete to true
                square_complete = True
                # add to the stack to come back to later if needed
                self.blank.append(self.index)
            elif val == 9:
                if not self.blanks:
                    self.invalid == True
                else:
                    self.index = self.blank.pop()
            else:
                # set blank and go to the previous index in the stack (pop from the stack)
                self.board.update(self.index, val + 1)

    def is_valid_square(self, index):
        if self.board.get(index) == 0:
            return False
        value = self.board.get(index)

        row = index / 9
        col = index % 9
        
        for i in range(9):
            if i != col and value == self.board.get_xy(row, i):
                return False
            if i != col and value == self.board.get_xy(i, col):
                return False

        if row < 3:
            if col < 3:
                for i in range(3):
                    for j in range(3, 6):
                        if value == self.board.get_xy(i, j):
                            return False
            if col < 6:
                for i in range(3):
                    for j in range(6, 3):
                        if value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(3):
                    for j in range(6, 9):
                        if value == self.board.get_xy(i, j):
                            return False
        if row < 6:
            if col < 3:
                for i in range(3, 6):
                    for j in range(0, 3):
                        if value == self.board.get_xy(i, j):
                            return False
            if col < 6:
                for i in range(3, 6):
                    for j in range(3, 6):
                        if value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(3, 6):
                    for j in range(6, 3):
                        if value == self.board.get_xy(i, j):
                            return False
        else:
            if col < 3:
                for i in range(6, 9):
                    for j in range(0, 3):
                        if value == self.board.get_xy(i, j):
                            return False
            if col < 6:
                for i in range(6, 9):
                    for j in range(3, 6):
                        if value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(6, 9):
                    for j in range(6, 9):
                        if value == self.board.get_xy(i, j):
                            return False
        return True

    def draw(self, window):
        self.board.draw(window)

    def solved(self):
        return not self.invalid and self.index >= 81

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Sudoku Solver')
clock = pg.time.Clock()

def main():
    solver = Solver()
    board = Board()
    run = True
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                run = False

        window.fill(pg.Color('white'))

        #if not solver.solved():
        #    solver.step()

        solver.draw(window)
        pg.display.update()
        pg.time.delay(int(150))

main()