from turtle import Turtle, Screen
import random

tim = Turtle()

directions = [90, 180, 270]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white"]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(15)
    tim.setheading(random.choice(directions))

scr = Screen()
scr.exitonclick()