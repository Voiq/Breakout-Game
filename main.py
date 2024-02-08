from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import scoreboard
import time


#------------Screen----------------
wn = Screen()
wn.bgcolor("black")
wn.title("Breakout")
wn.setup(width=600 , height = 600)
wn.tracer(0)


#Ball
ball = Ball()

#Paddle
paddle=Paddle((0,-250))

#Bricks
bricks =[]

for i in range(-200, 200, 50):
    for j in range(150, 250, 25):
        brick = Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("blue")
        brick.shapesize(stretch_wid=1, stretch_len=2.5)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

#scoreboard
scoreboard = scoreboard()



#---------KeyBindiings-----------------
wn.listen()
wn.onkeypress(paddle.go_right,"d")
wn.onkeypress(paddle.go_left,"a")



while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    elif ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision checking
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision checking
    for brick in bricks:
        if (ball.distance(brick) < 25):
            scoreboard.point()
            brick.goto(1000, 1000)  # Move the brick out of the screen
            ball.dy *= -1

    # Game over condition
    if ball.ycor() < -290:
        time.sleep(1)
        ball.goto(0, 0)
        ball.dy *= -1
