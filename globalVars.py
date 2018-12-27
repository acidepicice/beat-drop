from random import choice
from colors import tkColors

class globalVars (object) :


    def __init__ (self) :
        self.reset()

    def reset (self) :
        self.canvasWidth, self.canvasHeight = 640, 480
        self.background = choice(tkColors)
        self.mainColor = choice(tkColors)
        self.firstX = -125000
        self.iteration = self.firstX
        self.platformSpeed = 5

    


    