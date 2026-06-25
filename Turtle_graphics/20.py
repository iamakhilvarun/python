import turtle
import time

t=turtle.Turtle()
t.color('blue','yellow')

t.pensize(10)
#begin_fill() → "Start remembering the shape I'm drawing."
t.begin_fill()

# Draw the shape.
t.circle(100)

#end_fill() → "Now fill that shape with the fill color."
t.end_fill()

time.sleep(2)
t.reset()
turtle.done()