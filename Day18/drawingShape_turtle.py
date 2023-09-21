from turtle import Screen, Turtle
import random
tim = Turtle()

# List of common color names
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white"]


# drawing triangle, square, pentagon, hexagon, ...

text = "Drawing Using Turtle\n\n\n"
font = ("Arial", 12, "bold")
tim.write(text, font=font)

for i in range(7):
    tim.color(random.choice(colors))
    for _ in range(i+3):
        tim.forward(100)
        tim.right(360/(i+3))






scr = Screen()
scr.exitonclick()