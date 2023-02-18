import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=500)
turtle_colors = ["violet", "blue", "green", "orange", "yellow", "red"]
turtle_names =["timmy", "turty", "tommy", "turry", "terry", "torry"]
is_race_on = False


user_guess = screen.textinput("Make your bet ", "Which color turtle will finish first? ")
print(user_guess)

if user_guess:
    is_race_on = True

turtles = []
first_turtle_start_y = -150

for x in range(0, 6):
    name = turtle_names[x]
    name = Turtle(shape="turtle")
    name.color(turtle_colors[x])
    name.penup()
    name.setpos(-270, first_turtle_start_y + (x * 60))
    turtles.append(name)

while is_race_on:

    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 250:
            if user_guess == turtle.pencolor():
                print("You won!!!. You guessed it right.")
            else:
                print(f"You lose!!!. {turtle.pencolor()} color turtle won the race.")
            is_race_on = False
            break

screen.exitonclick()
