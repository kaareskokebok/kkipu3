from turtle import *
speed(9)

def oyemonster():
  circle(25)
  fillcolor("gray")
  begin_fill()
  circle(15)
  end_fill()
  fillcolor("black")
  begin_fill()
  circle(10)
  end_fill()

oyemonster()
forward(75)
oyemonster()
penup()
right(90)
forward(50)
left(90)
pendown()
oyemonster()
backward(75)
oyemonster()
hideturtle()