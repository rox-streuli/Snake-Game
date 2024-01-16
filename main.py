from turtle import Screen
from snake import Snake
import time

# create window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

# Turn off .tracer()
window.tracer(0)

# Initiate snake
my_snake = Snake()

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    my_snake.move()

window.exitonclick()
