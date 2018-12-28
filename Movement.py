class Movement () :

    movingLeft = False
    movingRight = False
    movingUp = False
    movingDown = False

    @staticmethod
    def moveLeft(event) :
        print "yeet"
        Movement.movingRight = False
        Movement.movingLeft = True

    @staticmethod
    def moveRight(event) :
        Movement.movingLeft = False
        Movement.movingRight = True

    @staticmethod
    def moveUp(event) :
        Movement.movingUp = True
        Movement.movingDown = False

    @staticmethod
    def moveDown(event) :
        Movement.movingUp = False
        Movement.movingDown = True

    @staticmethod
    def stopLeft(event) :
        Movement.movingLeft = False

    @staticmethod
    def stopRight(event) :
        Movement.movingRight = False

    @staticmethod
    def stopUp(event) :
        Movement.movingUp = False

    @staticmethod
    def stopDown(event) :
        Movement.movingDown = False
            