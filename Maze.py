import random

class Maze:
    # constructor - length is x, width is y
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.cellList = [[]*width]*length
        for x in cellList:
            for y in cellList[x]:
                cellList[x][y] = Cell(x, y)
    
    # method to find and give random neighbours of given coordinate
    def findNeighbour(self, x, y):
        neighbours = []
        # may need to add try/catch, idk how python compile works
        if not cellList[x-1][y+1].getPassed():
            neighbours.append(cellList[x-1][y])
        if not cellList[x+1][y-1].getPassed():
            neighbours.append(cellList[x+1][y-1])
        if not cellList[x-1][y-1].getPassed():
            neighbours.append(cellList[x-1][y])
        if not cellList[x+1][y+1].getPassed():
            neighbours.append(cellList[x+1][y+1])
        rand = random.randint(0, len(neighbours)-1)
        return neighbours.get(rand)
        
            
