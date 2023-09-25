from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 12, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.score = 0
        with open("Day24\highscore.txt") as file:
            self.highscore = int(file.read())

        # self.highscore = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            with open("Day24\highscore.txt", "w") as file:
                self.highscore = self.score
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()