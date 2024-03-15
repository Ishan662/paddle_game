from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

x_paddle=Paddle(350,0)
y_paddle=Paddle(-350,0)
ball=Ball()
ball.speed(0.6)
screen.listen()
screen.onkey(x_paddle.go_up, "Up")
screen.onkey(x_paddle.go_down, "Down")
screen.onkey(y_paddle.go_up, "w")
screen.onkey(y_paddle.go_down, "s")
scoreboard=ScoreBoard()


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(x_paddle) <50 and ball.xcor() > 320 or ball.distance(y_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update()

screen.exitonclick()