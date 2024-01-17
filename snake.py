from turtle import Turtle
# Constants help to refactor the code in the future
SARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Instantiate a snake body."""
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Create starting snake body."""
        for start_pos in SARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(start_pos)
            self.body.append(new_segment)


    def move(self):
        """Shift position of each segment in the snake body."""
        for section in range(len(self.body) -1, 0, -1):
            new_pos = self.body[section -1].position()
            self.body[section].setposition(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def head_up(self):
        """Change head heading to 90 if not 270."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def head_right(self):
        """Change head heading to 0 if not 180."""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def head_left(self):
        """Change head heading to 180 if not 0."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def head_down(self):
        """Change head heading to 270 if not 90."""
        if self.head.heading() != 90:
            self.head.setheading(270)
