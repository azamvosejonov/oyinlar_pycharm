from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.sanash = 0

    def update_socreboard(self):
        self.goto(0, 200)
        self.write(f'Score: {self.score}'f'|{self.sanash}', align='center', font=('Arial', 24,"normal"))
    def add_score1(self):
        self.score+=1
        self.clear()
        self.update_socreboard()
    def add_score2(self):
        self.sanash+=1
        self.clear()
        self.update_socreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Arial', 24,"normal"))


