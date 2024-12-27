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
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0)
        turtle.pendown()

        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.end_fill()
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
        turtle.penup()

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.setheading(0)
        turtle.pendown()

        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.penup()

    def pushdisk(self, disk):
        if self.stack:
            top_disk = self.stack[-1]
            disk.newpos(self.pxpos - disk.dwidth / 2, top_disk.dypos + top_disk.dheight)
        else:
            disk.newpos(self.pxpos - disk.dwidth / 2, self.pypos)
        
        self.stack.append(disk)
        disk.showdisk()

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.cleardisk()

            if self.stack:
                top_disk = self.stack[-1]
                # Move remaining disks down
                for d in self.stack:
                    d.newpos(d.dxpos, d.dypos - d.dheight)
                    d.showdisk()

if __name__ == "__main__":
    turtle.speed(5)

    disk1 = Disk(name="d1", xpos=0, ypos=0, height=20, width=60)
    disk1.showdisk()

    disk2 = Disk(name="d2", xpos=0, ypos=0, height=20, width=80)
    disk2.showdisk()

    pole1 = Pole(name="Pole 1", xpos=-50, ypos=-100, thick=10, length=200)
    pole1.showpole()

    pole2 = Pole(name="Pole 2", xpos=150, ypos=-100, thick=10, length=200)
    pole2.showpole()

    pole3 = Pole(name="Pole 3", xpos=250, ypos=-100, thick=10, length=200)
    pole3.showpole()


    pole1.pushdisk(disk1)
    pole1.pushdisk(disk2)

    pole1.popdisk()

    turtle.done()
