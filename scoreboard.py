from turtle import Turtle

FONT_LEVEL = ("Courier", 12, "normal")
FONT_GAME_OVER = ("Courier", 20, "normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.ht()
        self.penup()
        self.color("black")
        self.level_increase()

    def level_increase(self):
        self.clear()
        self.current_level += 1
        self.goto(-240, 260)
        self.write(f"Level: {self.current_level}", move=False, align='center', font=FONT_LEVEL)


    def game_over_turtle(self):
        gamer_over_turtle = Turtle()
        gamer_over_turtle.ht()
        gamer_over_turtle.penup()
        gamer_over_turtle.color("black")
        gamer_over_turtle.home()
        gamer_over_turtle.write("GAME OVER", move=False, align='center', font=FONT_GAME_OVER)


