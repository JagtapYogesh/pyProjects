import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


def end_game():
    exit(0)


screen = Screen()

screen.tracer(0)
screen.title("Ping Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")

l_scorecard = Scoreboard(-100)
r_scorecard = Scoreboard(100)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()


screen.listen()
screen.onkey(end_game, "c")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() >= 340 and ball.distance(r_paddle) <= 50 or ball.xcor() <= -340 and ball.distance(l_paddle) <= 50:
        ball.x_bounce()

    if ball.xcor() >= 390:
        l_scorecard.update_score()
        time.sleep(2)
        ball.start_over()

    elif ball.xcor() <= -390:
        r_scorecard.update_score()
        time.sleep(2)
        ball.start_over()


screen.exitonclick()
