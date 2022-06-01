import pygame as pg
pg.font.init()

FONT = pg.font.Font(None, 32)

# Square of side length `a` at position x,y
class Square:
    def __init__(self, x, y, a=50, text=''):
        self.x = x
        self.y = y
        self.a = a # length of a side
        self.bgcolor = pg.Color('white')
        self.textcolor = pg.Color('black')
        self.text = text
        self.text_surface = FONT.render(text, True, self.textcolor)
        self.rect = pg.Surface((self.a, self.a))
        self.rect.fill(self.bgcolor)

    def size(self):
        return self.a

    # change the text
    def update(self, text):
        self.text = text
        self.init()

    def init(self):
        self.text_surface = FONT.render(self.text, True, self.textcolor)

    def draw(self, window):
        window.blit(self.rect, (self.x, self.y))
        for i in range(10):
            pg.draw.line(window, pg.Color('black'), (0, i * 50), (9 * self.a, i * 50), 2)
            pg.draw.line(window, pg.Color('black'), (i * 50, 0), (i * 50, 9 * self.a), 2)
        # When the value is zero keep the square blank
        if self.text != '0':
            # place the number at the center of the square
            window.blit(self.text_surface, (self.x + self.a / 2 - 5, self.y + self.a / 2 - 5))
        
