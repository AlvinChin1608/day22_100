from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.penup()
    center_line.hideturtle()
    center_line.goto(0, 300)
    center_line.setheading(270)

    while center_line.ycor() > -300:
        center_line.pendown()
        center_line.forward(10)
        center_line.penup()
        center_line.forward(10)


screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Draw the center line
draw_center_line()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # ball moving too fast, so let it sleep to slow down
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        print("Made contact")
        ball.bounce_x()


    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

