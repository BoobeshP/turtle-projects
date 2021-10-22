import turtle as t

a = t.Turtle()
a.getscreen().bgcolor("black")

a.penup()
a.goto(-200,50)
a.pendown()
a.hideturtle()
a.color("orange")
a.speed(0)

def star(t,size):
    if size <=10:
        return
    else:
        for i in range(5):
            t.begin_fill()
            t.forward(size)
            star(t,size/3)
            t.left(216)
            t.end_fill()

star(a,360)
t.done()