# Sudoku Project

This is a code-up animation for solving Sodoku. It shows you how each square is individually tested, as well as the backtracking that's needed when a solution at particular square isn't possible. Make sure you are in the `main` directory  when you run the program.

<img>src/sudokugif_converted.gif</img>

    python sudoku-solver.py

# Outline

The program divides the squares into its own class, and the square instances are compiled into a grid contained in the `Board` class. Finally, a `Board` instance is used inside the `Solver` class for solving. 

# Improvements

Some features that I think would be interesting to add on is the option for the user to enter their own Sudoku problem. I was thinking that the user could enter a command-line argument to enable that option, something like `python sudoku-solver.py --manual`. Either that or we expand the size of the window and add an option for that.

# My Thoughts

This was a very fun project to make. I learned what Sudoku is and I significantly improved my understanding of recursion and backtracking algorithms along the way. I can't describe how satisfying it is seeing your program work after slaving away at the bugs for so long. Coding up the `is_valid_square()` was tricky. Converting 1D array indexes to 2D, making sure you're checking the right column and row, etc.