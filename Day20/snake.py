from turtle import Turtle
POSITIONS = [(0,0), (-20,0), (-40,0)]
STEP = 20
class Snake :
    
    def __init__(self):
        self.segments = []
        self.createSnake()

    def createSnake(self):
        for position in POSITIONS:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x,y)
        self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
        
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        