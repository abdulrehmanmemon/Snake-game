from turtle import Turtle,Screen
timpy=Turtle()
screen=Screen()
screen.listen()
def up_move():
    timpy.forward(10)
def right_move():
    timpy.right(90)
def left_move():
    timpy.left(90)
def back():
    timpy.back(10)
screen.onkey(key='Up',fun=up_move)
screen.onkey(key='Right',fun=right_move)
screen.onkey(key='Left',fun=left_move)
screen.onkey(key='Down',fun=back)

screen.exitonclick()