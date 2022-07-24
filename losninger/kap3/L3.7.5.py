from turtle import *
speed(0)

def kvadrat(farge):
  fillcolor(farge)
  begin_fill()
  for i in range(4):
    forward(50)
    left(90)
  end_fill()

kvadrat("brown")
forward(50)
kvadrat("white")
forward(50)
kvadrat("brown")
hideturtle()