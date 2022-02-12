# gen2 is the recursive division algorithm implemented in python
# http://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm

from random import randint
import time


# parameters to make the maze
width = 10
height = 10
grid = [[]*width]*height


# set up constants
S, E = 1, 2
HORIZONTAL, VERTICAL = 1, 2


# helper routines
def chooseOrientation(width, height):
    if width < height:
        return HORIZONTAL
    elif height < width:
        return VERTICAL
    else:
        return randint(1, 2)

def displayMaze(grid):
    pass


# recursive division algorithm
def divide(grid, x, y, width, height, orientation):
    if width < 2 or height < 2: return
    
    displayMaze(grid)
    time.sleep(0.2)
    
    horizontal = orientation == HORIZONTAL
    
    # where will the wall be drawn from?
    wx = x + compare(horizontal, 0, randint(0, width-3))
    wy = y + compare(horizontal, randint(0, height-3), 0)
    
    # where will the passage through the wall exist?
    px = wx + compare(horizontal, randint(width-1), 0)
    py = wy + compare(horizontal, 0, randint(height-1))
    
    # how long will the wall be?
    length = compare(horizontal, width, height)
    
    # what direction is perpendicular to the wall?
    dir = compare(horizontal, S, E)
    
    for i in range(length):
        if wx != px or wy != py:
            grid[wy][wx] |= dir
        wx += dx
        wy += dy
    
    nx, ny = x, y
    w, h = compare(horizontal, [width, wy-y+1], [wx-x+1, height])
    divide(grid, nx, ny, w, h, chooseOrientation(w, h))
    
    
    

# Jamis loves using ? : but I don't have that in Python. Custom function to replicate it
def compare(value, set1, set2):
    if value:
        return set2
    return set1
    
