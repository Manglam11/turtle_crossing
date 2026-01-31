import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.car_move()
    #detecting collision of car and turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            print("collision")
            game_is_on = False

    #detecting turtle crossing
    if player.ycor() > 300:
        print("turtle crossed")

    screen.update()

screen.exitonclick()
