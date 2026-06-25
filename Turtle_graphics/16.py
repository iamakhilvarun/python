import turtle
import time

t=turtle.Turtle()
print(t.heading())

for i in range(4):
    time.sleep(1)
    t.forward(100)
    t.right(90)
    print(t.heading())#It does not move or rotate the turtle. It simply tells you its current heading (angle).
    
turtle.done()