from Tkinter import *

class Platform (object) :
    def __init__ (self, canvas, x) :
        self.canvas = canvas
        self.x = x
        self.body = self.canvas.create_rectangle(x, 430, x+500, 450)

    