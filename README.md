# Sudoku Solver

This is a project to show animated solutions to Sodoku. It shows you how each square is individually tested, as well as the backtracking that's needed when a solution at particular square isn't possible. Make sure you are in the `main/` directory  when you run the program.

![example](https://github.com/dgodfrey206/sudoku-project/blob/master/sudokufinal.gif)

    python sudoku-solver.py

# Outline

The program divides the squares into its own class, and the square instances are compiled into a grid contained in the `Board` class. Finally, a `Board` instance is used inside the `Solver` class for solving. 
