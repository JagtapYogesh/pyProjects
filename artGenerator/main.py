import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
colors = [(200, 167, 110), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46)]

jack = Turtle()
s = Screen()
jack.speed("fastest")
print(jack.pos())
jack.penup()
for y in range(0, 10):
    ypos = -140 + (y * 40)
    jack.sety(ypos)

    for x in range(0, 10):
        xpos = -140 + (x * 40)
        jack.setx(xpos)
        jack.color(random.choices(colors))
        jack.pendown()
        jack.begin_fill()
        jack.circle(10)
        jack.end_fill()
        jack.penup()
s.exitonclick()
