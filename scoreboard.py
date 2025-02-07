from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.stage_number = 0
        self.level_update()
        self.hideturtle()
        self.color("blue")


    def level_update(self):
        self.goto(-220,260)
        self.write(f"Level:{self.stage_number}", align="center", font=FONT)


    def reach_end(self):
        self.stage_number += 1
        self.clear()
        self.level_update()

    def game_won(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"You Won!", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(f"Turtle got Killed on Road", align="center", font=FONT)