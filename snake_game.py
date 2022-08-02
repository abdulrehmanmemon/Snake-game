import time
from turtle import Turtle,Screen
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Everywhere")
screen.tracer(0)
start=[(0,0),(-20,0),(-40,0)]
snakes=[]
for posi in start:
    snake=Turtle(shape="square")
    snake.color('white')
    snake.penup()
    snake.goto(posi)
    snakes.append(snake)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for sna in range(len(snakes)-1,0,-1):
        new_x=snakes[sna-1].xcor()
        new_y=snakes[sna-1].ycor()
        snakes[sna].goto(new_x,new_y)
    
    




screen.exitonclick()