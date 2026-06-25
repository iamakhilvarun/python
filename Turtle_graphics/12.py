import turtle
import time

# There are two ways wwe can clear our stamps/traces 
# 1st would be clearstamps which clear all the stamps 
# 2nd would be clearstamp which we have to specify which stamp we need to clear

t=turtle.Turtle()

stamp_no_list=[]

for i in range(6):
    stamp_no=t.stamp()
    stamp_no_list.append(stamp_no)
    t.forward(100)
    t.left(60)
for i in range(6):   
    time.sleep(1)
    t.clearstamp(stamp_no_list[i])

turtle.done()