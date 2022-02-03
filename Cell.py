class Cell:
    # boolean to see if cell has been passed by generator
    passed = False
    
    # string to store direction cell traveled from. "O" is none
    cameFrom = "O"
    
    # dictionary to store opposite directions
    oppositeDirection = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E"
    }
    
    # list to store all active walls (all start active)
    wallList = ["N", "E", "S", "W"]
    
    # constructor
    def __init__(self, x, y, cameFrom):
        self.x = x;
        self.y = y;
    
    # method to enter a cell and effect walls
    def startPass(self, cameFrom):
        self.cameFrom = cameFrom
        passed = True
        wallList.append(oppositeDirection[cameFrom])
    
    # method to exit a cell and effect walls
    def endPass(self, goingTo):
        wallList.append(goingTo)
    
    # set/get cameFrom variable
    def setCameFrom(self, cameFrom):
        self.cameFrom = cameFrom
    def getCameFrom(self):
        return self.cameFrom
        
    # set/get passed variable
    def setPassed(self, passed):
        self.passed = passed
    def getPassed(self):
        return self.passed
    
    # get and set methods for coordinates
    def getY(self):
        return self.y
    def getX(self):
        self.y=y
    def getX(self):
        return self.x
    def setX(self, x):
        self.x=x
