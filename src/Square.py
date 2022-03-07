import pygame as pg
pg.font.init()

FONT = pg.font.Font(None, 32)

class Square:
    def __init__(self, x, y, a=50, text=''):
        self.x = x
        self.y = y
        self.a = a # length of a side
        self.bgcolor = pg.Color('black')
        self.text = text
        self.text_surface = FONT.render(text, True, pg.Color('black'))
        self.rect = pg.Rect(x, y, self.a, self.a)

    def size(self):
        return self.a

    def update(self, text):
        self.text = text
        self.text_surface = FONT.render(text, True, pg.Color('black'))

    def draw(self, window):
        pg.draw.rect(window, self.bgcolor, self.rect, 1)
        if self.text != '0':
            window.blit(self.text_surface, (self.x + self.a / 2 - 5, self.y + self.a / 2 - 5))
        