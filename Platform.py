from Tkinter import *

class Platform (object) :
    def __init__ (self, canvas, x, fill) :
        self.canvas = canvas
        self.x = x
        self.fill = fill
        self.body = self.canvas.create_rectangle(self.x, 430, x+530, 450, fill=self.fill)

    