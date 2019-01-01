from random import choice
from colors import tkColors
from Platform import Platform

class globalVars (object) :

    def __init__ (self) :
        self.reset()

    def reset (self) :
        self.canvasWidth, self.canvasHeight = 640, 480
        self.background = choice(tkColors)
        self.mainColor = choice(tkColors)
        self.firstX = -Platform.length / 2
        self.iteration = self.firstX
        self.platformSpeed = 5
        self.ballSpeed = 2
        self.score = 0
        self.multiplier = 1
        self.level = 1
    
    def colorSwitch (self) :
        self.mainColor = choice(tkColors)
        self.background = choice(tkColors)
        while self.mainColor == self.background :
            self.mainColor = choice(tkColors)
        

    


    