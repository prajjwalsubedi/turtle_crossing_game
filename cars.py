from turtle import Turtle
import random

LANE = []
for x in range(-200, 270, 80):
    LANE.append(x)

COLORS = ["orange", "yellow", "green", "blue", "indigo", "violet", "black"]
car_list = []


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        color = random.choice(COLORS)
        self.penup()
        self.color(color)
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(x=random.choice(LANE), y=random.choice(LANE))
        self.seth(-180)
        car_list.append(self)

    def move(self):
        self.fd(10)
