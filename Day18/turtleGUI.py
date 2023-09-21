from turtle import Turtle, Screen
tim = Turtle()

# Draw a Square

# text = "Drawing a square\n\n"
# font = ("Arial", 14, "bold")
# align = "center"

# tim.write(text, align=align, font=font)
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# dashed square

text = "Drawing dashed square\n\n"
font = ("Arial", 14, "bold")
align = "center"
tim.write(text, align=align, font=font)

for _ in range(4):
    for _ in range(5):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
        
    tim.right(90)

scr = Screen()
scr.exitonclick()