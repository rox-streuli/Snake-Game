from turtle import Turtle


class CreateSegment:
    def __init__(self, start):
        """Instantiate a snake segment."""
        self.segment = Turtle(shape='square')
        self.segment.color('white')
        self.segment.speed('fast')
        self.segment.penup()
        self.segment.setposition(start)

class Snake:
    """Intantiate a snake body."""
    starting_position = [(0, 0), (-20, 0), (-40, 0)]
    def __init__(self):
        self.body = []
        for start_pos in Snake.starting_position:
            self.body.append(CreateSegment(start_pos))

    def move(self):
        """Shift position of each segment in the snake."""
        for section in range(len(self.body) -1, 0, -1):
            new_pos = self.body[section -1].segment.position()
            self.body[section].segment.setposition(new_pos)
        self.body[0].segment.forward(20)

