class Cell:
    # boolean to see if cell has been passed by generator
    passed = False
    
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
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
    
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
