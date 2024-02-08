from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0,y=0)
        self.dx=0.4
        self.dy= -0.4