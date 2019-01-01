from Tkinter import Tk, Canvas, NW
from Platform import Platform
from Ball import Ball
from Movement import Movement
from colors import tkColors
from random import choice, randint
from globalVars import globalVars


root = Tk()
root.title("beat-drop")
g = globalVars()
canvas = Canvas(root, width=g.canvasWidth, height=g.canvasHeight, bg=g.background)
canvas.pack()
floorlist = []
ball, scoreLabel = None, None

def setup() :

    print "reset"
    global ball, scoreLabel
    g.reset()
    canvas.delete('all')

    g.mainColor = choice(tkColors)
    g.background = choice(tkColors)
    while g.mainColor == g.background :
        g.mainColor = choice(tkColors)
    canvas.config(bg=g.background)
    scoreLabel = canvas.create_text(10, 5, anchor=NW, fill=g.mainColor, font='Trebuchet 20', text=str(g.score))

    while floorlist :
        del(floorlist[0])

    for x in xrange(1, 3) :
        floorlist.append(Platform(canvas, g.iteration, g.mainColor))
        g.iteration = g.firstX + x*640

    ball = Ball(canvas, randint(0, g.canvasWidth - Ball.radius), -Ball.radius, g.mainColor)

setup()

root.bind('<Left>', Movement.moveLeft)
root.bind('<Right>', Movement.moveRight)
root.bind('<Up>', Movement.moveUp)
root.bind('<Down>', Movement.moveDown)
root.bind('<KeyRelease-Left>', Movement.stopLeft)
root.bind('<KeyRelease-Right>', Movement.stopRight)
root.bind('<KeyRelease-Up>', Movement.stopUp)
root.bind('<KeyRelease-Down>', Movement.stopDown)

def tick() :
    
    if Movement.movingLeft and floorlist[0].x2 > 0:
        for platform in floorlist :
            canvas.move(platform.body, -g.platformSpeed, 0)
            platform.x -= g.platformSpeed
            platform.x2 -= g.platformSpeed
    
    if Movement.movingRight and floorlist[1].x < g.canvasWidth:
        for platform in floorlist :
            canvas.move(platform.body, g.platformSpeed, 0)
            platform.x += g.platformSpeed
            platform.x2 += g.platformSpeed
    
    if Movement.movingUp and Platform.y > 0:
        for platform in floorlist :
            canvas.move(platform.body, 0, -g.platformSpeed)
        Platform.y -= g.platformSpeed
        Platform.y2 -= g.platformSpeed
    
    if Movement.movingDown and Platform.y2 < g.canvasHeight:
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
    
    if ball.y >= g.canvasHeight :
        print("over")
        g.colorSwitch()
        canvas.config(bg=g.background)
        for platform in floorlist :
            canvas.itemconfig(platform.body, fill=g.mainColor)
        canvas.itemconfig(scoreLabel, text=g.score, fill=g.mainColor)
        
        ball.x = randint(0, g.canvasWidth-Ball.radius)
        ball.x2 = ball.x + Ball.radius
        ball.y = -Ball.radius
        ball.y2 = 0
        canvas.coords(ball.body, ball.x, ball.y, ball.x2, ball.y2)
        canvas.itemconfig(ball.body, fill=g.mainColor)
        g.score += g.multiplier
        g.level += 1
        if g.level % 5 == 0 :
            g.multiplier *= 1.5
            if g.ballSpeed < 0 :
                g.ballSpeed -= 0.5
            else :
                g.ballSpeed += 0.5
        
        
        if randint(0,1) == 0 :
            g.ballSpeed *= -1


    canvas.itemconfigure(scoreLabel, text = str(g.score))
    canvas.after(5, tick)


canvas.after(5, tick)
root.mainloop()