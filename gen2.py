# gen2 is the recursive division algoritem implemented in python
# http://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm
from random import randint
import time

HORIZONTAL, VERTICAL = 1, 2
S, E = 1, 2

def display_maze(grid):
    pass

def choose_orientation(width, height):
    if width < height:
        return HORIZONTAL
    elif height < width:
        return VERTICAL
    else:
        return randint(1, 2)
        
def divide(grid, x, y, width, height, orientation):
    if width < 2 or height < 2: 
        return
    
    display_maze(grid)
    time.sleep(0.2)
    
    horizontal = orientation == HORIZONTAL
    
    # where will the wall be drawn from?
    wx = x
    if horizontal:
        wx += randint(0, width-2)
    wy = y
    if not horizontal:
        wy += randint(0, height-2)
        
    # where will the passage through the wall exist?
    px = wx
    if not horizontal: px += randint(width)
    py = wy
    if horizontal: py += randint(height)
    
    # what direction will the wall be drawn?
    dx = 1
    if horizontal: dx = 0
    dy = 0
    if horizontal: dy = 1
    
    # how long will the wall be?
    
    



