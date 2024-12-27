import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        turtle.penup()
        turtle.goto(self.dxpos/2, self.dypos)
        turtle.setheading(0) 
        turtle.pendown()

        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(self.dwidth/2)

        turtle.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0)  
        turtle.pendown()

        turtle.fillcolor("white")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(self.dwidth/2)

        turtle.penup()

if __name__ == "__main__":
    turtle.speed(1) 

    disk1 = Disk(name="d1", xpos=0, ypos=0, height=20, width=60)
    disk1.showdisk()
    disk1.cleardisk()
    disk1.newpos(100, 100)  
    disk1.showdisk()

    turtle.done()
