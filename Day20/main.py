from snake import Snake
from turtle import Screen
import time

my_scr = Screen()
my_scr.setup(width=600, height=600)
my_scr.bgcolor("black")
my_scr.title("Nokia Snake Game")
my_scr.tracer(0)

snake = Snake()

game_on = True
while game_on:
    my_scr.update()
    time.sleep(0.05)
    snake.move()

my_scr.exitonclick()