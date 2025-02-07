import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
t = Player()
screen.onkey(t.move_up, "Up")
screen.onkey(t.move_down, "Down")
score = Scoreboard()
score.level_update()


cars = []

for c in range(0,30):
    X_LOC = random.randint(400, 1600)
    Y_LOC = random.randint(-240, 260)
    new_car = CarManager()
    new_car.goto(X_LOC, Y_LOC)
    cars.append(new_car)


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for i in range(len(cars)):
        cars[i].move()
        if cars[i].xcor() < -400:
            cars[i].reset_car()
        if t.ycor() > 280:
            score.reach_end()
            t.player_reset()
        if score.stage_number > 2:
            cars[i].increase_speed()
        if cars[i].distance(t) < 23:
            game_is_on = False
            score.game_over()
        if score.stage_number > 5:
            game_is_on = False
            score.game_won()


screen.exitonclick()