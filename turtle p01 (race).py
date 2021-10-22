import random
import turtle
from turtle import *

a1=Turtle()
a1.shape("turtle")
a1.penup()
a1.left(90)
a1.color("red")
a1.shapesize(2,2,2)
a1.speed(0)

a2=a1.clone()
a2.color("blue")

a1.goto(-200,-200)
a2.goto(200,-200)
#------------------------------------#

x1=Turtle()
x1.penup()
x1.goto(-280,280)
x1.pendown()
x1.pensize(3)
x1.color("lightgreen")
x1.goto(280,280)
x1.hideturtle()

#---------------------------------------#

def play():
    for i in range(350):
        a1.fd(random.randrange(5))
        a2.fd(random.randrange(5))
        if (a1.position()[1]) >= 270 and (a1.position()[1]) > (a2.position()[1]) :
            print("Player 1 is winner \n P1 \t  P2")
            print(a1.position()[1], "\t", a2.position()[1])
            break
        if (a2.position()[1]) >= 270 and (a2.position()[1]) > (a1.position()[1]) :
            print("Player 2 is winner \n P1 \t  P2")
            print(a1.position()[1], "\t", a2.position()[1])
            break
play()

turtle.done()