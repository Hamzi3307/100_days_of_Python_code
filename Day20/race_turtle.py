from turtle import Turtle, Screen
import random

#tim = Turtle()
my_scr = Screen()
my_scr.setup(width=500, height=400)
colors = ["red", "orange", "blue", "green", "pink", "purple"]
user_bet = my_scr.textinput(title="Make a Bet", prompt=f"{colors}, You bet on: ")
y_position = [-75, -45, -15, 15, 45, 75]
all_turtles = []
race_on = False

for index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(x=-230, y= y_position[index])
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for tim in all_turtles:
        if tim.xcor() > 225:
            race_on = False
            winner = tim.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner.upper()} turtle is the winner")
            else: print(f"You've lost! The {winner.upper()} turtle is the winner")
        tim.forward(random.randint(0,10))    

my_scr.exitonclick()