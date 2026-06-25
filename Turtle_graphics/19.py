import turtle
import time

t=turtle.Turtle()

t.turtlesize(10)
t.pensize(5)
t.color('red','green') # the first parameter changes the pen colr and second parameter changes turtle object color 
# # changes both turtle object and line color
t.pencolor('red')# changes only line color
t.fillcolor("blue") # changes turtle object color
for i in range(4):
    t.forward(150)
    t.left(90)
    time.sleep(1)
    

turtle.done()