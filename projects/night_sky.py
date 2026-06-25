import turtle
import time
import random
screen=turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor('dark blue') 
screen.title("The Night skyline")

t = turtle.Turtle()
t.speed(0)
# t.pen(shown=False)

time.sleep(1)

#MOON
t.penup()
t.goto(170,180)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

#stars
t.penup()
for _ in range(80):
    x=random.randint(-380,380)
    y=random.randint(-200,250)
    size=random.randint(1,3)
    color=random.choice(['white','yellow','lightgray'])
    t.goto(x,y)
    t.dot(size,color)

# road
t.penup()
t.goto((-400, -220))
t.pendown()
t.fillcolor("gray20")

t.begin_fill()

t.forward(800)
t.right(90)
t.forward(80)
t.right(90)
t.forward(800)
t.right(90)
t.forward(80)

t.end_fill()  

# STREET LIGHT
t.penup()
t.goto(-300, -220)
t.pendown()
t.pensize(8)
t.pencolor('black')

# Draw the pole (vertical line going up)
t.setheading(90)  # Face up
t.forward(150)

# Draw the arm extending to the right
t.pensize(5)
t.right(90)  # Turn to face right
t.forward(60)

# Draw the light bulb/fixture (circle)
t.penup()
t.forward(20)  # Move a bit further for the lamp
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
t.circle(15)  # Yellow circular light
t.end_fill()

# Optional: Add a glow effect around the light
t.penup()
t.goto(-300 + 80, -220 + 150 + 20)  # Position at light center
t.pencolor('orange')
t.pensize(1)
t.circle(25)  # Orange glow ring

t.hideturtle()
turtle.done()