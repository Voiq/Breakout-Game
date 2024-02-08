from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score=0
        
    def update_scoreboard(self):
        self.goto(-100,205)
        self.write(self.score,align="center",font=("Courier",80,"normal"))
    def point(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
