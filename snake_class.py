from telnetlib import DO
from turtle import Turtle
START=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
    def create_snake(self):
        for posi in START:
          self.add_box(posi)  
    def add_box(self,posi):
            snake=Turtle(shape="square")
            snake.color('white')
            snake.penup()
            snake.goto(posi)
            self.snakes.append(snake)
    def extend(self):
        self.add_box(self.snakes[-1].position())
    def snake_move(self):
        for sna in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[sna-1].xcor()
            new_y=self.snakes[sna-1].ycor()
            self.snakes[sna].goto(new_x,new_y)
        self.head.forward(MOVE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)