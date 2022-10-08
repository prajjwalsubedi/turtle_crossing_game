import random
import time
from  turtle import Turtle
from player import Player
from turtle import Screen
from cars import Car, LANE, car_list

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

for x in range(random.randint(25,40)):
    car = Car()
    car.fd(2)

player = Player()
screen.listen()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
player.print_level()
is_game_on = True
sleep_time = 0.1
while is_game_on:

    screen.update()
    for x in car_list:
        x.move()
        if x.xcor() < -260:
            x.goto(280, x.ycor())
        if player.distance(x) < 30:
            tim = Turtle()
            tim.hideturtle()
            tim.write("GAME OVER!!!", align='center', font=('Arial', 54, 'normal'))
            is_game_on = False
    time.sleep(sleep_time)

    if player.ycor() > 280:
        player.goto(0, -280)
        sleep_time -= 0.01
        time.sleep(0.2)
        player.update_point()
        player.print_level()


screen.exitonclick()