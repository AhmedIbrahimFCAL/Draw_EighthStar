# Author: Ahmad_Ibrahim_AbuDanckash
# This code draws eighth star
import turtle
s=turtle.getscreen()
s.bgcolor("violet")
p=turtle.Turtle()
p.pensize(5)
p.pencolor("blue")
def right_star(num=8,steps=60):
    for i in range(num):
        p.pencolor("blue")
        p.fd(steps)
        p.lt(135)
        p.pencolor("white")
        p.fd(steps)
        p.rt(90)

right_star()
turtle.mainloop()