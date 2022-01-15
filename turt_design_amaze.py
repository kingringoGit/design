from turtle import *
bgcolor("black")
pencolor("blue")
a=0
b=0
speed(0)
penup()
goto(0,200)
pendown()
while True:
    forward(a)
    right(b)
    a+=3
    b+=1
    if b==210:
        break
    hideturtle()