import turtle
import time
# goto() → Short and intuitive. "Go to this position."
# setposition() → More descriptive. "Set the turtle's position."
# setpos() → A shorter version of setposition().

# All three call the same underlying functionality.

t=turtle.Turtle()

time.sleep(1)

turtle.goto(0,200)
print(turtle.pos())

time.sleep(1)
turtle.setposition(200,0)

time.sleep(1)
turtle.setpos(0,0)

turtle.done()