# grid.py provides the life grid implementation

import collections

# Assign constant symbols for grid representation
# for .as_string()
ALIVE = '■'
DEAD = '.'

class LifeGrid:
    # Constructor
    def __init__(self, pattern):
        self.pattern = pattern
    
    # .evolve() will check the currently alive cells and their neighbors 
    # to determine the next generation of alive cells
    def evolve(self):
        '''
        The rules of how cells evolve:

        1) Alive cells die if they have fewer than two (underpopulation) or more than three living neighbors (overpopulation).
        2) Alive cells stay alive if they have two or three living neighbors.
        3) Dead cells with exactly three living neighbors become alive (reproduction).

        Coordinates diagram
        ----------------------------
        |        |        |        |
        | (0, 0) | (0, 1) | (0, 2) |
        |        |        |        |
        |---------------------------
        |        |        |        |
        | (1, 0) | (1, 1) | (1, 2) |
        |        |        |        |
        |---------------------------
        |        |        |        |
        | (2, 0) | (2, 1) | (2, 2) |
        |        |        |        |
        ----------------------------

        Assume check the cell at (1,1), the neighbor cells are the rest 8 (surrounding) cells

        How to determine neighbor cells: It is the Delta (the difference) see neighbors below
        '''
        # A tuple in Python is a collection of elements enclosed within parentheses ( ). 
        # Tuples are similar to lists but are immutable, meaning once they are created, their elements cannot be changed.
        neighbors = (
            (-1, -1), # Above Left
            (-1, 0),  # Above
            (-1, 1),  # Above Right
            (0, -1),  # Left
            (0, 1),   # Right
            (1, -1),  # Below Left
            (1, 0),   # Below 
            (1, 1),   # Below Right
        )

        # creates a dictionary for counting the number of living neighbors.
        # if you try to access a key that doesn't exist, 
        # it'll automatically create that key and assign a default value of int() to it (0 this case).
        num_neighbors = collections.defaultdict(int)

        # run a loop over the currently alive cells, which are stored in the .pattern object. 
        # This loop allows to check the neighbors of each living cell so that we can determine the next generation of living cells.
        for row, col in self.pattern.alive_cells:
            # start a loop over the neighbor (deltas). 
            # This inner loop counts how many cells the current cell neighbors.
            # This count allows you to know the number of living neighbors for both living and dead cells.
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        # build a set containing the cells that will stay alive.
        # create a set of neighbors that have two or three alive neighbors themselves. 
        # Then, find the cells that are common to both this set and .alive_cells. 
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells

        # create a set with the cells that will come alive. 
        # In this case, create a set of neighbors that have exactly three living neighbors. 
        # Then, determine the cells that come alive by removing cells that are already in .alive_cells.
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        # updates .alive_cells with the set that results 
        # as the union of the cells that stay alive and those that come alive.
        self.pattern.alive_cells = stay_alive | come_alive
    
    # .as_string() will provide a way to represent the grid as a string 
    # that can display in the terminal window.
    def as_string(self, bbox):
        # bounding box for the life grid (bbox) 
        # This box will define which part of the grid to display in the terminal window.

        # first, unpack the bounding box coordinates into four variables
        start_col, start_row, end_col, end_row = bbox

        # create the display variable as a list containing the pattern’s name
        # use .center() to center the name over the grid’s width.
        display = [self.pattern.name.center(2 * (end_col - start_col))]

        # for loop iterates over the range of rows inside the view
        for row in range(start_row, end_row):
            # create a new list containing the alive and dead cells in the current row. 
            display_row = [
                # To figure out if a given cell is alive, check if its coordinates are in the set of alive cells.
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            # append the row as a string to the display list.
            display.append(" ".join(display_row))
        # join together every string using a newline character (\n) to create the life grid as a string.
        return "\n ".join(display)
        # pass

    # special method provides a way to represent the containing object in a user-friendly manner.
    # check to know the living cells in each generation.
    def __str__(self):
        # With this method in place, when we use the built-in print() function to print an instance of LifeGrid, 
        # we get the name of the current pattern and the set of alive cells in the next line.
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )
        # pass
        # pass statement is a placeholder that allows you to define a code block that does nothing.

