from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0


    def update_board(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="Center", font=("Verdena", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="Center", font=("Verdena", 80, "normal"))


    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_board()


    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_board()