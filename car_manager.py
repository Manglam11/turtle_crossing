from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 100
screen = Screen()

class CarManager:
    # pass
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            turtle_color = random.choice(COLORS)
            turtle_y_cor = random.randint(-240, 240)
            new_car.color(turtle_color)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(340, turtle_y_cor)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DISTANCE)


# car = CarManager()
# car.car_move()
#
# screen.exitonclick()