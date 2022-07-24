from turtle import *
speed(7)

def kvadrat(side): 
  for i in range(4):
    forward(side)
    left(90)

kvadrat(50)
backward(25)
kvadrat(100)
backward(25)
kvadrat(150)
backward(25)
kvadrat(200)
hideturtle()