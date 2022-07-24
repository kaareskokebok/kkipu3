from turtle import *

speed(0)
radius = 100
while radius > 0:
  circle(radius)
  circle(-radius)
  forward(radius)
  radius -= 10
  forward(radius)
hideturtle()