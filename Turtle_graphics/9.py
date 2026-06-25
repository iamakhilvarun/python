import turtle
import time
t = turtle.Turtle() 

t.goto(-250,0)
t.home()
t.goto(250,0)
t.home()
t.goto(0,250)
t.home()
t.goto(0,-250)

t.circle(250) # The circle() method is used to draw a circle or part of a circle (an arc).

turtle.done()
