from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(280)
        self.update()

    def add_score(self):
        self.clear()
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, "center", ("Times", 15, "bold"))

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.scoreboard()
