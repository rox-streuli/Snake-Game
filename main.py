import turtle
from turtle import Turtle, Screen
import time
from random import randint
# create window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

# Turn off .tracer()
window.tracer(0)
worm_list = []
food_list = []


def create_worm(x, y, colour='white'):
    """Create a worm segment."""
    worm = Turtle(shape='square')
    worm.color(colour)
    worm.speed('fast')
    worm.penup()
    worm.setposition(x, y)
    return worm


def move_worm(worm, degrees=0):
    """Set head new heading and move worm."""
    turtle.update()
    worm.setheading(degrees)
    for segment in worm_list:
        segment.forward(20)
    turtle.update()
    shift_headings()


def shift_headings():
    """Shift worm headings."""
    heading_list = []
    for worm in worm_list[:-1]:
        heading_list.append(worm.heading())
    for index, heading in enumerate(heading_list):
        worm_list[index + 1].setheading(heading)



def move_up():
    if worm_list[0].heading() != 270:
        move_worm(worm_list[0], 90)


def move_right():
    if worm_list[0].heading() != 180:
        move_worm(worm_list[0], 0)


def move_left():
    if worm_list[0].heading() != 0:
        move_worm(worm_list[0], 180)


def move_down():
    if worm_list[0].heading() != 90:
        move_worm(worm_list[0], 270)


def food():
    x = randint(0, 550)
    y = randint(0, 550)
    food_list+= create_worm(x, y, colour='cyan')


# orininal positions
x_position = 0
y_position = 0

# Create starter worm
for _ in range(3):
    new_segment = create_worm(x_position, y_position)
    worm_list.append(new_segment)
    x_position += -20
print(worm_list)
game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    # Collect key-events
    turtle.listen()
    turtle.onkey(move_down, key='Down')
    turtle.onkey(move_up, key='Up')
    turtle.onkey(move_right, key='Right')
    turtle.onkey(move_left, key='Left')

window.exitonclick()
