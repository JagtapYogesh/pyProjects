from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.resizemode("user")
        self.shape("square")
        self.goto(x_cor, 0)
        self.color("white")
        self.setheading(90)
        self.speed("fastest")
        self.shapesize(stretch_len=5)

    def move_up(self):
        self.forward(30)

    def move_down(self):
        self.backward(30)
