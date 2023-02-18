from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x_cor, 250)
        self.write(f"{self.score}", False, "center", ("Courier", 40, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Courier", 40, "normal"))
