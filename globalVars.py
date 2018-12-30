from random import choice
from colors import tkColors

class globalVars (object) :

    def __init__ (self) :
        self.reset()

    def reset (self) :
        self.canvasWidth, self.canvasHeight = 640, 480
        self.background = choice(tkColors)
        self.mainColor = choice(tkColors)
        self.firstX = -75000
        self.iteration = self.firstX
        self.platformSpeed = 5
        self.ballSpeed = 2
    
    def colorSwitch (self) :
        self.mainColor = choice(tkColors)
        self.background = choice(tkColors)
        while self.mainColor == self.background :
            self.mainColor = choice(tkColors)
        

    


    