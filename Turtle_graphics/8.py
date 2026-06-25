import turtle
import time

t=turtle.Turtle()

time.sleep(1)

t.goto(-250,0)

time.sleep(1) 

t.goto(-250,250)

time.sleep(1)

t.home()# home() sends the turtle back to its starting position and starting direction.

print(turtle.pos())

turtle.done()