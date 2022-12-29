from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("black")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()

        # self.right_border()

    def update_scoreboard(self):
        # self.penup()
        # self.goto(0, 300)
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()


    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290, 290)
        self.left_border()

    def left_border(self):
        self.goto(-290, 290)
        self.pendown()
        self.goto(-290, -290)
        self.goto(290, -290)
        self.goto(290, 290)
        self.goto(-290, 290)
