import sys
sys.path.append('../src')

import pygame as pg
from Board import Board
from Square import Square

import numpy

pg.init()

screen_width = 450
screen_height = 450

class Solver:
    def __init__(self):
        self.board = Board()
        self.index = 0
        self.invalid = False # the board can be solved
        self.square_complete = True
        self.blanks = [] # stack; contains the index of squares to be worked on
        # populate board
        
        for i in range(81):
            s = str(numpy.random.choice(numpy.arange(0, 10), p=[0.7,0.02,0.02,0.02,0.02,0.02,0.1,0.05,0.025,0.025]))
            if s != '0':
                self.board.update(i, s)
    def step(self): # perform next step in the solution
        # if the current square is complete, search for the next blank space
        if self.square_complete:
            while self.index < 81:
                val = self.board.get(self.index)
                if val == 0:
                    # once found add the index into
                    # ...the stack and turn square_complete to False
                    self.blank.append(self.index)
                    square_complete = False
                    break
                self.index += 1
        else:
            val = self.board.get(self.index)
            # if it is unique 
            if self.is_valid_square(self.index):
                # set square_complete to true
                square_complete = True
            elif val == 9:
                if not self.blanks:
                    self.invalid == True
                else:
                    self.index = self.blank.pop()
            else:
                # set blank and go to the previous index in the stack (pop from the stack)
                self.board.update(self.index, str(val + 1))

    def is_valid_square(self, i):
        if self.board.get(i) == 0:
            return False
        pass

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

        if not solver.solved():
            solver.step()

        solver.draw(window)
        pg.display.update()
        pg.time.delay(int(150 * 1.5))

main()