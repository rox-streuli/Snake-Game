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
# Collect key-events
window.listen()
window.onkey(my_snake.head_down, key='Down')
window.onkey(my_snake.head_up, key='Up')
window.onkey(my_snake.head_right, key='Right')
window.onkey(my_snake.head_left, key='Left')

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    my_snake.move()

window.exitonclick()
