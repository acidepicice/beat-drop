from Tkinter import *
from Platform import Platform
from colors import tkColors
from random import choice
from globalVars import globalVars


root = Tk()
root.title("beat-drop")
g = globalVars()
canvas = Canvas(root, width=g.canvasWidth, height=g.canvasHeight, bg=g.background)
canvas.pack()
floorlist = []
movingLeft, movingRight = False, False


def setup() :

    g.reset()
    
    while True :
        g.mainColor = choice(tkColors)
        if g.mainColor != g.background: 
            break

    while floorlist :
        del(floorlist[0])

    for x in xrange(250) :
        if x == 0 or x == 249:
            print g.iteration
        floorlist.append(Platform(canvas, g.iteration, g.mainColor))
        g.iteration = g.firstX + x*640

setup()

def moveLeft(event) :
    global movingLeft, movingRight
    movingRight = False
    movingLeft = True

def moveRight(event) :
    global movingLeft, movingRight
    movingLeft = False
    movingRight = True

def stopLeft(event) :
    global movingLeft
    movingLeft = False
def stopLeft(event) :
    global movingLeft
    movingLeft = False
def stopRight(event) :
    global movingRight
    movingRight = False


root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRight)
root.bind('<KeyRelease-Left>', stopLeft)
root.bind('<KeyRelease-Right>', stopRight)

def tick() :
    global movingLeft, movingRight
    if movingLeft :
        for platform in floorlist :
            canvas.move(platform.body, -g.platformSpeed, 0)
            platform.x -= g.platformSpeed
            platform.x2 -= g.platformSpeed
    
    if movingRight :
        for platform in floorlist :
            canvas.move(platform.body, g.platformSpeed, 0)
            platform.x += g.platformSpeed
            platform.x2 += g.platformSpeed

    canvas.after(5, tick)


canvas.after(5, tick)
root.mainloop()