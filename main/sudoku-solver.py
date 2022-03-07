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

solver = Solver(ex1)
run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    window.fill(pg.Color('white'))

    if solver.valid:
        if solver.solved():
            while solver.stack:
                idx = solver.stack.pop()
                solver.board.get_square(idx).textcolor = pg.Color('darkblue')
                solver.board.get_square(idx).init()
        else:
            solver.step()
    else:
        print 'Not a solvable board'

    solver.draw(window)
    pg.display.update()
