from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

# Initiate food
next_food = Food()

# Initiate scoreboard
scoreboard_banner = Scoreboard()

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

    # Detect collision with food
    if my_snake.head.distance(next_food) < 15:
        scoreboard_banner.increase_scoreboard()
        next_food.refresh()

    # Detect collisin with wall
    x = my_snake.head.xcor()
    y = my_snake.head.ycor()
    if x < -280 or x > 280 or y < -280 or y > 280:
        scoreboard_banner.game_over()
        game_is_on = False


window.exitonclick()
