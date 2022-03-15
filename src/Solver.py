from Board import Board

class Solver:
    def __init__(self, b):
        self.board = Board()
        self.index = -2 # the current square being looked at on the board (-2 because -1 is 
                        # used for another check)
        self.valid = True # the board can be solved
        self.stack = [] # stack; contains the index of squares to be worked on

        # populate board
        
        for i in range(81):
            self.board.update(i, b[i])

    # Go through the board for the next blank square
    def find_next_blank(self, i):
        while i < 81 and self.board.get(i) != 0:
            i += 1
        return i if i < 81 else -1
            
    def step(self): # perform next step in the solution
        # If index < 0, this is the first iteration, so look for the next blank square 
        if self.index < 0:
            self.index = self.find_next_blank(0)
            if self.index < 0:
                return
        # increase square value by 1
        new_val = 1 + self.board.get(self.index)
        self.board.update(self.index, new_val)

        if self.is_valid_square(self.index):
            # add current square to stack and move to the next blank square
            self.stack.append(self.index)
            self.index = self.find_next_blank(self.index)
        elif new_val == 9:
            if not self.stack:
                self.valid = False
            else:
                # continue to pop the stack until we find a square with a value under 9
                # A square with a value of 9 will backtrack so they need to be skipped
                while self.stack and self.board.get(self.index) == 9:
                    self.board.update(self.index, 0)
                    self.index = self.stack.pop()
                # No square to backtrack to, this board can't be solved
                if self.board.get(self.index) == 9:
                    self.valid = False


    # Goes through each row, column, and 3x3 subgrid and checks for duplicates
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
