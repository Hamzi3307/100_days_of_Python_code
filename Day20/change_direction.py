from snake import Snake
from turtle import Screen
import time

my_scr = Screen()
my_scr.setup(width=600, height=600)
my_scr.bgcolor("black")
my_scr.title("Nokia Snake Game")
my_scr.tracer(0)

snake = Snake()

my_scr.listen()
my_scr.onkey(snake.up, "Up")
my_scr.onkey(snake.down, "Down")
my_scr.onkey(snake.right, "Right")
my_scr.onkey(snake.left, "Left")

game_on = True
while game_on:
    my_scr.update()
    time.sleep(0.2)
    snake.move()

my_scr.exitonclick()