from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.color("red")
        self.shape("turtle")
        self.shapesize(1.2, 1.2)
        self.goto(0, -280)
        self.tim = Turtle()

    def up(self):
        self.seth(90)
        self.fd(10)

    def down(self):
        self.seth(270)
        self.fd(10)

    def print_level(self):
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.goto(-230, 240)
        self.tim.clear()
        self.tim.write(f"Level {self.level}", align='center', font=('Arial', 24, 'normal'))

    def update_point(self):
        self.level += 1
        self.tim.clear()