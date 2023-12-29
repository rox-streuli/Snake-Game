from turtle import Turtle, Screen

# create window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

worm_list = []


def create_worm(x, y):
    """Create a segment of the worm."""
    worm = Turtle(shape='square')
    worm.color('white')
    worm.penup()
    worm.setposition(x, y)
    worm_list.append(worm)


def move_worm():
    pass

# orininal positions
x_position = 0
y_position = 0

# Create starter worm
for _ in range(3):
    create_worm(x_position, y_position)
    x_position += -20


window.exitonclick()
