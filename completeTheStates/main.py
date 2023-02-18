import turtle
import pandas

screen = turtle.Screen()
screen.title("States")
screen.setup(1000, 780, starty=0)
image = "india_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("state_coors.csv")

states = data["states"].tolist()
game_is_on = True
score = 0
while game_is_on:
    user_answer = screen.textinput(title=f"{score}/37 States Guessed", prompt="Next States name? ")

    if user_answer.lower() in states:
        score += 1
        state_info = data[data.states == user_answer.lower()]
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        tom.goto(float(state_info.x_cor), float(state_info.y_cor))
        tom.write(user_answer.title(), True, align="center")

    if score == 37:
        game_is_on = False
screen.mainloop()
