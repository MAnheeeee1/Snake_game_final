from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over!\nFinal score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))




