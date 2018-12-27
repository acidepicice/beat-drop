from Tkinter import *

class Platform (object) :
    def __init__ (self, canvas, x, fill) :
        self.canvas = canvas
        self.x = x
        self.x2 = self.x + 530
        self.fill = fill
        self.body = self.canvas.create_rectangle(self.x, 430, self.x2, 450, fill=self.fill)

    