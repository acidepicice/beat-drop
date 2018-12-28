from Tkinter import Tk, Canvas
from Platform import Platform
from Ball import Ball
from colors import tkColors
from random import choice, randint
from globalVars import globalVars


root = Tk()
root.title("beat-drop")
g = globalVars()
canvas = Canvas(root, width=g.canvasWidth, height=g.canvasHeight, bg=g.background)
canvas.pack()
floorlist = []
ball = None
movingLeft, movingRight, movingUp, movingDown = False, False, False, False


def setup() :

    global ball
    g.reset()
    canvas.delete('all')
    
    g.mainColor = choice(tkColors)
    g.background = choice(tkColors)
    while g.mainColor == g.background :
        g.mainColor = choice(tkColors)
    canvas.config(bg=g.background)

    while floorlist :
        del(floorlist[0])

    for x in xrange(250) :
        floorlist.append(Platform(canvas, g.iteration, g.mainColor))
        g.iteration = g.firstX + x*640
    
    ball = Ball(canvas, randint(0, g.canvasWidth - Ball.radius), -Ball.radius, g.mainColor)

setup()

def moveLeft(event) :
    global movingLeft, movingRight
    movingRight = False
    movingLeft = True

def moveRight(event) :
    global movingLeft, movingRight
    movingLeft = False
    movingRight = True

def moveUp(event) :
    global movingUp, movingDown
    movingUp = True
    movingDown = False

def moveDown(event) :
    global movingUp, movingDown
    movingUp = False
    movingDown = True

def stopLeft(event) :
    global movingLeft
    movingLeft = False

def stopRight(event) :
    global movingRight
    movingRight = False

def stopUp(event) :
    global movingUp
    movingUp = False

def stopDown(event) :
    global movingDown
    movingDown = False

root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRight)
root.bind('<Up>', moveUp)
root.bind('<Down>', moveDown)
root.bind('<KeyRelease-Left>', stopLeft)
root.bind('<KeyRelease-Right>', stopRight)
root.bind('<KeyRelease-Up>', stopUp)
root.bind('<KeyRelease-Down>', stopDown)

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
    
    if movingUp :
        for platform in floorlist :
            canvas.move(platform.body, 0, -g.platformSpeed)
        Platform.y -= g.platformSpeed
        Platform.y2 -= g.platformSpeed
    
    if movingDown :
        for platform in floorlist :
            canvas.move(platform.body, 0, g.platformSpeed)
        Platform.y += g.platformSpeed
        Platform.y2 += g.platformSpeed
  
    ball.move(g.ballSpeed)

    if ball.x <= 0 or ball.x2 >= g.canvasWidth :
        g.ballSpeed *= -1

    if (ball.y2 > Platform.y and ball.y2 < Platform.y2) or (ball.y > Platform.y and ball.y < Platform.y2) :
        for platform in floorlist :
            if (ball.x > platform.x and ball.x < platform.x2) or  (ball.x2 > platform.x and ball.x2 < platform.x2):
                setup()

    canvas.after(5, tick)


canvas.after(5, tick)
root.mainloop()