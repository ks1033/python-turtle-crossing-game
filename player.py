STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.goto(0,-280)
        self.left(90)

    def player_reset(self):
        self.goto(0, -280)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(0,new_y)

    def move_down(self):
        new_y = self.ycor() -20
        self.goto(0,new_y)