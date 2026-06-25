import turtle
import time

t=turtle.Turtle()

for i in range(6):
    time.sleep(1)
    t.backward(200)
    t.left(60)

turtle.done()