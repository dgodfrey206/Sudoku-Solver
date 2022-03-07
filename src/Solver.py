from Board import Board

example_board = [  
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

class Solver:
    def __init__(self, b=example_board):
        self.board = Board()
        self.index = 0
        self.valid = True # the board can be solved
        self.stack = [] # stack; contains the index of squares to be worked on
        self.stack_idx = -1 # current element in stack
        # populate board
        
        for i in range(81):
            self.board.update(i, b[i])

        self.index = self.find_next_blank(0)
        if self.index == -1:
            self.valid = False

    def find_next_blank(self, i):
        while i < 81 and self.board.get(i) != 0:
            i += 1
        return i if i < 81 else -1
            
    def step(self): # perform next step in the solution
        val = self.board.get(self.index)
        self.board.update(self.index, val + 1)

        if self.is_valid_square(self.index):
            self.stack.append(self.index)
            self.index = self.find_next_blank(self.index)
        elif val + 1 == 9:
            if not self.stack:
                self.valid = False
            else:
                while len(self.stack) >= 0 and self.board.get(self.index) == 9:
                    self.board.update(self.index, 0)
                    self.index = self.stack.pop()
                if self.board.get(self.index) == 9:
                    self.valid = False


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
