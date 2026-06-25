import turtle
import time

t=turtle.Turtle()

t.setx(250)

t.dot(50,'red')# Draws a dot with a diameter of 50 pixels.

t.goto(-250,0)

t.dot(50,'green')

t.home()

t.sety(250)

t.dot(50,'yellow')

t.home()

t.sety(-250)

t.dot(50,'blue')

t.circle(250)

turtle.done()