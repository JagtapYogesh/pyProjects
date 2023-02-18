from turtle import Screen, Turtle
from car import Car
from timmy import Timmmy
from scoreboard import Scoreboard
import time

FONT = ("Courier", 20, "normal")


def game_over():
    tommy = Turtle()
    tommy.hideturtle()
    tommy.write("GAME OVER", False, align="center", font=FONT)


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(height=600, width=800)
screen.tracer(0)

timmy = Timmmy()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(timmy.move_up, "Up")
screen.onkeypress(timmy.move_down, "Down")

first_line_cars = []
second_line_cars = []
third_line_cars = []

for _ in range(0, 5):
    slow_car = Car(0)
    medium_car = Car(100)
    fast_car = Car(200)
    first_line_cars.append(slow_car)
    second_line_cars.append(medium_car)
    third_line_cars.append(fast_car)

game_is_on = True

speed = 0.05
speed_multiplier = 0.9
while game_is_on:
    print(speed)
    time.sleep(speed)
    screen.update()
    for x in range(0, 5):
        first_line_cars[x].move_slow_pace()
        first_line_cars[x].start_over()
        second_line_cars[x].move_medium_pace()
        second_line_cars[x].start_over()
        third_line_cars[x].move_fast_pace()
        third_line_cars[x].start_over()

        if timmy.distance(first_line_cars[x]) < 12 or timmy.distance(second_line_cars[x]) < 12 or timmy.distance(third_line_cars[x]) < 12:
            game_over()
            game_is_on = False

    if timmy.reached_crossing():
        scoreboard.update_score()
        speed *= speed_multiplier


screen.exitonclick()
