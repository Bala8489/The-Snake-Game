
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()  #to hide the arrow mark in screen
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score : {self.score}",align="center",font=("Arial",10,"bold"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",20,"bold"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

