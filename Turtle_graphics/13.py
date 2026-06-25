import turtle
import time
t=turtle.Turtle()

for i in range(8):
    t.stamp()
    t.forward(150)
    t.right(45)


for i in range(24):
    t.undo()#undo() reverses the last turtle action.
turtle.done()