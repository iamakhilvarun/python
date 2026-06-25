import turtle
import time

t = turtle.Turtle()

for i in range(12):
    t.forward(100)
    t.right(30)
    print(
        f"x:{t.xcor()} ,y:{t.ycor()}"
    )  # xcor() and ycor() return the turtle's current coordinates.
    # They do not move the turtle. They only tell you where it is.
turtle.done()
