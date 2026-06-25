import turtle
import time

t = turtle.Turtle()

t.turtlesize(5)  # pensize() changes the thickness of the line the turtle draws.
t.pen(
    pensize=5, shown=True, pendown=True, fillcolor="green"
)  # shown = Makes the turtle visible.
# fillcolor = Sets the fill color to green
for i in range(6):
    t.forward(150)
    t.left(60)
    time.sleep(1)

turtle.done()
