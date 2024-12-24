from turtle import  Turtle, Screen

thomas = Turtle()
screen = Screen()

def move_forward():
    thomas.forward(15)

def move_up():
    thomas.setheading(90)
    thomas.forward(15)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Up", fun=move_up)
screen.exitonclick()