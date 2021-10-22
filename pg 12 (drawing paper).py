import turtle
from turtle import *

t=Turtle()
t.shape("turtle")
t.shapesize(3,3,3)
t.color("Yellow")
t.speed(0)

def lan(x,y):
    #print(x,y) #print clicking points

    t.ondrag(None)  #cleaning old values
    t.setheading(t.towards(x,y))    #turn the turtle towards clicking direction
    t.goto(x,y)
    t.ondrag(lan)

onscreenclick(lan)
turtle.done()