from turtle import  Turtle, Screen

thomas = Turtle()
screen = Screen()

def move_forward():
    thomas.forward(15)

def move_backward():
    thomas.backward(15)

def clockwise(): 
    thomas.setheading(thomas.heading() + 15)

def counter_clockwise():
    thomas.setheading(thomas.heading() - 15)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.exitonclick()