from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('lightgreen')
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write("Score: 0", align='center', font=('verdana', 12,
                                                     'normal'))