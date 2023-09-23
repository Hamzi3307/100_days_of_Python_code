from turtle import Turtle, Screen
import time
tim = Turtle()
my_scr = Screen()

my_scr.setup(width=600, height=600)
my_scr.bgcolor("black")
my_scr.title("Nokia Snake Game")

# to create 
my_scr.tracer(0)

positions = [(0,0), (-20,0), (-40,0)]
segments = []

for pos in positions:
    seg = Turtle("square")
    seg.color("white")
    seg.penup()
    seg.goto(pos)
    segments.append(seg)

game_on = True
while game_on:    
    my_scr.update()
    time.sleep(0.1)
    # for s in segments:
    #     s.forward(20)
    # s.left(90)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
    segments[0].forward(20)
    segments[0].left(90)
my_scr.exitonclick()