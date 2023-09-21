from turtle import Turtle, Screen
tim = Turtle()
my_scr = Screen()

def forward():
    tim.forward(100)

def backward():
    tim.backward(100)
    
def left():
    tim_heading = tim.heading() + 10
    tim.setheading(tim_heading)
    
def right():
    tim_heading = tim.heading() - 10
    tim.setheading(tim_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.penup()

my_scr.listen()
my_scr.onkey(key="f", fun=forward)
my_scr.onkey(key="b", fun=backward)
my_scr.onkey(key="l", fun=left)
my_scr.onkey(key="r", fun=right)
my_scr.onkey(key="c", fun=clear)






my_scr.exitonclick()