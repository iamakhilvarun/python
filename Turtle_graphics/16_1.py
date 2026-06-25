import turtle
import time

t=turtle.Turtle()

x,y=t.position()
print(x,y)
t.goto(180,0)   
time.sleep(1)
t.goto(180,240)

distance=t.distance(x,y)
print(distance)
turtle.done()