class Ball (object) :

    radius = 20

    def __init__ (self, canvas, x, y, fill) :
        self.canvas = canvas
        self.x = x
        self.x2 = x + self.radius
        self.y = y
        self.y2 = self.y + self.radius
        self.fill = fill
        self.body = self.canvas.create_oval(self.x, self.y, self.x2, self.y2, fill=self.fill)
    
    def move(self, speed) :
        self.canvas.move(self.body, speed, abs(speed))
        self.x += speed
        self.x2 += speed
        self.y += abs(speed)
        self.y2 += abs(speed)