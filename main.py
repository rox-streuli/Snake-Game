from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Guide
import time


def quit_game():
    game_is_on = False


# create window
window = Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('Snake Game')

# Turn off .tracer()
window.tracer(0)

# create snake
my_snake = Snake()

# create food
next_food = Food()

# create main scoreboard
scoreboard_banner = Scoreboard()

# create game guide
guide = Guide()

# Collect key-events
window.listen()

window.onkey(my_snake.head_down, key='Down')
window.onkey(my_snake.head_up, key='Up')
window.onkey(my_snake.head_right, key='Right')
window.onkey(my_snake.head_left, key='Left')

window.onkey(quit_game, key='q')

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(scoreboard_banner.current_speed)
    my_snake.move()

    # Detect collision with food
    if my_snake.head.distance(next_food) < 15:
        scoreboard_banner.increase_scoreboard()
        my_snake.extend()
        next_food.refresh()

    # Detect collisin with wall
    x = my_snake.head.xcor()
    y = my_snake.head.ycor()
    if x < -290 or x > 290 or y < -290 or y > 290:
        scoreboard_banner.game_over()

    # Detect collision with tail
    for segment in my_snake.body[4:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard_banner.game_over()

window.exitonclick()
