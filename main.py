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
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    car_manager.create_car()
    car_manager.car_move()
    #detecting collision of car and turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            print("collision")
            scoreboard.game_over_turtle()
            game_is_on = False

    #detecting turtle crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.level_increase()


    screen.update()

screen.exitonclick()
