import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r, g, b)
    return new_color


# tim.color(random_color())
# tim.forward(100)

########### Challenge 5 - Spirograph ########
tim.speed("fastest")
def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(radius=100)
        tim.setheading(tim.heading() + gap)
draw_spirograph(5)

#############################################
scr = t.Screen()
scr.exitonclick()