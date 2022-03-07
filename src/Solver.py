from Board import Board
from Square import Square

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
        self.valid = True # the board can be solved
        self.square_complete = True
        self.stack = [] # stack; contains the index of squares to be worked on
        # populate board
        
        k = 0
        for i in range(81):
            self.board.update(i, example_board[i])

        self.index = self.find_next_blank(0)
        if self.index == -1:
            self.valid = False
        else:
            self.stack.append(self.index)

    def find_next_blank(self, i):
        while i < 81 and self.board.get(i) != 0:
            i += 1
        return i if i < 81 else -1
            
    def step(self): # perform next step in the solution
        self.index = self.stack[-1]
        val = self.board.get(self.index)

        if val != 9:
            self.board.update(self.index, val + 1)
            if self.is_valid_square(self.index):
                self.index = self.find_next_blank(self.index)
                if self.index != -1:
                    self.stack.append(self.index)
        else:
            if not self.stack:
                valid = False
            else:
                self.board.update(self.index, 0)
                self.index = self.stack.pop()


    def is_valid_square(self, index):
        if not 0 <= index < 81:
            return False
        if self.board.get(index) == 0:
            return False
        value = self.board.get(index)

        row = index / 9
        col = index % 9
        
        for i in range(9):
            if i != col and value == self.board.get_xy(row, i):
                return False
            if i != row and value == self.board.get_xy(i, col):
                return False
        if row < 3:
            if col < 3:
                for i in range(3):
                    for j in range(0, 3):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            elif col < 6:
                for i in range(3):
                    for j in range(3, 6):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(3):
                    for j in range(6, 9):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
        elif row < 6:
            if col < 3:
                for i in range(3, 6):
                    for j in range(0, 3):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            elif col < 6:
                for i in range(3, 6):
                    for j in range(3, 6):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(3, 6):
                    for j in range(6, 9):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
        else:
            if col < 3:
                for i in range(6, 9):
                    for j in range(0, 3):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            elif col < 6:
                for i in range(6, 9):
                    for j in range(3, 6):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
            else:
                for i in range(6, 9):
                    for j in range(6, 9):
                        if (i, j) != (row, col) and value == self.board.get_xy(i, j):
                            return False
                            
        return True

    def draw(self, window):
        self.board.draw(window)

    def solved(self):
        return self.valid and self.index == -1
