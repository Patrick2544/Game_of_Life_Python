# views.py implements a way to display the life grid and its evolution.

import curses

from time import sleep

from Game_of_Life.grid import LifeGrid

__all__ = ["CursesView"]

# use the curses package from the standard library to display the evolution of the game.
class CursesView:

    def __init__(self, pattern, gen=10, frame_rate=7, bbox=(0, 0, 40, 20)):
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    # The .show() method will have the responsibility of displaying 
    # the life grid on the screen
    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = LifeGrid(self.pattern)
        # calls .curs_set() to set the cursor’s visibility. 
        # In this case, set 0 as an argument (the cursor will be invisible).
        curses.curs_set(0)
        screen.clear()

        # define a try … except block that raises a ValueError exception 
        # when the current terminal window doesn’t have enough space to display the life grid.
        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"error: terminal too small for pattern '{self.pattern.name}'"
            )  
        #  starts a loop that will run as many times as the number of generations.
        for _ in range(self.gen):
            current_grid.evolve()
            # The first two arguments define the row and column where you want to start drawing the life grid.
            # (0, 0) is the upper left corner of the terminal window.
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            # refreshes the screen by calling .refresh(). 
            # This call updates the screen immediately to reflect the changes from the previous call to .addstr()
            screen.refresh()
            # calls sleep() to set the frame rate 
            # that uses to display consecutive generations in the grid.
            sleep(1 / self.frame_rate)


