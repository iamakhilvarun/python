import turtle
import time

t=turtle.Turtle()
x=0
for _ in range(6):
    x = x + 60
    time.sleep(1)
    t.setheading(x) # setheading() changes the direction the turtle is facing. It does not move the turtle.
    time.sleep(1)
    t.forward(200)

turtle.done()