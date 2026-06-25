import turtle
import time


#penup() and pendown() control whether the turtle draws while moving.
t=turtle.Turtle()
t.forward(100)
time.sleep(1)
t.left(90)

t.penup()

t.forward(100)
time.sleep(1)
t.left(90)

t.pendown()

t.forward(100)
time.sleep(1)
t.left(90)

t.penup()

t.forward(100)
time.sleep(1)
t.left(90)



turtle.done()