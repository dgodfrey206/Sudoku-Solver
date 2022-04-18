import pygame as pg
pg.font.init()

FONT = pg.font.Font(None, 32)

# Square of side length `a` at position x,y
class Square:
    def __init__(self, x, y, a=50, text=''):
        self.x = x
        self.y = y
        self.a = a # length of a side
        self.bgcolor = pg.Color('black')
        self.textcolor = pg.Color('black')
        self.text = text
        self.text_surface = FONT.render(text, True, self.textcolor)
        self.rect = pg.Rect(x, y, self.a, self.a)

    def size(self):
        return self.a

    # change the text
    def update(self, text):
        self.text = text
        self.init()

    def init(self):
        self.text_surface = FONT.render(self.text, True, self.textcolor)

    def draw(self, window):
        pg.draw.rect(window, self.bgcolor, self.rect, 1)
        # When the value is zero keep the square blank
        if self.text != '0':
            # place the number at the center of the square
            window.blit(self.text_surface, (self.x + self.a / 2 - 5, self.y + self.a / 2 - 5))
        
