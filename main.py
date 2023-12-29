from turtle import Turtle, Screen

window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

worm_list = []


def create_worm(x, y):
    worm = Turtle(shape='square')
    worm.color('white')
    worm.penup()
    worm.setposition(x, y)
    worm_list.append(worm)


x_position = 0
y_position = 0
for _ in range(3):
    create_worm(x_position, y_position)
    x_position += -20


window.exitonclick()
