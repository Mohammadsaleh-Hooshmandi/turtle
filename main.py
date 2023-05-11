import turtle

screen = turtle.Screen()
jimy = turtle.Turtle("turtle")

def move():
    jimy.forward(20)

screen.listen()
screen.onkey(fun=move, key="Right")

screen.exitonclick()