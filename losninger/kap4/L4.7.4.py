from turtle import *
speed(0)
shape("circle")

radius = 100
riss = radius/4
for i in range(12):
  circle(radius, 360/12)
  left(90)
  forward(riss)
  backward(riss)
  right(90)
penup()
left(90)
forward(radius)