import turtle
import time
# clear() -> Erases all drawings but keeps the turtle's current position, direction, and settings.

# reset() -> Erases all drawings and restores the turtle to its default state
#            (center position, facing right, default colors, pen size, etc.).
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