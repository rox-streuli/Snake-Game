from turtle import Turtle

ALIGMENT = 'center'
FONT = ('verdana', 12, 'normal')
SCORE_BOUNDARIES = [5, 10, 15, 25]
LEVELS = {2: 0.3, 3: 0.2, 4: 0.1}
WINNER = 35
GUIDE_POSITION = (0, -290)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('lightgreen')
        self.score = 0
        self.level = 1
        self.current_speed = 0.4
        self.high_score = 0
        self.save_high_score_in_file()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        """Update current level and score banner."""
        self.write(f"Level: {self.level}\tScore: {self.score}"
                   f"\tHigh Score: {self.high_score}",
                   align=ALIGMENT, font=FONT)

    def increase_scoreboard(self):
        """Increase scoreboard by 1 and refresh score banner."""
        self.score += 1
        self.update_high_score()
        self.check_end_game()
        self.refresh_scoreboard()

    def update_high_score(self):
        """Saves high score."""
        if self.score > self.high_score:
            self.high_score = self.score

    def check_level(self):
        """Check if player reach boundary scores,
         and increase one level."""
        for score in SCORE_BOUNDARIES:
            if self.score == score:
                self.level += 1
                self.current_speed = LEVELS[self.level]

    def check_end_game(self):
        if self.score == WINNER:
            self.game_over("YOU WON!")
        else:
            self.check_level()
            self.clear()

    def game_over(self, win='GAME OVER'):
        """Write game over message on window."""
        self.goto(0, 0)
        self.clear()
        self.write(f"**** {win} ****\nScore {self.score}\tHigh Score "
                   f"{self.high_score}",
                   align=ALIGMENT, font=FONT)
        self.reset_banner()

    def reset_banner(self):
        self.clear()
        self.goto(0, 280)
        self.score = 0
        self.level = 1
        self.current_speed = 0.4
        self.read_high_score_from_file()
        self.refresh_scoreboard()

    def save_high_score_in_file(self):
        with open("data.txt", mode='w') as file:
            file.write(f"{self.high_score}")

    def read_high_score_from_file(self):
        with open("data.txt") as data:
            self.high_score = int(data.read())

class Guide(Turtle):
    """Instantiate game commands guide."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(GUIDE_POSITION)
        self.color('lightpink')
        self.write(f"To move the snake use the arrow keys. "
                   f"Press 'Q' to end game.",
                   align=ALIGMENT, font=('verdana', 10, 'normal'))