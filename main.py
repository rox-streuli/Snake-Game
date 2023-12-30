import turtle
from turtle import Turtle, Screen
import time

# create window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

# Turn off .tracer()
window.tracer(0)
worm_list = []


def create_worm(x, y, colour='white'):
    """Create a worm segment."""
    worm = Turtle(shape='square')
    worm.color(colour)
    worm.speed('fast')
    worm.penup()
    worm.setposition(x, y)
    return worm


def move_worm(worm, degrees=0):
    # save heading for next segment
    next_segment_heading = worm.heading()
    # set head new heading
    worm.setheading(degrees)
    for segment in worm_list:
        segment.forward(20)
        turtle.update()
    worm_list[1]



def move_up():
    move_worm(worm_list[0], 90)


def move_right():
    move_worm(worm_list[0], 0)


def move_left():
    move_worm(worm_list[0], 180)


def move_down():
    move_worm(worm_list[0], 270)


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
    # change heading of first worm if needed and move
    # Collect key-events
    turtle.listen()
    turtle.onkey(move_down, key='Down')
    turtle.onkey(move_up, key='Up')
    turtle.onkey(move_right, key='Right')
    turtle.onkey(move_left, key='Left')

window.exitonclick()
