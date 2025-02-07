import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1,random.randint(2,3))

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def reset_car(self):
        new_x = random.randint(400, 1200)
        new_y = random.randint(-240, 260)
        self.goto(new_x, new_y)

    def increase_speed(self):
        self.backward(10)



