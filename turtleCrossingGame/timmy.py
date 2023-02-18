from turtle import Turtle


class Timmmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("green")
        self.start()

    def start(self):
        self.goto(0, -250)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def reached_crossing(self):
        if self.ycor() >= 270:
            self.start()
            return True

        return False
