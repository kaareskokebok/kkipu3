from turtle import *

y = 120  

for i in range(6):
  sety(y)
  dot(10)
  sety(0)
  forward(30)
  y -= 20

dot(10)
hideturtle()