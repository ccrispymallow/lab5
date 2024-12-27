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

        # Remove filling; just draw the outline
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.penup()
        
    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0)
        turtle.pendown()

        turtle.pencolor("white")
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.penup()
        turtle.pencolor("black")

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
            disk.cleardisk()  # Remove the disk visually
            return disk  # Return the disk so it can be moved to another pole

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i * 150, 20, (n - i) * 30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

if __name__ == "__main__":
    turtle.speed(0)

    h = Hanoi(n=3)
    h.solve()

    turtle.done()