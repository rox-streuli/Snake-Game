from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('lightgreen')
        self.score = 0
        self.write(f"Score: {self.score}", align='center', font=('verdana', 12,
                                                                 'normal'))

    def refresh_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('verdana', 12,
                                                     'normal'))