class Platform (object) :

    length = 530
    height = 20
    y = 430
    y2 = y + height

    def __init__ (self, canvas, x, fill) :
        self.canvas = canvas
        self.x = x
        self.x2 = self.x + self.length
        self.fill = fill
        self.body = self.canvas.create_rectangle(self.x, self.y, self.x2, self.y2, fill=self.fill)

    