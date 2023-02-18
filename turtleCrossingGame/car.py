import random
import time
from turtle import Turtle

COLORS = ["yellow", "red", "blue", "orange", "purple", "brown"]


class Car(Turtle):

    def __init__(self, y_pos):
        super().__init__()
        random_x = random.randint(-350, 350)
        self.hideturtle()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(random_x, y_pos)
        self.showturtle()

    def move_slow_pace(self):
        self.forward(2)

    def move_medium_pace(self):
        self.forward(4)

    def move_fast_pace(self):
        self.forward(6)

    def start_over(self):
        if self.xcor() <= -290:
            self.goto(290, self.ycor())