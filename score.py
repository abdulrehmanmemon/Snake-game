from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.update()
        self.hideturtle()
    def update(self):
        self.write(f"Score : {self.score}",align='center',font=('Courier',24,'normal'))
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=('Courier',24,'normal'))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()