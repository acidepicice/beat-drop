from Tkinter import *
from Platform import Platform

canvasWidth, canvasHeight = 640, 480
movingLeft, movingRight = False, False
floorlist = []
platformSpeed = 5

root = Tk()
root.title("beat-drop")
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg='white')
canvas.pack()

def setup() :

    platformSpeed = 5

    while floorlist :
        del(floorlist[0])

    for x in xrange(400) :
        floorlist.append(Platform(canvas, 3))

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
            canvas.move(platform.body, -platformSpeed, 0)
    
    if movingRight :
        for platform in floorlist :
            canvas.move(platform.body, platformSpeed, 0)

    canvas.after(5, tick)


canvas.after(5, tick)
root.mainloop()