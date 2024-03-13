from turtle import Turtle

ALIGMENT = 'center'
FONT = ('verdana', 12, 'normal')
SCORE_BOUNDARIES = [5, 10, 15, 25]
LEVELS = {2: 0.3, 3: 0.2, 4: 0.1}
WINNER = 35

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('lightgreen')
        self.score = 0
        self.level = 1
        self.refresh_scoreboard()
        self.current_speed = 0.4
        self.high_score = 0

    def refresh_scoreboard(self):
        """Update current level and score banner."""
        self.write(f"Level: {self.level}\tScore: {self.score}\tHigh Score: "
                   f"{self.high_score}",
                   align=ALIGMENT, font=FONT)

    def increase_scoreboard(self):
        """Increase scoreboard by 1 and refresh .write()"""
        self.score += 1
        if self.score == WINNER:
            self.game_over("YOU WON!")
        else:
            self.check_level()
            self.clear()
            self.refresh_scoreboard()

    def check_level(self):
        """Check if player reach boundary scores,
         and increase one level."""
        for score in SCORE_BOUNDARIES:
            if self.score == score:
                self.level += 1
                self.current_speed = LEVELS[self.level]

    def game_over(self, win='GAME OVER'):
        """Write game over message on window."""
        self.goto(0, 0)
        self.clear()
        self.write(f"**** {win} ****", align=ALIGMENT, font=FONT)
