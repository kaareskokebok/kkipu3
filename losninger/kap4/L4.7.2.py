from turtle import *
speed(0)
pensize(5)
radius = 30

for i in range(8):
  penup()
  circle(radius, 30)
  pendown()
  circle(radius, 120)
  penup()
  circle(radius, -150)
  radius += 15
  sety(ycor() - 15)