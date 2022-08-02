from ctypes import alignment
from snake_class import snake
from turtle import Screen
import time
from score import scoreboard
from food_snake import Food
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake EveryWhere")
screen.tracer(0)
s_nake=snake()
food=Food()
score_eat=scoreboard()
screen.listen()
screen.onkey(key="Up",fun=s_nake.up)
screen.onkey(key="Down",fun=s_nake.down)
screen.onkey(key="Right",fun=s_nake.right)
screen.onkey(key="Left",fun=s_nake.left)
game_is_on=True
t=0.15
while game_is_on:
    screen.update()
    time.sleep(t)
    s_nake.snake_move()
    if s_nake.head.distance(food)<15:
        food.refresh()
        s_nake.extend()
        score_eat.increase_score()
    if s_nake.head.xcor()>290 or s_nake.head.xcor()<-300 or s_nake.head.ycor()>300 or s_nake.head.ycor()<-290:
        game_is_on=False
        score_eat.gameover()
    for sn in s_nake.snakes[1:]:
        if s_nake.head.distance(sn)<10:
            game_is_on=False
            score_eat.gameover()
    if score_eat.score%2==0 and score_eat.score!=0:
        t-=0.000001
screen.exitonclick()