import pygame as pg
import sys
sys.path.append('../src')

from Solver import Solver

pg.init()

screen_width = 450
screen_height = 450

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Sudoku Solver')
clock = pg.time.Clock()

# The following are boards used for presentation and debugging. They are both solvable
ex1 = [
    5,0,1,6,0,7,9,0,0,
    0,0,9,0,0,3,2,5,0,
    8,2,7,0,9,0,0,0,0,
    9,0,2,0,5,1,3,7,0,
    3,0,0,9,8,0,0,0,0,
    0,0,5,7,0,6,0,0,0,
    4,0,6,0,7,5,0,3,2,
    0,1,0,0,0,0,7,0,5,
    0,0,3,0,0,0,1,9,6
]

ex2 = [  
    1,9,0,0,2,0,5,0,8,
    0,6,7,0,0,0,0,4,0,
    0,0,4,6,8,3,0,9,0,
    3,0,0,7,0,0,2,0,9,
    0,0,0,1,0,0,6,0,5,
    0,0,0,5,9,8,0,0,4,
    4,0,5,8,0,0,9,0,6,
    2,0,6,0,4,0,0,5,1,
    9,0,1,0,0,6,0,7,0
]

solver = Solver(ex1)
run = True
while run:
    #clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    window.fill(pg.Color('white'))

    # The board needs to be valid before we check if it is solved
    if solver.valid:
        if solver.solved():
            # Go through the internal stack of filled-in squares and highlight them
            while solver.stack:
                idx = solver.stack.pop()
                solver.board.get_square(idx).rect.fill(pg.Color('lightblue'))
                solver.board.get_square(idx).init()
        else:
            # The step() method increases the integer at the first blank square, checks if
            # it is a valid solution for that square, and moves on (and possibly backtracks). 
            # The function is designed to return whenever a single change is made to a square, 
            # so that we can print out the modified board later
            solver.step()
    else:
        print 'Not a solvable board'

    solver.draw(window)
    pg.display.update()
