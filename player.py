from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.fd(MOVE_DISTANCE)
        # if self.ycor() == FINISH_LINE_Y:
        #     self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

# player = Player()
# while True:
#     player.player_move()
#
#
# screen.exitonclick()
