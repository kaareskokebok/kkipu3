from turtle import *

radius = 150
okning = -25
for farge in ["gray", "black", "blue", "red", "yellow"]:
  fillcolor(farge)
  begin_fill() 
  circle(radius)
  end_fill()
  penup()
  sety(ycor() - okning)
  pendown
  radius += okning
hideturtle()