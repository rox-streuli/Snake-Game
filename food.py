from turtle import Turtle
from random import randrange

class Food(Turtle):
    def __init__(self):
        """Instantiate a Food object. Inherits from Turtle class."""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('cyan')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(randrange(-260, 260), randrange(-260, 260))