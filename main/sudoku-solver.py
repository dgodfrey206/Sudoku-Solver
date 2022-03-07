import pygame as pg
import sys
sys.path.append('../src')

from Solver import Solver

pg.init()

screen_width = 450
screen_height = 450

example_board = [
    0,0,0,9,0,0,0,0,0,
    2,0,0,0,0,0,4,0,0,
    0,0,1,6,0,8,0,2,0,
    0,0,0,0,3,0,0,0,0,
    0,7,0,0,0,0,0,0,5,
    0,0,6,2,0,1,0,4,0,
    0,0,0,0,9,0,0,8,0,
    0,0,3,0,4,0,0,0,0,
    0,6,0,8,0,3,7,0,0
]

window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Sudoku Solver')
clock = pg.time.Clock()

solver = Solver(example_board)
run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    window.fill(pg.Color('white'))

    if solver.valid and not solver.solved():
        solver.step()

    solver.draw(window)
    pg.display.update()
